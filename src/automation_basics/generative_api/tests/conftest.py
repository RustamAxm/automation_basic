import yaml
from pytest import fixture

from automation_basics.generative_api.gen.out import Temp
from automation_basics.generative_api.tmp_class import TempGen


class Dev:
    def write(self, payload):
        pass

    def read(self, size):
        return b"{\x00\x00\x00"


@fixture(scope="session")
def get_class_gen_by_str():
    dev = Dev()
    v = Temp(dev)
    return v


@fixture(scope="session")
def get_class_gen_by_dynamically():
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

      - {name: second, 
         args: [
           {name: d, type: uint8, info: "some a for second"},
         ],       
         ret: [
           {name: e, type: uint32, info: "data cmd", size: 4},
         ]
        }
        """
    to_gen = yaml.safe_load(yaml_)
    dev = Dev()
    t = TempGen(dev, config=to_gen.get("interfaces"))
    return t
