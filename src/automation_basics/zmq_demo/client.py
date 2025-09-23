import json

import zmq
from loguru import logger


def client():
    """
    Простой клиент для приема широковещательных сообщений от сервера.
    С примером управления потоком через входящие сообщения.
    """
    config = {"ip": "localhost", "port": 5555}
    context = zmq.Context()
    addr = f"tcp://{config['ip']}:{config['port']}"
    logger.debug(f"{addr}")
    socket = context.socket(zmq.SUB)
    socket.setsockopt(zmq.SUBSCRIBE, b"")
    socket.connect(addr)

    for _ in range(10):
        tmp_dict_ = json.loads(socket.recv_json())
        logger.info(f"{tmp_dict_=}")
        if tmp_dict_["data"] == 1:
            logger.debug("action1")
        if tmp_dict_["data2"] == 2:
            logger.debug("action2")

    socket.disconnect(addr)


if __name__ == "__main__":
    client()
