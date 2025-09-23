def test_str_gen(get_class_gen_by_str):
    val = get_class_gen_by_str.f_first(2, 3)
    assert val == 123


def test_dynamically_gen(get_class_gen_by_dynamically):
    val = get_class_gen_by_dynamically.first(2, 3)
    assert val == 123
    val = get_class_gen_by_dynamically.second(5)
    assert val == 123
