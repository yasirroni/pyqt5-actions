# pyqt5-actions

Minimal working example of running `.py` file containing `matplotlib.use('Qt5Agg')` using  `python3-pyqt5`.

```python
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5.QtCore import QT_VERSION_STR
from PyQt5.Qt import PYQT_VERSION_STR
from sip import SIP_VERSION_STR

print(f'Python version: {sys.version}')
print(f'matplotlib version: {matplotlib.__version__}')
print(f'Qt version:{QT_VERSION_STR}')
print(f'SIP version:{SIP_VERSION_STR}')
print(f'PyQt version:{PYQT_VERSION_STR}')
```

## base

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

## matrix.python

```yml
name: CI-python-matrix

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.7", "3.8", "3.9", "3.10"]

    steps:
      - name: Clone this repository
        uses: actions/checkout@v3

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v3
        with:
          python-version: ${{ matrix.python-version }}
          cache: 'pip'

      - name: Install pyqt5
        run: |
          sudo apt-get install python3-setuptools python3-pyqt5
          python3 -m pip install matplotlib PyQt5

      - name: Run python script
        run: |
          python3 test_matplotlib_pyqt5.py
```
