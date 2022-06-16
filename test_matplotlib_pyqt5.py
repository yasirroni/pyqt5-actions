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
