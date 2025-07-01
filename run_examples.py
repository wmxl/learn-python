#!/usr/bin/env python3
"""
Demonstration of Python __name__ behavior in different scenarios
"""

print("=" * 60)
print("PYTHON __name__ DEMONSTRATION")
print("=" * 60)

print("\n1. NORMAL CASE: Importing a file")
print("-" * 40)
print("Running: import tool")
import tool
print("Current script __name__:", __name__)

print("\n2. PACKAGE CASE: Importing from package")
print("-" * 40)
print("Running: from myapp.utils import helper")
print("(Notice: tool.py won't print again - Python only executes modules once!)")
from myapp.utils import helper
print("Current script __name__:", __name__)

print("\n3. SUMMARY:")
print("-" * 40)
print("• tool.py (imported): __name__ = 'tool'")
print("• helper.py (imported from package): __name__ = 'myapp.utils.helper'")
print("• This script (run directly): __name__ = '__main__'")

print("\n4. TO TEST THE EXCEPTION CASE:")
print("-" * 40)
print("Run these commands in your terminal:")
print("  python tool.py              # __name__ will be '__main__'")
print("  python myapp/utils/helper.py # __name__ will be '__main__'")
print("  python -m myapp.utils.helper # __name__ will be '__main__'")

print("\n" + "=" * 60) 