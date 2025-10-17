import time

import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5555")

print("Publisher запущен на tcp://127.0.0.1:5555")

# Отправка сообщений с темами
topics = ["news", "sports", "tech", "weather"]

while True:
    for topic in topics:
        message = f"{topic}: Сегодня отличная погода!"
        socket.send_string(f"{topic} {message}")
        print(f"Отправлено: {topic} {message}")
        time.sleep(1)
