#!/usr/bin/with-contenv bashio

# Generate config file for local connection plugin
echo "
_MQTT_ip = '$(bashio::config 'MQTT_ip')'
_MQTT_port = $(bashio::config 'MQTT_port')
_MQTT_authentication = $(bashio::config 'MQTT_authentication')
_MQTT_user = '$(bashio::config 'MQTT_user')'
_MQTT_pass = '$(bashio::config 'MQTT_pass')'
_MQTT_TOPIC_SUB = '$(bashio::config 'MQTT_TOPIC_SUB')'
_MQTT_TOPIC_PUB = '$(bashio::config 'MQTT_TOPIC_PUB')'
_MQTT_PAYLOAD_TYPE = '$(bashio::config 'MQTT_PAYLOAD_TYPE')'
_WS_RECONNECTS_BEFORE_ALERT = $(bashio::config 'WS_RECONNECTS_BEFORE_ALERT')
_REFRESH_INTERVAL = $(bashio::config 'REFRESH_INTERVAL')
_MCZip = '$(bashio::config 'MCZip')'
_MCZport = '$(bashio::config 'MCZport')'
_VERSION = '1.03'
" > /maestro/local/_config_.py

# Generate config file for cloud connection plugin
echo "
_MQTT_ip = '$(bashio::config 'MQTT_ip')'
_MQTT_port = $(bashio::config 'MQTT_port')
_MQTT_authentication = $(bashio::config 'MQTT_authentication')
_MQTT_user = '$(bashio::config 'MQTT_user')'
_MQTT_pass = '$(bashio::config 'MQTT_pass')'
_MQTT_TOPIC_SUB = '$(bashio::config 'MQTT_TOPIC_SUB')'
_MQTT_TOPIC_PUB = '$(bashio::config 'MQTT_TOPIC_PUB')'
_MQTT_PAYLOAD_TYPE = '$(bashio::config 'MQTT_PAYLOAD_TYPE')'
_WS_RECONNECTS_BEFORE_ALERT = $(bashio::config 'WS_RECONNECTS_BEFORE_ALERT')
_MCZip = '$(bashio::config 'MCZip')'
_MCZport = '$(bashio::config 'MCZport')'
_MCZ_device_serial = '$(bashio::config 'MCZ_device_serial')'
_MCZ_device_MAC = '$(bashio::config 'MCZ_device_MAC')'
_MCZ_App_URL = '$(bashio::config 'MCZ_App_URL')'
_VERSION = '1.5'
" > /maestro/cloud/_config_.py

# Make _data_.py point to the chosen translation
echo "
from translations.data_$(bashio::config 'Cloud_Locale') import RecuperoInfo as RecuperoInfo_translated
RecuperoInfo = RecuperoInfo_translated
" > /maestro/cloud/_data_.py

if bashio::config.true 'USE_MCZ_CLOUD'; then
    bashio::log.info "Launching maestro cloud connection plugin"
    python3 /maestro/cloud/maestro.py
else
    bashio::log.info "Launching maestro local connection plugin"
    python3 /maestro/local/maestro.py
fi
