import forbiddenfruit

def modify(*objects):

    def decorator(func):
        for obj in objects:
            forbiddenfruit.curse(obj, func.__name__,func)
        return func

    return decorator

def unsupported_type(op, obj1, obj2):
    return TypeError(f"unsupported operand type(s) for {op}: '{obj1.__class__.__name__}' and '{obj2.__class__.__name__}'")

@modify(str)
def __invert__(self):
    return ''.join(reversed(self))

@modify(list, tuple)
def __invert__(self):
    return self.__class__(reversed(self))

@modify(dict)
def __invert__(self):
    return {v:k for k,v in self.items()}

@modify(str)
def __sub__(self, other:str):
    if isinstance(other, str):
        return self.replace(other,'')
    else:
        raise unsupported_type('-', self, other)


@modify(list, tuple)
def __sub__(self, other):
    if isinstance(other, (list, tuple, set)):
        return self.__class__(elem for elem in self if elem not in other)
    else:
        raise unsupported_type('-', self, other)

@modify(dict)
def __add__(self, other:dict):
    if isinstance(other, dict):
        return {**self, **other}
    else:
        raise unsupported_type('+', self, other)


# Doesn't work :/
# @modify(str)
# def __setitem__(self, key, value):
#     temp = list(self)
#     temp[key] = str(value)
#     self = ''.join(temp)