# Basic Calculator Mac App — Design Spec
**Date:** 2026-04-17

## Overview
A basic calculator Mac app built with Python 3 + tkinter. Single-file, no dependencies beyond the standard library. Runs with `python3 ~/calculator.py`.

## UI Layout
- Window size: ~300×400px, non-resizable, dark theme (macOS Calculator-inspired)
- Display: top section, right-aligned, large font, shows current input or result
- Button grid (5 rows × 4 columns):
  - Row 1: `AC`, `+/-`, `%`, `÷`
  - Row 2: `7`, `8`, `9`, `×`
  - Row 3: `4`, `5`, `6`, `−`
  - Row 4: `1`, `2`, `3`, `+`
  - Row 5: `0` (spans 2 cols), `.`, `=`
- Operator buttons: orange; function buttons (AC, +/-, %): light gray; digit buttons: dark gray

## Behavior
- `AC`: clears display and resets state
- `+/-`: toggles sign of current number
- `%`: divides current number by 100
- Operators (`+ − × ÷`): store current number and operator, wait for next input
- `=`: evaluates stored operation and displays result
- Chained operations: left-to-right (matches iOS Calculator behavior)
- Division by zero: displays "Error", resets on next input

## Architecture
- Single file: `~/calculator.py`
- `Calculator` class: holds state (current value, stored value, pending operator, new-input flag)
- `build_ui()`: constructs the tkinter window and button grid
- No external dependencies

## Success Criteria
- Launches as a native window on macOS
- All basic operations work correctly
- Handles edge cases: division by zero, chained operations, decimal input
