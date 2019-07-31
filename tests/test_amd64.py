from archinfo.arch import Register, Endness, Arch
from nose.tools import assert_raises
from archinfo import ArchAMD64
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

try:
    import pyvex as _pyvex
except ImportError:
    _pyvex = None


def test_arch_amd64():
    endness = Endness.LE
    assert ArchAMD64(endness)

def test_capstone_x86_syntax():
    inst_1 = ArchAMD64(endness=Endness.LE)
    nose.tools.assert_is_none(inst_1.capstone_x86_syntax)

    inst_1.capstone_x86_syntax = 'intel'
    nose.tools.assert_equal(inst_1.capstone_x86_syntax, 'intel')
    inst_1.capstone_x86_syntax = 'at&t'
    nose.tools.assert_equal(inst_1.capstone_x86_syntax, 'at&t')
    # todo
    # inst_1.capstone_x86_syntax = 'intel'
    # nose.tools.assert_raises(ArchError, inst_1.capstone_x86_syntax)

def test_configure_capstone():
    pass

def test_keystone_x86_syntax():
    inst_1 = ArchAMD64(endness=Endness.LE)

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
    inst_1 = ArchAMD64(endness=Endness.LE)
    nose.tools.assert_is_not_none(inst_1._configure_keystone)
    # todo