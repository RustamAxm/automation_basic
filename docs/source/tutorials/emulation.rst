Эмуляция устройств
==========================================

Виртуальный порт
-------------------
В работе с железками полезно промоделировать поведение на цифровом двойнике.
Конечно для этого требуется соглашение по интерфейсам.
Проделаем это на примере ком порта.

.. code-block::

    rustam@rustam-zenbook:~$ socat -d -d pty,raw,echo=0,link=/tmp/ttyV0 pty,raw,echo=0,link=/tmp/ttyV1
    2025/04/28 11:59:15 socat[7635] N PTY is /dev/pts/2
    2025/04/28 11:59:15 socat[7635] N PTY is /dev/pts/3
    2025/04/28 11:59:15 socat[7635] N starting data transfer loop with FDs [5,5] and [7,7]
    2025/04/28 11:59:19 socat[7635] N socat_signal(): handling signal 2
    2025/04/28 11:59:19 socat[7635] N exiting on signal 2
    2025/04/28 11:59:19 socat[7635] N socat_signal(): finishing signal 2
    2025/04/28 11:59:19 socat[7635] N exit(130)

Пример кода для взаимодействия

.. code-block::

    rustam@rustam-zenbook:~$ echo "test com" > /tmp/ttyV1

Другой терминал

.. code-block::

    rustam@rustam-zenbook:~$ cat < /tmp/ttyV0
    test com


Таким образом проверили виртуальный порт.

Пример кода на Python
------------------------

См. документацию в сабпроекте automation_basics/emulaton_demo


i2c пример для stub
---------------------

* `первый источник <https://stackoverflow.com/questions/63430327/how-can-i-emulate-an-i2c-device-on-linux>`_

* `второй  <https://shawn-maybush.com/building-a-dockerized-i%C2%B2c-development-platform-for-raspberry-pi/>`_


