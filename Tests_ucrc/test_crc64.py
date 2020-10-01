from ucrc import crc64
import pytest


def test_crc64_type_error():
    with pytest.raises(TypeError):
        crc64("Not a bytes")
    with pytest.raises(TypeError):
        crc64(bytes([0xFF, 0xFF, 0xFF, 0xFF]), in_ref="Yes")


def test_crc64_results():
    assert crc64(bytes([0xFF, 0xFF, 0xFF, 0xFF])) == 0x42F0E1EBA9EA3693
    assert crc64(bytes([0xFF, 0xFF, 0xFF, 0xFF]), poly=0x995DC9BBDF1939FA) == 0x181D305EAFEF0B02
    assert crc64(bytes([0xFF, 0xFF, 0xFF, 0xFF]), in_ref=True) == 0xD2F9D878539E5AD0
    assert crc64(bytes([0xFF, 0xFF, 0xFF, 0xFF]), out_ref=True) == 0x0B5A79CA1E1B9F4B
    assert crc64(bytes([0xFF, 0xFF, 0xFF, 0xFF]), in_ref=True, out_ref=True) == 0x0B5A79CA1E1B9F4B