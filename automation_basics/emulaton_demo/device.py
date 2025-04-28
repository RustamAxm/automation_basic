import serial
from loguru import logger

def device():
    """
    Эмулируем ответ устройства по ком порту

    """
    dev = serial.Serial('/tmp/ttyV1')
    while True:
        vals = dev.readline()
        logger.info(f'{vals=}')
        payload = 'from device\n'.encode('utf-8')
        logger.info(f'send from device {payload=}')
        dev.write(payload)

if __name__ == '__main__':
    device()
