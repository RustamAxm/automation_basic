"""
В данном примере простой способ протестировать
значение которое возвращается из функции.
Обычно в conftest указываются такие вспомогательные функции.

"""

import numpy as np
from pytest import fixture

from automation_basics.test_demo.client import Client


@fixture
def get_testing_data():
    """
    Простая фикстура которая возвращает случайное значение

    :return: Возвращает float в диапазоне 0 - 1;
    """
    val = np.random.random()
    return val


@fixture(scope="session", params=[1, 2, 3])
def get_params(request):
    return request.param


@fixture(scope="session")
def get_client():
    cl = Client()
    return cl
