# Disclaimer
This addon communicates with MCZ Maestro pellet stove API. It is provided as is with no implied warranty or liability. Please use with care.

# About the addon
Maestro technology uses a Websocket to communicate with the pellet stove. It is used by the MZC Maestro App and also by external thermostats.
https://www.mcz.it/en/maestro-technology/

This addon is simply embeds the code from https://github.com/Chibald/maestrogateway in a Home Assistant container.

# Usage
After installing the addon, the pellet state and commands (as described on Chibald's Github) should be available through MQTT.
Make sure the stove is reachable from the device on which HA is running. To do this, you'll typically need to use a wifi dongle on your HA device to connect to the stove AP or setup a second (client) wifi interface on your router.

# Credits
All credits go to Chibald and Anthony-55 who created the Python scripts that I'm embedding in this Home Assistant addon.
You can visit their Github repositories there:
https://github.com/Chibald/maestrogateway
https://github.com/Anthony-55/maestro

The script was initially created for "Jeedom", a home automation solution similar to HA. Discussions about this script can be found there (French):
https://community.jeedom.com/t/mcz-maestro-et-jeedom/6159
