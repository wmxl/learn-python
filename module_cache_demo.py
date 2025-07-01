#!/usr/bin/env python3
"""
Show Python's module cache and how to reload modules
"""
import sys
import importlib

print("=" * 50)
print("PYTHON MODULE CACHE DEMONSTRATION")
print("=" * 50)

print("\n1. Before any imports:")
print("-" * 30)
print("'tool' in sys.modules:", 'tool' in sys.modules)

print("\n2. First import of tool:")
print("-" * 30)
import tool
print("'tool' in sys.modules:", 'tool' in sys.modules)

print("\n3. Second import of tool:")
print("-" * 30)
import tool  # No output from tool.py!
print("'tool' in sys.modules:", 'tool' in sys.modules)

print("\n4. To force reload (advanced):")
print("-" * 30)
print("Reloading tool module...")
importlib.reload(tool)  # This WILL execute tool.py again!

print("\n5. Alternative: Manual cache removal")
print("-" * 30)
if 'myapp.utils.helper' in sys.modules:
    print("helper was in cache, removing...")
    del sys.modules['myapp.utils.helper']
    
print("Importing helper after cache removal:")
from myapp.utils import helper  # This will execute again!

print("\nKEY POINTS:")
print("-" * 30)
print("• sys.modules is Python's module cache")
print("• Once imported, modules stay in cache")
print("• importlib.reload() can force re-execution")
print("• This is why your tool.py only printed once!") 