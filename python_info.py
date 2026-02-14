

import sys

# The actual path to the running interpreter
print(f"Executable: {sys.executable}")

# The root directory of the active environment
print(f"Prefix: {sys.prefix}")

# Check if you are in a virtual environment
if sys.prefix != sys.base_prefix:
    print("Status: Virtual Environment is ACTIVE")
else:
    print("Status: Using Global System Python")