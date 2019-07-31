from archinfo.arch import Register, Endness, Arch
from nose.tools import assert_raises, assert_equal, assert_is_not_none, assert_is_none
from archinfo import ArchSoot
from archinfo.arch_soot import SootAddressDescriptor, SootMethodDescriptor
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


def test_address():
    __slots__ = ['method', 'block_idx', 'stmt_idx']
    method = SootMethodDescriptor("dummy", "dummy", tuple())
    # assert_equal(method, SootAddressDescriptor)
    inst_1 = SootAddressDescriptor(method, block_idx = 0, stmt_idx = 0)
    # inst_2 = SootMethodDescriptor(class_name, name, params, soot_method=None)
