import threading
import time

import zmq


def subscriber(topic_filter, name):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://127.0.0.1:5555")
    socket.setsockopt_string(zmq.SUBSCRIBE, topic_filter)
    print(f"{name} подписан на {topic_filter}")

    while True:
        message = socket.recv_string()
        print(f"{name} получил: {message}")
        time.sleep(0.1)


# Запуск нескольких подписчиков в отдельных потоках
threading.Thread(target=subscriber, args=("news", "Sub1"), daemon=True).start()
threading.Thread(target=subscriber, args=("tech", "Sub2"), daemon=True).start()

# Основной поток не завершается
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Остановка...")
