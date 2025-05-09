Docker
===================================

В данной части более общая и обрывистая информация, потому что и так хорошая документация.


Установка docker
-------------------
Удобный способ поставить `через скрипт <https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script>`_

И `пример доступа к приложению без sudo <https://docs.docker.com/engine/install/linux-postinstall/>`_

Репозиторий с примерами докерфайлов и скриптов bash `ссылка <https://github.com/RustamAxm/sh_scripts>`_


Работа с устройствами
-----------------------
Самый простой способ взаимодействия прокинуть железку с привилегией

.. code-block::

    docker run ...  --privileged -v /dev/bus/usb:/dev/bus/usb ...

В случае socketcan достаточно поместить контейнер в хостовую сеть

.. code-block::

    docker run ... --network host ...

Доступ уровня user
---------------------

Иногда доставляет неудобство, что примонтированная папка в docker при изменении остается с root правами.
Для этого можно использовать самодельного юзера.

`Пример создания образа <https://github.com/RustamAxm/sh_scripts/tree/main/docker-user>`_

Управление производительностью контейнера
--------------------------------------------

`работа по ссылке <https://github.com/RustamAxm/grpc-test-project/blob/main/research_docs/docker_performance.md>`_

