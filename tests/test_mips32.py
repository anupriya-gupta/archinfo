from archinfo.arch import Register, Endness, Arch
from nose.tools import assert_raises
from archinfo import ArchARM
from archinfo.archerror import ArchError
import nose.tools
try:
    import capstone as _capstone
except ImportError:
    _capstone = None

try:
    import keystone as _keystone
except ImportError:
    _keystone = None

try:
    import unicorn as _unicorn
except ImportError:
    _unicorn = None

