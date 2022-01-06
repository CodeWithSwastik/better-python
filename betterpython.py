import forbiddenfruit


def modify(*objects):
    def decorator(func):
        for obj in objects:
            if isinstance(func, property):
                forbiddenfruit.curse(obj, func.fget.__name__, func)
            elif isinstance(func, (staticmethod, classmethod)):
                forbiddenfruit.curse(obj, func.__func__.__name__, func)
            elif callable(obj):
                forbiddenfruit.curse(obj, func.__name__, func)
            else:
                raise TypeError(f"Object must be either a function, staticmethod, classmethod or property. Encountered {type(obj)} instead.")
        return func

    return decorator


def delete(obj, attribute):
    forbiddenfruit.reverse(obj, attribute)


### Default Modifications


@modify(str)
def __invert__(self):
    return "".join(reversed(self))


@modify(list, tuple)
def __invert__(self):
    return self.__class__(reversed(self))


@modify(dict)
def __invert__(self):
    return {v: k for k, v in self.items()}


@modify(str)
def __sub__(self, other: str):
    if isinstance(other, str):
        return self.replace(other, "")
    else:
        raise unsupported_type("-", self, other)


@modify(list, tuple)
def __sub__(self, other):
    if isinstance(other, (list, tuple, set)):
        return self.__class__(elem for elem in self if elem not in other)
    else:
        raise unsupported_type("-", self, other)


@modify(dict)
def __add__(self, other: dict):
    if isinstance(other, dict):
        return {**self, **other}
    else:
        raise unsupported_type("+", self, other)


# Doesn't work :/
# @modify(str)
# def __setitem__(self, key, value):
#     temp = list(self)
#     temp[key] = str(value)
#     self = ''.join(temp)


def unsupported_type(op, obj1, obj2):
    return TypeError(
        f"unsupported operand type(s) for {op}: '{obj1.__class__.__name__}' and '{obj2.__class__.__name__}'"
    )
