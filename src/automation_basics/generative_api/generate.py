"""
Проект для демонстрации генерации api
"""
import yaml
from loguru import logger


def generate():
    """
    Удобно определить общие положения в каком нибудь ямлике.
    """
    yaml_ = """
interfaces:
  - {name: first, 
     args: [
       {name: a, type: uint8, info: "some a"},
       {name: b, type: uint32, info: "some b"},
     ],       
     ret: [
       {name: c, type: uint32, info: "data cmd", size: 4},
     ]
  }
    """
    to_gen = yaml.safe_load(yaml_)
    logger.info(f'{to_gen=}')
    """
    пример генерации класса str
    """
    ident4 = " " * 4
    ident8 = " " * 8
    out_str_ = (f'import numpy as np\n\n\n'
                f'class Temp:\n'
                f'{ident4}def __init__(self, dev):\n'
                f'{ident8}self.dev = dev\n\n')
    for item in to_gen.get('interfaces'):
        vals_ = ''
        for var in item.get('args'):
            vals_ += f'{var["name"]}, '
        out_str_ += f'{ident4}def f_{item["name"]}(self, {vals_}):\n'
        out_str_ += f'{ident8}payload = b\'\'\n'
        for var in item.get('args'):
            out_str_ += f'{ident8}payload += np.{var["type"]}({var["name"]}).tobytes()\n'

        for var in item.get('ret'):
            out_str_ += (f'{ident8}self.dev.write(payload)\n'
                         f'{ident8}ret = self.dev.read({var["size"]})\n'
                         f'{ident8}return np.frombuffer(ret, dtype=np.{var["type"]})\n\n')

    with open('gen/out.py', 'w') as file:
        file.write(out_str_)


if __name__ == '__main__':
    generate()