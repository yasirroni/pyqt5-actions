# pyqt5-actions

Minimal working example of running `.py` file containing `matplotlib.use('Qt5Agg')` using  `python3-pyqt5`.

```python
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
from PyQt5 import QtCore, QtWidgets
```

## Base

```yml
name: CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Clone this repository
        uses: actions/checkout@v3
        
      - name: Install pyqt4 pyqt5
        run: |
          sudo apt-get install python3-setuptools python3-pyqt5
          python3 -m pip install matplotlib
      - name: Run python script
        run: |
          python3 test_matplotlib_pyqt5.py
```
