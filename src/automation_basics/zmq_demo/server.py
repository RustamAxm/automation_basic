import json
import time

import zmq
from loguru import logger


def server():
    """
    Простой паблишер сервер.
    Не обязательно так пользоваться,
    можно req-rep использовать, но это менее очевидный кейс.
    """
    port = 5555
    context = zmq.Context()
    socket_ = context.socket(zmq.PUB)
    socket_.bind(f"tcp://*:{port}")
    logger.info("start server send")
    time.sleep(1)
    for i in range(10):
        to_send = {"data": i, "data2": i + 1}
        logger.info(f"data received {to_send=}")
        socket_.send_json(json.dumps(to_send))
        time.sleep(1)
    socket_.close()
    logger.info("socket closed")


if __name__ == "__main__":
    server()
