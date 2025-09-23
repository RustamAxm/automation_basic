import pytest


def test_get_a0(get_api):
    """
    simple test idea
    """
    dev = get_api
    vals = dev.get_a0()
    assert vals.get("header") == 10
    assert vals.get("cmd") == 0
    assert vals.get("payload") == 23
    assert vals.get("err") == 0


def test_get_a1(get_api):
    """
    test demo for raises
    """
    dev = get_api
    with pytest.raises(Exception) as e_info:
        dev.get_a1()

    assert e_info.type is ValueError
    assert "error in device command=1" in f"{e_info.value}"
