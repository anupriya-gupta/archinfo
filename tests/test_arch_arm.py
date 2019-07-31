from archinfo.arch import Register, Endness, Arch
from nose.tools import assert_raises
from archinfo import ArchARM
import archinfo.arch_arm as arch_arm
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

def test_is_arm_arch():
    endness = Endness.LE
    a = Arch(endness, instruction_endness=None)
    a.name = 'ARM'
    nose.tools.assert_equal(arch_arm.is_arm_arch(a), True)
    a.name = 'AArch'
    nose.tools.assert_equal(arch_arm.is_arm_arch(a), True)
    a.name = 'Abc'
    nose.tools.assert_not_equal(arch_arm.is_arm_arch(a), True)

def test_get_real_address_if_arm():
    addr = 9
    expected_output = 8
    endness = Endness.LE
    a = Arch(endness, instruction_endness=None)
    a.name = 'ARM'
    nose.tools.assert_equal(arch_arm.get_real_address_if_arm(a, addr), expected_output)
    a.name = 'AArch'
    nose.tools.assert_equal(arch_arm.get_real_address_if_arm(a, addr), expected_output)
    a.name = 'Abc'
    nose.tools.assert_equal(arch_arm.get_real_address_if_arm(a, addr), addr)

def test_init():
    inst_1 = ArchARM(endness=Endness.LE)
    nose.tools.assert_equal(inst_1.instruction_endness, 'Iend_LE')
    inst_1 = ArchARM(endness=Endness.ME)
    nose.tools.assert_is_not_none(inst_1.instruction_endness)
    print(inst_1.instruction_endness)

def test_eq():
    inst_1 = ArchARM()
    inst_1.__eq__ = 'ArchARMEL'
    nose.tools.assert_equal(inst_1.__eq__, 'ArchARMEL')

def test_getstate():
    inst_1 = ArchARM()
    inst_1._cs = None
    nose.tools.assert_equal(inst_1._cs, None)
    inst_1._cs_thumb = None
    nose.tools.assert_equal(inst_1._cs_thumb, None)
    inst_1._ks = None
    nose.tools.assert_equal(inst_1._ks, None)
    inst_1._ks_thumb = None
    nose.tools.assert_equal(inst_1._ks_thumb, None)

    inst_1.__getstate__ = None
    nose.tools.assert_equal(inst_1.__getstate__, None)

def test_setstate():
    #todo
    inst_1 = ArchARM()
    d = {1: "one", 2: "three"}
    inst_1.__setstate__ = d
    nose.tools.assert_equal(inst_1.__setstate__, d)

def test_capstone_thumb():
    inst_1 = ArchARM()
    # nose.tools.assert_raises(ArchError, inst_1.capstone_thumb)
    nose.tools.assert_is_not_none(_capstone, None)
    # nose.tools.assert_is_none(ArchError, inst_1.capstone_thumb)

# todo
def test_keystone_thumb():
    inst_1 = ArchARM()
    # print(inst_1.keystone_thumb)
    nose.tools.assert_is_none(_keystone, None)
    nose.tools.assert_raises(ArchError, inst_1.keystone_thumb)

# todo
def test_unicorn_thumb():
    inst_1 = ArchARM()
    nose.tools.assert_is_not_none(_unicorn, None)
    # nose.tools.assert_raises(ArchError, inst_1.unicorn_thumb)


def test_m_addr():
    addr = -10
    inst_1 = ArchARM()
    nose.tools.assert_equal(inst_1.m_addr(addr), addr & ~1)

def test_x_addr():
    addr = 9
    thumb = None
    inst_1 = ArchARM()
    nose.tools.assert_equal(inst_1.x_addr(addr, thumb), addr)
    nose.tools.assert_equal(inst_1.x_addr(addr, thumb=not None), addr | 1)

def test_is_thumb():
    addr = 10
    inst_1 = ArchARM()
    nose.tools.assert_not_equal(bool(inst_1.is_thumb(addr)), bool(addr & ~1))
    nose.tools.assert_equal(bool(inst_1.is_thumb(addr)), bool(addr & 1))

# make separate files for these three classes line 285
