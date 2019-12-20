from ucrc.utils import *


def test_bytes_to_int():
    assert bytes_to_int([0xFF]) == 255
    assert bytes_to_int([0xFF,0xFF]) == 65535


def test_ref_bits():
    assert ref_bits(0x01) == 0x80
    assert ref_bits(0x02) == 0x40
    assert ref_bits(0x03) == 0xC0

