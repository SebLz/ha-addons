#!/usr/bin/python3
# coding: utf-8

import json
import logging
import time
from logging.handlers import TimedRotatingFileHandler
import paho.mqtt.client as mqtt
import socketio

from _config_ import _MCZ_App_URL
from _config_ import _MCZ_device_MAC
from _config_ import _MCZ_device_serial
from _config_ import _MQTT_TOPIC_PUB
from _config_ import _MQTT_TOPIC_SUB
from _config_ import _MQTT_authentication
# MQTT
from _config_ import _MQTT_ip
from _config_ import _MQTT_pass
from _config_ import _MQTT_port
from _config_ import _MQTT_user

try:
    import thread
except ImportError:
    import _thread as thread

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s :%(name)s :: %(levelname)s :: %(message)s')
file_handler = TimedRotatingFileHandler('maestro.log', when='D', interval=1, backupCount=5)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

sio = socketio.Client(logger=True, engineio_logger=True)


class PileFifo(object):
    def __init__(self, maxpile=None):
        self.pile = []
        self.maxpile = maxpile

    def empile(self, element, idx=0):
        if (self.maxpile != None) and (len(self.pile) == self.maxpile):
            raise ValueError("erreur: tentative d'empiler dans une pile pleine")
        self.pile.insert(idx, element)

    def depile(self, idx=-1):
        if len(self.pile) == 0:
            raise ValueError("erreur: tentative de depiler une pile vide")
        if idx < -len(self.pile) or idx >= len(self.pile):
            raise ValueError("erreur: element de pile à depiler n'existe pas")
        return self.pile.pop(idx)

    def element(self, idx=-1):
        if idx < -len(self.pile) or idx >= len(self.pile):
            raise ValueError("erreur: element de pile à lire n'existe pas")
        return self.pile[idx]

    def copiepile(self, imin=0, imax=None):
        if imax == None:
            imax = len(self.pile)
        if imin < 0 or imax > len(self.pile) or imin >= imax:
            raise ValueError("erreur: mauvais indice(s) pour l'extraction par copiepile")
        return list(self.pile[imin:imax])

    def pilevide(self):
        return len(self.pile) == 0

    def pilepleine(self):
        return self.maxpile != None and len(self.pile) == self.maxpile

    def taille(self):
        return len(self.pile)


def on_connect_mqtt(client, userdata, flags, rc):
    logger.info("Connecté au broker MQTT avec le code : " + str(rc))


def on_message_mqtt(client, userdata, message):
    logger.info('Message MQTT reçu : ' + str(message.payload.decode()))
    cmd = message.payload.decode().split(",")
    if cmd[0] == "42":
        cmd[1] = (int(cmd[1]) * 2)
    Message_MQTT.empile("C|WriteParametri|" + cmd[0] + "|" + str(cmd[1]))
    logger.info('Contenu Pile Message_MQTT : ' + str(Message_MQTT.copiepile()))
    send()


def secTOdhms(nb_sec):
    qm, s = divmod(nb_sec, 60)
    qh, m = divmod(qm, 60)
    d, h = divmod(qh, 24)
    return "%d:%d:%d:%d" % (d, h, m, s)


@sio.event
def connect():
    logger.info("Connected")
    logger.info("SID is : {}".format(sio.sid))
    sio.emit(
        "join",
        {
            "serialNumber": _MCZ_device_serial,
            "macAddress": _MCZ_device_MAC,
            "type": "Android-App",
        },
    )
    sio.emit(
        "chiedo",
        {
            "serialNumber": _MCZ_device_serial,
            "macAddress": _MCZ_device_MAC,
            "tipoChiamata": 0,
            "richiesta": "RecuperoParametri",
        },
    )
    sio.emit(
        "chiedo",
        {
            "serialNumber": _MCZ_device_serial,
            "macAddress": _MCZ_device_MAC,
            "tipoChiamata": 1,
            "richiesta": "C|RecuperoInfo",
        },
    )


@sio.event
def disconnect():
    logger.error("Disconnected")



