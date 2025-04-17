"""
В данном примере простой способ протестировать
значение которое возвращается из функции.
Обычно в conftest указываются такие вспомогательные функции.

"""

from pytest import fixture
import numpy as np


@fixture
def get_testing_data():
    """
    Простая фикстура которая возвращает случайное значение

    :return: Возвращает float в диапазоне 0 - 1;
    """
    val = np.random.random()
    return val
