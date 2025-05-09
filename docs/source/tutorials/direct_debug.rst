Прямое управление данными на чипе
====================================

OpenOCD
---------
Первый пример с прямым управлением значением регистров.
Пример кода для f103 с изменением периода мигания светодиода.
`Ссылка на репозиторий с примером <https://github.com/RustamAxm/arduino_based_projects/tree/main/openocd_stm_blink/OpenOCD_test>`_

Segger J-Link
----------------

Прикольный отладчик много всего умеет из коробки. Самый лучший remote control
`ссылка на артефакты <https://www.segger.com/downloads/jlink/>`_

`Пакет для управления отладчиком <https://pypi.org/project/pylink-square/>`_

Xilinx
--------------
Пример  DLC оригинала но есть куча китайских клонов
`ссылка <https://www.chipdip.ru/product/hw-usb-ii-g>`_

Удобно зашивать через `Vivado Lab <https://docs.amd.com/r/en-US/ug908-vivado-programming-debugging/Introduction>`_.
Есть поддержка скриптов из-под IDE

Можно пользоваться и `ftdi <https://docs.amd.com/r/2022.1-English/ug908-vivado-programming-debugging/Programming-FTDI-Devices-for-Vivado-Hardware-Manager-Support>`_

Пакет для использования `ссылка <https://pypi.org/project/pyftdi/>`_.
Предварительно нужно правильно поставить `драйвера <https://ftdichip.com/drivers/d2xx-drivers/>`_.