@sio.event
def rispondo(response):
    logger.info("Received 'rispondo' message")
    datas = response["stringaRicevuta"].split("|")
    from _data_ import RecuperoInfo
    for i in range(0, len(datas)):
        for j in range(0, len(RecuperoInfo)):
            if i == RecuperoInfo[j][0]:
                if len(RecuperoInfo[j]) > 2:
                    for k in range(0, len(RecuperoInfo[j][2])):
                        if int(datas[i], 16) == RecuperoInfo[j][2][k][0]:
                            MQTT_MAESTRO[RecuperoInfo[j][1]] = RecuperoInfo[j][2][k][1]
                            break
                        else:
                            MQTT_MAESTRO[RecuperoInfo[j][1]] = ('Code inconnu :', str(int(datas[i], 16)))
                else:
                    if i == 6 or i == 26 or i == 28:
                        MQTT_MAESTRO[RecuperoInfo[j][1]] = float(int(datas[i], 16)) / 2

                    elif i >= 37 and i <= 42:
                        MQTT_MAESTRO[RecuperoInfo[j][1]] = secTOdhms(int(datas[i], 16))
                    else:
                        MQTT_MAESTRO[RecuperoInfo[j][1]] = int(datas[i], 16)
    logger.info('Publication sur le topic MQTT ' + str(_MQTT_TOPIC_PUB) + ' le message suivant : ' + str(
        json.dumps(MQTT_MAESTRO)))
    client.publish(_MQTT_TOPIC_PUB, json.dumps(MQTT_MAESTRO), 1)


def receive(*args):
    while True:
        time.sleep(30)
        logger.info("Websocket still connected ? " + str(sio.connected))
        if sio.connected:
            logger.info("Envoi de la commande pour rafraichir les donnees")
            sio.emit(
                "chiedo",
                {
                 "serialNumber": _MCZ_device_serial,
                 "macAddress": _MCZ_device_MAC,
                 "tipoChiamata": 1,
                 "richiesta": "C|RecuperoInfo",
                },
            )
            time.sleep(15)
        else:
            logger.warning("Websocket disconnected ! Waiting 30seconds")
            time.sleep(30)


def send():
    def run(*args):
        time.sleep(_INTERVALLE)
        logger.info("Websocket still connected ? " + str(sio.connected))
        if sio.connected:
            if Message_MQTT.pilevide():
                Message_MQTT.empile("C|RecuperoInfo")
            cmd = Message_MQTT.depile()
            logger.info("Envoi de la commande : " + str(cmd))
            sio.emit(
              "chiedo",
               {
                   "serialNumber": _MCZ_device_serial,
                   "macAddress": _MCZ_device_MAC,
                   "tipoChiamata": 1,
                   "richiesta": cmd,
               },
            )
        else:
            logger.warning("Websocket disconnected ! waiting 30 seconds")
            time.sleep(30)

    thread.start_new_thread(run, ())


Message_MQTT = PileFifo()
Message_WS = PileFifo()

_INTERVALLE = 1
_TEMPS_SESSION = 60

MQTT_MAESTRO = {}

logger.info('Lancement du deamon')
logger.info('Anthony L. 2019')
logger.info("Pipolaq's version")
logger.info('Niveau de LOG : DEBUG')

sio.connect(_MCZ_App_URL)

logger.info('Connection en cours au broker MQTT (IP:' + _MQTT_ip + ' PORT:' + str(_MQTT_port) + ')')
client = mqtt.Client()
if _MQTT_authentication:
    client.username_pw_set(username=_MQTT_user, password=_MQTT_pass)
client.on_connect = on_connect_mqtt
client.on_message = on_message_mqtt
client.connect(_MQTT_ip, _MQTT_port)
client.loop_start()
logger.info('Souscription au topic ' + str(_MQTT_TOPIC_SUB) + ' avec un Qos=1')
client.subscribe(_MQTT_TOPIC_SUB, qos=1)

thread.start_new_thread(receive, ())
