import numpy as np


def python_type(val):
    to_check = str(type(val))
    if "int" in to_check:
        return int(val)
    elif "float" in to_check:
        return float(val)
    else:
        raise ValueError(f"error in convert data {val=}")


def struct_to_dict(s_struct: np._ArrayT):
    tmp = {}
    for key in s_struct.dtype.fields:
        tmp[key] = python_type(s_struct[key][0])

    return tmp
