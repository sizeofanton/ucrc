from ucrc import crc8
from ucrc import crc8_gen_table
from ucrc import crc8_fast
import pytest


def test_crc8_type_error():
    with pytest.raises(TypeError):
        crc8("Not a bytes")
    with pytest.raises(TypeError):
        crc8(bytes([0xFF,0x22,0x33]),in_ref="Yes")


def test_crc8_results():
    assert crc8(bytes([0xFF, 0xFE, 0xFA, 0xF0])) == 0x78
    assert crc8(bytes([0xFF, 0xFE, 0xFA, 0xF0]), poly=0x7) == 0xD9
    assert crc8(bytes([0xFF, 0xFE, 0xFA, 0xF0]), in_ref=True) == 0x2E
    assert crc8(bytes([0xFF, 0xFE, 0xFA, 0xF0]), out_ref=True) == 0x1E
    assert crc8(bytes([0xFF, 0xFE, 0xFA, 0xF0]), in_ref=True, out_ref=True) == 0x74


def test_crc8_table_results():
    table = crc8_gen_table()
    assert crc8_fast(bytes([0xFF, 0xFE, 0xFA, 0xF0]), table) == 0x78
    table = crc8_gen_table(0x7)
    assert crc8_fast(bytes([0xFF, 0xFE, 0xFA, 0xF0]), table) == 0xD9
    table = crc8_gen_table()
    assert crc8_fast(bytes([0xFF, 0xFE, 0xFA, 0xF0]), table, in_ref=True) == 0x2E
    assert crc8_fast(bytes([0xFF, 0xFE, 0xFA, 0xF0]), table, out_ref=True) == 0x1E
    assert crc8_fast(bytes([0xFF, 0xFE, 0xFA, 0xF0]), table, in_ref=True, out_ref=True) == 0x74

