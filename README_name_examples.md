# Python `__name__` Examples

This directory contains examples to demonstrate how Python's `__name__` variable works in different scenarios.

## File Structure

```
learn-python/
├── main.py                 # Simple import example
├── tool.py                 # Module to be imported
├── package_demo.py         # Package import example
├── run_examples.py         # Comprehensive demonstration
├── myapp/                  # Example package
│   ├── __init__.py
│   └── utils/
│       ├── __init__.py
│       └── helper.py
```

## How to Run the Examples

### 1. Comprehensive Demo
```bash
python run_examples.py
```
This shows all cases in one run with clear explanations.

### 2. Normal Case (Simple Import)
```bash
python main.py
```
**Expected Output:**
```
tool.py:  tool
main.py:  __main__
```

### 3. Package Case
```bash
python package_demo.py
```
**Expected Output:**
```
helper.py:  myapp.utils.helper
package_demo.py:  __main__
```

### 4. Exception Case (Run Modules Directly)

**Run tool.py directly:**
```bash
python tool.py
```
**Expected Output:**
```
tool.py:  __main__
```

**Run helper.py directly:**
```bash
python myapp/utils/helper.py
```
**Expected Output:**
```
helper.py:  __main__
```

## Key Takeaways

| File | How It's Used | `__name__` Value |
|------|---------------|------------------|
| `main.py` | Run directly | `'__main__'` |
| `tool.py` | Imported | `'tool'` |
| `helper.py` | Imported from package | `'myapp.utils.helper'` |
| `helper.py` | Run directly | `'__main__'` |

## The Rule

- **When imported**: `__name__` = the module's name (possibly with package path)
- **When run directly**: `__name__` = `'__main__'` (always)

This is why you often see:
```python
if __name__ == '__main__':
    # This code only runs when the file is executed directly
    # Not when it's imported
``` 