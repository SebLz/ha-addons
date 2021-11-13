#!/usr/bin/env bashio

# Generate config file
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
_VERSION = '1.03'
" > /maestro/_config_.py

# Launch maestro gateway
python3 /maestro/maestro.py
