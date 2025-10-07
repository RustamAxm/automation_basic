import inspect
import ast
import inspect

class Template:
    def __init__(self):
        pass

    def _private(self):
        pass

    def once(self, val1, val2) -> int:
        print(f"{val1}, {val2}")
        return 1

    def second(self):
        pass

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
            print(f"Set added class {args}, {kwargs}")
            return None
        sig = inspect.signature(set_method)
        sig = sig.replace(parameters=tuple(args_vals))
        set_method.__signature__ = sig
        return set_method
    else:
        def get_method(self, *args, **kwargs):
            print(f"Get added class {args}, {kwargs}")
            ret = self.get()
            return ret
        sig = inspect.signature(get_method)
        sig = sig.replace(parameters=tuple(args_vals))
        get_method.__signature__ = sig
        return get_method

def create_methods_from_rhs(cls, rhs):
    for name, method_ in rhs.__dict__.items():
        if callable(method_) and not name.startswith("_"):
            args_vals =  inspect.signature(method_).parameters.values()
            print(f"{args_vals=}")
            ret_vals = inspect.signature(method_).return_annotation
            print(f"{ret_vals}")
            method_new = get_method(ret_vals, args_vals)
            setattr(cls, f'dynamic_{name}', method_new)
            print(f"{name=}, {method_=}")

if  __name__ == '__main__':
    create_methods_from_rhs(MyClass, Template)
    dev = MyClass()
    print(dev.dynamic_once(12, val1 = 1))
    print(dev.dynamic_second(13))
    print(MyClass.__dict__.items())

    print("_____________")
    print(inspect.signature(MyClass.dynamic_once).parameters.values())
    print(inspect.signature(MyClass.dynamic_second).parameters.values())
