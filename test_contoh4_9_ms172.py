from contoh4_9_ms172 import *
from tud_test_base import *
import pytest

@pytest.mark.parametrize("a,b", [(4,16), (5, 25), (6,36)])
def test_kuasadua(a,b):
    x = kuasadua(a)
    assert x == b
    
def test_main():
    set_keyboard_input([8])
    main()
    output = get_display_output()

    assert output == [
        "Masukkan satu nombor integer: ",
        "Kuasa dua bagi 8 ialah 64",
    ]