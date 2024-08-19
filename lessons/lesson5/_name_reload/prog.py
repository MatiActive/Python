import mathmodule
import importlib
print(mathmodule.addNumber(10,20))
print("prog.py: " + __name__ )

importlib.reload(mathmodule)
importlib.reload(mathmodule)
importlib.reload(mathmodule)