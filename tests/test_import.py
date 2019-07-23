import archinfo

from archinfo.arch import Arch, Endness, Register

def test_endness(): 
    inst_endness = Endness() 
    assert inst_endness.LE == "Iend_LE"
    assert inst_endness.BE == "Iend_BE"
    assert inst_endness.ME == "Iend_ME"

def test_register():
    register = Register( name = 'MIPS', size = 8, vex_offset = 10, vex_name = 'xyz', subregisters = ['a', 'b'],
                         alias_names = ('r0'), general_purpose = True, floating_point = True,
                         vector = True, argument = True, persistent = True,
                         default_value = (True, 'global'), linux_entry_value = 'argv',
                         concretize_unique = True, concrete = True, artificial = True )
    assert register.name == 'MIPS'
    assert register.size == 8 
    assert register.vex_offset == 10
    assert register.vex_name == "xyz"
    assert register.subregisters == ['a', 'b']
    assert register.alias_names == ('r0')
    assert register.general_purpose == True
    assert register.floating_point == True
    assert register.vector == True
    assert register.argument == True
    assert register.persistent == True 
    assert register.default_value == (True, 'global')
    assert register.linux_entry_value == 'argv'
    assert register.concretize_unique == True
    assert register.concrete == True
    assert register.artificial == True

