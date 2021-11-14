# Disclaimer
This addon communicates with MCZ Maestro pellet stove API. It is provided as is with no implied warranty or liability. Please use with caution.

# About the addon
Maestro technology uses a Websocket to communicate with the pellet stove. It is used by the [MCZ Maestro](https://www.mcz.it/en/maestro-technology/) App and also by external thermostats.
After installing the addon, the pellet [state and commands](https://github.com/Chibald/maestrogateway#payload-type-topic) should be available through MQTT.
This addon simply embeds the code from https://github.com/Chibald/maestrogateway in a Home Assistant container.
There are many areas of improvements, like support of [MQTT discovery](https://www.home-assistant.io/docs/mqtt/discovery/), better docs and type checking for options,... My time and expertise are limited but hopefully this is already helpful to some people and can be further improved by others :).

# Installation
You can install this addon after adding my repository url (https://github.com/SebLz/ha-addons) in your HA instance (you can follow [the official guide](https://www.home-assistant.io/common-tasks/os#installing-third-party-add-ons). Also, make sure the stove is reachable from the device on which HA is running. To do this, you'll typically need to use a wifi dongle on your HA device to connect to the stove AP or setup a second (client) wifi interface on your router.

# Configuration
Available options enable user to set up [Chibald' maestrogateway config](https://github.com/Chibald/maestrogateway#configuration)

# Usage
Examples of code you can use in you configuration.yaml:

Sensor to display stove state:
```
- platform: mqtt
    name: PoelePellets
    state_topic: Maestro/Stove_State
    value_template: >-
      {% set mapper = {
        '0' : 'Eteint',
        '1' : 'Controle du poele froid / chaud',
        '2' : 'Clean Froid',
        '3' : 'Load Froid',
        '4' : 'Start 1 Froid',
        '5' : 'Start 2 Froid',
        '6' : 'Clean Chaud',
        '7' : 'Load Chaud',
        '8' : 'Start 1 chaud',
        '9' : 'Start 2 chaud',
        '10' : 'Stabilisation',
        '11' : 'Puissance 1',
        '12' : 'Puissance 2',
        '13' : 'Puissance 3',
        '14' : 'Puissance 4',
        '15' : 'Puissance 5',
        '30' : 'Mode diagnostique',
        '31' : 'Marche',
        '40' : 'Extinction',
        '41' : 'Refroidissement en cours',
        '42' : 'Nettoyage basse p.',
        '43' : 'Nettoyage haute p.',
        '44' : 'Débloquage vis sans fin',
        '45' : 'AUTO ECO',
        '46' : 'Standby',
        '48' : 'Diagnostique',
        '49' : 'CHARG. VIS SANS FIN',
        '50' : 'Erreur A01 - Allumage raté',
        '51' : 'Erreur A02 - Pas de flamme',
        '52' : 'Erreur A03 - Surchauffe du réservoir',
        '53' : 'Erreur A04 - Température des fumées trop haute',
        '54' : 'Erreur A05 - Obstruction conduit - Vent',
        '55' : 'Erreur A06 - Mauvais tirage',
        '56' : 'Erreur A09 - Défaillance sonde de fumées',
        '57' : 'Erreur A11 - Défaillance motoréducteur',
        '58' : 'Erreur A13 - Température carte mère trop haute',
        '59' : 'Erreur A14 - Défaut Active',
        '60' : 'Erreur A18 - Température d eau trop haute',
        '61' : 'Erreur A19 - Défaut sonde température eau',
        '62' : 'Erreur A20 - Défaut sonde auxiliaire',
        '63' : 'Erreur A21 - Alarme pressostat',
        '64' : 'Erreur A22 - Défaut sonde ambiante',
        '65' : 'Erreur A23 - Défaut fermeture brasero',
        '66' : 'Erreur A12 - Panne controleur motoréducteur',
        '67' : 'Erreur A17 - Bourrage vis sans fin',
        '69' : 'Attente Alarmes securité' } %}
      {% set state = (value | string) %}
      {{ mapper[state] if state in mapper else 'Inconnu' }}
```

Switch (power on/off)
```
- platform: mqtt
  name: PoelePellets
  state_topic: "Maestro/Stove_State"
  value_template: >
    {% if value | int > 0 %}
    on
    {% else %}
    off
    {% endif %}
  state_on: "on"
  state_off: "off"
  command_topic: "Maestro/Command/Power"
  payload_on: 1
  payload_off: 0
```

# Credits
All credits go to Chibald and Anthony-55 who created the Python scripts that I'm embedding in this Home Assistant addon.
You can visit their Github repositories there:
- https://github.com/Chibald/maestrogateway
- https://github.com/Anthony-55/maestro

The script was initially created for "Jeedom", a home automation solution similar to HA. Discussions about this script can be found there (French):
- https://community.jeedom.com/t/mcz-maestro-et-jeedom/6159
