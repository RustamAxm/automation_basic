Удобные фичи для linux
============================
Systemd
-------------
Для работы с сервисами демонами удобно пользоваться systemd
И так про это все написано куча инфы. Мне нравится пользоваться
`данным ресурсом по linux <https://www.baeldung.com/linux/create-remove-systemd-services>`_

Можно создать шаблон и скриптовые точки входа оформить как systemd сервисы.

deb пакеты
--------------
Тоже куча всякой инфы и так, но полезно самому проделать хоть раз.
`ссылка на пример  <https://github.com/RustamAxm/sh_scripts>`_

Установка dhcp сервера
-------------------------
Полезно когда нужно поднять отладочную сеть.
`Пример со скриптом <https://github.com/RustamAxm/sh_scripts>`_

Работа с ip
--------------

установка ip на интерфейс

.. code-block::

    ip a a 192.168.1.1/23 dev eth0

статистика по пакетам

.. code-block::

    ip -s -s  link show wlp0s20f3
    3: wlp0s20f3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DORMANT group default qlen 1000
    link/ether a0:80:69:87:64:2d brd ff:ff:ff:ff:ff:ff
        RX:  bytes packets errors dropped  missed   mcast
        1415441992 2010036      0     516       0       0
        RX errors:  length    crc   frame    fifo overrun
                         0      0       0       0       0
        TX:  bytes packets errors dropped carrier collsns
         238697972  680228      0      41       0       0
        TX errors: aborted   fifo  window heartbt transns
                         0      0       0       0      32


Прокинуть пакеты от одного ip `интерфейса в другой <https://github.com/RustamAxm/sh_scripts/blob/main/route_ip_to_ip/run_ip_to_ip.sh>`_

Namespace ip 
---------------

.. code-block::

        ip link

        sudo ip netns add ns1

        sudo ip link set eth1 netns ns1

        sudo ip netns exec ns1 ip link set eth1 up

        sudo ip link set eth0 up

        sudo ip addr add 10.0.0.1/24 dev eth0

        sudo ip netns exec ns1 ip addr add 10.0.0.2/24 dev eth1

        sudo ip netns exec ns1 ping 10.0.0.1

        
Утилита iperf
---------------

Утилита для работы с сетевым трафиком.

Есть несколько версий iperf3 - стандартный кейс, iperf2 - больше фич для udp

Много инструкций в сети, но упомяну что для udp мультикаст нужно открыть разрешение пакетов

.. code-block::

    ip route add 224.0.0.0/4 dev eth0
