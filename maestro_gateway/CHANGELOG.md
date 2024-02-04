# Changelog

## 2.8

- Implement GPT-4 translations for the cloud script (addressing https://github.com/SebLz/ha-addons/issues/55). Locale can be set using the Cloud_Locale option. Currently supported: nl, fr, en, de, es, it.

## 2.7

- Ensures that the client automatically tries to resubscribe to the MQTT topic whenever it reconnects after an unexpected disconnection (addressing https://github.com/SebLz/ha-addons/issues/53)
- Update HA dependencies

## 2.6.1

- Update all python packages and alpine version to solve build issues with new version of HA

## 2.6

- Add a parameter _REFRESH_INTERVAL defining how often the local API is queried for updates

## 2.5

- Update python packages to fix connection errors (cf. https://github.com/pipolaq/maestro/issues/5 & https://github.com/SebLz/ha-addons/issues/37)

## 2.4

- Cloud script: Code improvement + check if connection is still alive, thanks @SkyPhilHome (https://github.com/pipolaq/maestro/pull/4)

## 2.3

- Add missing state variables in cloud script
- !!! BREAKING CHANGE !!! : remove all accents in state variables in cloud script => please adapt your template sensors/switches accordingly

## 2.2

- Add fan2 & fan3 in cloud script (thanks @elzinc85)

## 2.1

- Update default config so that it works with the cloud script
- Update Doc to show example usage of commands with the cloud script

## 2.0

- Add option for connecting to the stove via MCZ cloud

## 1.1

- First working build

## 1.0

- Initial release
