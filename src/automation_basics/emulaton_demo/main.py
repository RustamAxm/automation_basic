import serial
from loguru import logger


def main():
    """
    Для создания ком порта можно воспользоваться скриптом

    .. code-block::

         uv run poe create-com

    """
    dev = serial.Serial("/tmp/ttyV0")
    payload = "to device\n".encode("utf-8")
    logger.info(f"send to device {payload=}")
    dev.write(payload)
    vals = dev.readline()
    logger.info(f"{vals=}")


if __name__ == "__main__":
    main()
