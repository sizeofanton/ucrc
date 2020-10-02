from ucrc import crc64
from ucrc import crc64_fast
from ucrc import crc64_gen_table
import pytest


def test_crc64_type_error():
    with pytest.raises(TypeError):
        crc64("Not a bytes")
    with pytest.raises(TypeError):
        crc64(bytes([0xFF, 0xFF, 0xFF, 0xFF]), in_ref="Yes")


def test_crc64_results():
    assert crc64(bytes([0xFF, 0xFF, 0xFF, 0xFF])) == 0xD2F9D878539E5AD0
    assert crc64(bytes([0xFF, 0xFF, 0xFF, 0xFF]), poly=0x995DC9BBDF1939FA) == 0x181D305EAFEF0B02
    assert crc64(bytes([0xFF, 0xFF, 0xFF, 0xFF]), in_ref=True) == 0xD2F9D878539E5AD0
    assert crc64(bytes([0xFF, 0xFF, 0xFF, 0xFF]), out_ref=True) == 0x0B5A79CA1E1B9F4B
    assert crc64(bytes([0xFF, 0xFF, 0xFF, 0xFF]), in_ref=True, out_ref=True) == 0x0B5A79CA1E1B9F4B


def test_crc64_table_results():
    table = crc64_gen_table()
    assert crc64_fast(bytes([0xFF, 0xFF, 0xFF, 0xFF]), table) == 0xD2F9D878539E5AD0
    assert crc64_fast(bytes([0xFF, 0xFF, 0xFF, 0xFF]), table, in_ref=True) == 0xD2F9D878539E5AD0
    assert crc64_fast(bytes([0xFF, 0xFF, 0xFF, 0xFF]), table, out_ref=True) == 0x0B5A79CA1E1B9F4B
    assert crc64_fast(bytes([0xFF, 0xFF, 0xFF, 0xFF]), table, in_ref=True, out_ref=True) == 0x0B5A79CA1E1B9F4B
    table = crc64_gen_table(0x995DC9BBDF1939FA)
    assert crc64_fast(bytes([0xFF, 0xFF, 0xFF, 0xFF]), table)
