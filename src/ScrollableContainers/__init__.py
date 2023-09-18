for module in ('.Qt5', '.Qt6', '.Tk', '.Wx'):
    try:
        exec(f'from {module} import *')
    except ImportError:
        pass
del Qt5, Qt6, Tk, Wx
