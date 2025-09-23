import sys
import time
from enum import Enum

import ftd2xx
from loguru import logger


class PINNames(Enum):
    """
    Define the PINNames enum with relevant pins

    .. code-block::

        TXD = 0  # PIN_1 | D0
        RXD = 1  # PIN_5 | D1
        RTS = 2  # PIN_3 | D2
        CTS = 3  # PIN_11| D3
        DTR = 4  # PIN_2 | D4
        DSR = 5  # PIN_9 | D5
        DCD = 6  # PIN_10| D6
        RI = 7  # PIN_6 | D7

    """

    TXD = 0  # PIN_1 | D0
    RXD = 1  # PIN_5 | D1
    RTS = 2  # PIN_3 | D2
    CTS = 3  # PIN_11| D3
    DTR = 4  # PIN_2 | D4
    DSR = 5  # PIN_9 | D5
    DCD = 6  # PIN_10| D6
    RI = 7  # PIN_6 | D7


class FT232RLDevice:
    def __init__(self, device_index=0):
        """
        init ftdi device

        :param device_index:
        """
        try:
            self.dev = ftd2xx.open(device_index)
            logger.info("FT232RL device opened successfully.")
            self.previous_state = 0x00  # Initialize all pins to LOW
            self.dev.setBitMode(0x00, 0x01)  # Set to asynchronous bit-bang mode
            logger.info("Bit mode set to asynchronous bit-bang mode.")
        except ftd2xx.DeviceError as e:
            logger.info(f"Error opening FT232RL device: {e}")
            sys.exit(1)

    def write_pin(self, pin: PINNames, value: bool):
        """
        Write pin state

        :param pin:
        :param value:
        :return:
        """
        bit_position = pin.value
        if value:
            self.previous_state |= 1 << bit_position  # Set the bit
        else:
            self.previous_state &= ~(1 << bit_position)  # Clear the bit
        try:
            self.dev.write(bytes([self.previous_state]))
            logger.info(f"Set {pin.name} to {'HIGH' if value else 'LOW'}.")
        except ftd2xx.DeviceError as e:
            logger.info(f"Failed to write to device: {e}")

    def set_pins_as_output(self, pins):
        """
        Setup to output

        :param pins:
        :return:
        """
        bitmask = 0x00
        for pin in pins:
            bitmask |= 1 << pin.value
        try:
            self.dev.setBitMode(bitmask, 0x01)  # 0x01 for asynchronous bit-bang mode
            logger.info(f"Pins {[pin.name for pin in pins]} set as OUTPUT.")
        except ftd2xx.DeviceError as e:
            logger.info(f"Failed to set bit mode: {e}")
            sys.exit(1)

    def close(self):
        try:
            self.dev.close()
            logger.info("FT232RL device closed.")
        except ftd2xx.DeviceError as e:
            logger.info(f"Failed to close device: {e}")


def toggle_rxd_pin():
    """
    Instantiate the FT232RL device and set RXD as output

    :return:
    """
    device = FT232RLDevice()
    device.set_pins_as_output([PINNames.RXD])

    try:
        # Set RXD high
        for _ in range(5):
            device.write_pin(PINNames.RXD, True)
            logger.info("RXD is HIGH for 1 second.")

            # Wait for 1 second
            time.sleep(1)

            # Set RXD low
            device.write_pin(PINNames.RXD, False)
            logger.info("RXD is LOW.")
            time.sleep(1)
    finally:
        # Ensure the device is closed properly
        device.close()


if __name__ == "__main__":
    toggle_rxd_pin()
