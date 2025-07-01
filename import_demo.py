#!/usr/bin/env python3
"""
Demonstration of Python's "import once" behavior
"""

print("=" * 50)
print("PYTHON IMPORT BEHAVIOR DEMONSTRATION")
print("=" * 50)

print("\n1. First import of tool:")
print("-" * 30)
import tool

print("\n2. Second import of tool:")
print("-" * 30)
import tool  # This will NOT print again!

print("\n3. Third import with different syntax:")
print("-" * 30)
from tool import *  # Still won't print!

print("\n4. Fourth import:")
print("-" * 30)
import tool as my_tool  # Still won't print!

print("\n5. Now let's import from myapp.utils:")
print("-" * 30)
from myapp.utils import helper  # This WILL print (first time for helper)

print("\n6. Import helper again:")
print("-" * 30)
from myapp.utils import helper  # This will NOT print again!

print("\nEXPLANATION:")
print("-" * 30)
print("• Python loads and executes each module only ONCE")
print("• After first import, the module is cached in sys.modules")
print("• Subsequent imports just return the cached module")
print("• That's why tool.py only printed once!") 