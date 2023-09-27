from contoh4_10_ms173 import *
from tud_test_base import *
import pytest

# @pytest.fixture
# def radius():
#     radius = 5
#     return radius

@pytest.mark.parametrize("a,b", [(6, 3), (9,15)])
def test_besar_kecil(a,b):
    [x,y] = besar_kecil(a,b)
    assert x > y
    
def test_main():
    set_keyboard_input([8,10])
    main()
    output = get_display_output()

    assert output == [
        "Masukkan nombor integer yang pertama: ",
        "Masukkan nombor integer yang kedua: ",
        "Nombor 10 lebih besar daripada 8"
    ]
