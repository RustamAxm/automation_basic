import ast
import inspect

from loguru import logger


class Template:
    def __init__(self):
        pass

    def _private(self):
        pass

    def once(self, val1, val2) -> int:
        logger.debug(f"{val1}, {val2}")
        return 1

    def second(self):
        pass


class Template2:
    def __init__(self):
        pass

    def _private(self):
        pass

    def once_new(self, val1: int, val2: float, val3: str) -> int:
        logger.debug(f"{val1}, {val2}")
        return 1


class MyClass:
    def __init__(self):
        pass

    def get(self):
        return 12


def contains_explicit_return(f):
    return any(isinstance(node, ast.Return) for node in ast.walk(ast.parse(inspect.getsource(f))))


def get_method(ret_vals, args_vals):
    if ret_vals is inspect._empty:

        def set_method(self, *args, **kwargs):
            logger.debug(f"Set added class {args}, {kwargs}")
            return None

        sig = inspect.signature(set_method)
        sig = sig.replace(parameters=tuple(args_vals)[1:])
        set_method.__signature__ = sig
        return set_method
    else:

        def get_method(self, *args, **kwargs):
            logger.debug(f"Get added class {args}, {kwargs}")
            ret = self.get()
            return ret

        sig = inspect.signature(get_method)
        sig = sig.replace(parameters=tuple(args_vals)[1:])
        get_method.__signature__ = sig
        return get_method


def create_methods_from_rhs(cls, rhs):
    for name, method_ in rhs.__dict__.items():
        if callable(method_) and not name.startswith("_"):
            args_vals = inspect.signature(method_).parameters.values()
            logger.trace(f"{args_vals=}")
            ret_vals = inspect.signature(method_).return_annotation
            logger.trace(f"{ret_vals}")
            method_new = get_method(ret_vals, args_vals)
            method_new.__doc__ = method_.__doc__
            method_new.__qualname__ = method_.__qualname__
            setattr(cls, f"{name}", method_new)
            logger.trace(f"{name=}, {method_=}")


def create_methods_from_rhs_for_instance(obj, rhs):
    for name, method_ in rhs.__dict__.items():
        if callable(method_) and not name.startswith("_"):
            args_vals = inspect.signature(method_).parameters.values()
            logger.trace(f"{args_vals=}")
            ret_vals = inspect.signature(method_).return_annotation
            logger.trace(f"{ret_vals}")
            method_new = get_method(ret_vals, args_vals)
            method_new.__doc__ = method_.__doc__
            method_new.__qualname__ = method_.__qualname__
            setattr(obj, f"{name}", method_new.__get__(obj, obj.__class__))
            logger.debug(f"{name=}, {method_=}")


if __name__ == "__main__":
    create_methods_from_rhs(MyClass, Template)
    dev = MyClass()
    logger.debug(dev.once(12, val1=1))
    logger.debug(dev.second(13))
    logger.debug(MyClass.__dict__.items())
    logger.debug(dev.__class__.__dict__.items())

    logger.debug("_____________")
    logger.debug(inspect.signature(MyClass.once).parameters.values())
    logger.debug(type(list(inspect.signature(MyClass.once).parameters.values())[0]))
    logger.debug(inspect.signature(MyClass.second).parameters.values())
    logger.debug("______________")
    create_methods_from_rhs_for_instance(dev, Template2)
    logger.debug(dev.__class__.__dict__.items())
    logger.debug(dev.__dict__.items())
    logger.debug(dev.once_new(13))
    logger.debug(dev.once(12, val1=1))
    logger.debug(dev.second(13))
