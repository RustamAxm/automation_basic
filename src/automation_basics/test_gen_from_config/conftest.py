import pytest
import yaml
from loguru import logger


class DemoDec:
    def __init__(self, commands):
        self.config = commands
        for item in self.config["device_cmds"]:
            self.create_method(item)

    def close(self):
        print("CLOSE")

    def create_method(self, cmd):
        """Create method based on command configuration."""

        def tmp_():
            logger.info(f"{cmd['name']}")
            return f"get_{cmd['name']}"

        tmp_.__doc__ = cmd["info"]
        setattr(self, f"get_{cmd['name']}", tmp_)


def pytest_addoption(parser):
    parser.addoption("--config", default="")


@pytest.fixture(scope="session")
def get_fct_config(request):
    return request.config.getoption("--config")


@pytest.fixture(scope="session")
def get_device(get_fct_config):
    with open(get_fct_config) as file:
        commands = yaml.safe_load(file)
    demo_dec = DemoDec(commands)
    yield demo_dec
    demo_dec.close()


def get_functions_names(request):
    fct_config = request.config.getoption("--config")

    with open(fct_config) as file:
        commands = yaml.safe_load(file)

    to_ret = []
    for cmd in commands["device_cmds"]:
        to_ret.append(f"get_{cmd['name']}")
    return to_ret


def pytest_configure(config):
    fct_config = config.getoption("--config")
    with open(fct_config) as f:
        commands = yaml.safe_load(f)

    to_ret = []
    for cmd in commands["device_cmds"]:
        to_ret.append(f"get_{cmd['name']}")

    config.func_names = to_ret


def pytest_generate_tests(metafunc):
    func_names = metafunc.config.func_names
    metafunc.fixturenames.append("_func_name")
    metafunc.parametrize(["_func_name"], [[i] for i in func_names], ids=func_names, scope="class")
