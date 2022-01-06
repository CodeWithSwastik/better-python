# better-python
Adds more functionality to Python and an easy to use wrapper for forbiddenfruit. 

```py
from betterpython import modify

@modify(str)
def remove(self, substr):
    return self.replace(substr, "")
    
print("This is a string".remove("i")) # Ths s a strng
```
