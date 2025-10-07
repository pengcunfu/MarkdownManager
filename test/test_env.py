import os
import sys

real_path = os.path.realpath(sys.executable)
real_path = os.path.join(os.path.dirname(real_path), "./Library/bin")
real_path = os.path.normpath(real_path)

os.environ["Path"] += ';' + real_path
print(os.getenv("Path"))
print(real_path)
