"""
Тут фаил с тестами.

"""

def test_randon(get_testing_data):
    """
    простой assert проверяет значения

    :param get_testing_data:
    :return:
    """
    val = get_testing_data
    print(f"{val=}")
    assert 0.0 < val < 1.0


def test_randon_false(get_testing_data):
    """
    В данном случае иногда полезно проверить заведомо плохой результат
    так же стоит упомянуть что число тут будет другое, чтобы объект
    сохранился нужно прокинуть нужный параметр в фикстуру.

    :param get_testing_data:
    :return:
    """
    val = get_testing_data
    print(f"{val=}")
    assert not val > 1.0
