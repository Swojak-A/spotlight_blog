from .base import *

is_production = True

if is_production == True:
    from .production import *

try:
    from .local import *
except:
    pass