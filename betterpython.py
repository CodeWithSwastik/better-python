import forbiddenfruit

def modify(*objects):

    def decorator(func):
        for obj in objects:
            forbiddenfruit.curse(obj, func.__name__,func)
        return func

    return decorator

@modify(str, list, tuple)
def __invert__(self):
    return self[::-1]

@modify(dict)
def __invert__(self):
    return {v:k for k,v in self.items()}
