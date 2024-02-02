for module in ('.qt5', '.qt6', '.tk', '.wx'):
    try:
        exec(f'from {module} import *')
    except ImportError:
        pass
