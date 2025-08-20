Заметки по rpi
================

DTS
-----

Про `gpio expander <https://community.toradex.com/t/i2c-gpio-expander-pca9575-driver/23881>`_

.. code-block::

    // GPIO I2C PCA9548 Mux overlay v2

    /dts-v1/;
    /plugin/;

    /{
        compatible = "brcm,bcm2835";

        fragment@0 {
            target = <&i2c_arm>;
            __overlay__ {
                #address-cells = <1>;
                #size-cells = <0>;
                status = "okay";

                pca9548: mux@70 {
                    compatible = "nxp,pca9548";
                    reg = <0x70>;
                    #address-cells = <1>;
                    #size-cells = <0>;

                    i2c@0 {
                        #address-cells = <1>;
                        #size-cells = <0>;
                        reg = <0>;
                    };
                    i2c@1 {
                        #address-cells = <1>;
                        #size-cells = <0>;
                        reg = <1>;
                    };
                    i2c@2 {
                        #address-cells = <1>;
                        #size-cells = <0>;
                        reg = <2>;
                    };
                    i2c@3 {
                        #address-cells = <1>;
                        #size-cells = <0>;
                        reg = <3>;

                        pca9548a: mux@71 {
                            compatible = "nxp,pca9548";
                            reg = <0x71>;

                            };
                    };
                    i2c@4 {
                        #address-cells = <1>;
                        #size-cells = <0>;
                        reg = <4>;
                    };
                    i2c@5 {
                        #address-cells = <1>;
                        #size-cells = <0>;
                        reg = <5>;
                    };
                    i2c@6 {
                        #address-cells = <1>;
                        #size-cells = <0>;
                        reg = <6>;
                    };
                    i2c@7 {
                        #address-cells = <1>;
                        #size-cells = <0>;
                        reg = <7>;
                    };
                };
            };
        };
        fragment@1 {
            target-path = "/aliases";
            __overlay__ {
                i2c30 = &pca9548;
                i2c31 = &pca9548a;
            };
        };
    };

.. code-block::

    dtc -I dts -O dtb -o /dev/null mux_test.dts        # Проверка dts на ошибки
    dtc -@ -I dts -O dtb -o mux_test.dtbo mux_test.dts  # Компиляция dtbo
    sudo cp mux_test.dtbo /boot/firmware/overlays/     # Копирование файла к остальным оверлеям
    sudo dtoverlay mux_test                            # Загрузка нового оверлея в райнтайме
    sudo dtoverlay -l                                 # Список загруженных оверлеев в райнтайме. Там же можно посмотреть их ID.
    sudo dtoverlay -r 1                               # Выгрузка оверлея по его ID

в конфиге /boot/firmware/config.txt прописываем

.. code-block::

    dtparam=i2c_arm=on
    [all]
    dtoverlay=example


Сборка кастомного образа
------------------------------

Хорошая `статья <https://dev.to/brettops/customize-a-raspberry-pi-image-without-any-hardware-7a1>`_

Скрипт со скриптом в `репозитории <https://github.com/RustamAxm/sh_scripts/blob/main/qemu_rpi_edit/script_qemu_static.sh>`_