from archinfo.arch import Register, Endness, Arch
from nose.tools import assert_raises, assert_equal, assert_is_none, assert_is_not_none
from archinfo import ArchX86
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

def test_archx86():
    endness = Endness.LE
    inst_1 = ArchX86(endness)
    # inst_1.__init__ = 'Iend_LE'
    nose.tools.assert_equal(inst_1.__init__, 'Iend_LE')


def test_capstone_x86_syntax():
    inst_1 = ArchX86()

    nose.tools.assert_is_none(inst_1.capstone_x86_syntax)

    inst_1.capstone_x86_syntax = 'intel'
    nose.tools.assert_equal(inst_1.capstone_x86_syntax, 'intel')
    inst_1.capstone_x86_syntax = 'at&t'
    nose.tools.assert_equal(inst_1.capstone_x86_syntax, 'at&t')

def test_configure_capstone():
    pass

def test_keystone_x86_syntax():
    inst_1 = ArchX86()

    nose.tools.assert_is_none(inst_1.keystone_x86_syntax)
    inst_1.keystone_x86_syntax = 'intel'
    nose.tools.assert_equal(inst_1.keystone_x86_syntax, 'intel')
    inst_1.keystone_x86_syntax = 'at&t'
    nose.tools.assert_equal(inst_1.keystone_x86_syntax, 'at&t')
    inst_1.keystone_x86_syntax = 'nasm'
    nose.tools.assert_equal(inst_1.keystone_x86_syntax, 'nasm')
    inst_1.keystone_x86_syntax = 'masm'
    nose.tools.assert_equal(inst_1.keystone_x86_syntax, 'masm')
    inst_1.keystone_x86_syntax = 'gas'
    nose.tools.assert_equal(inst_1.keystone_x86_syntax, 'gas')
    inst_1.keystone_x86_syntax = 'radix16'
    nose.tools.assert_equal(inst_1.keystone_x86_syntax, 'radix16')

def test_configure_keystone():
    inst_1 = ArchX86(endness=Endness.LE)
    nose.tools.assert_is_not_none(inst_1._configure_keystone)
    # todo



