from ctypes import c_uint64
from ctypes import c_ubyte
from ucrc.utils import bytes_to_int, ref


def crc64(data: bytes, poly = 0x42F0E1EBA9EA3693, init_val = 0, final_xor = 0, in_ref = False, out_ref = False):
    """
    Function for calculating CRC64
    :param data: Input data as bytes
    :param poly: Generating polynomial
    :param init_val: CRC initial value
    :param final_xor: Value that will be XORed to result crc
    :param in_ref: Flag to reflect input
    :param out_ref: Flag to reflect output
    :return: CRC as unsigned int64 value
    """

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))
    if not isinstance(poly, int):
        raise TypeError("Expected int, got %s" % (type(poly),))
    if not isinstance(init_val, int):
        raise TypeError("Expected int, got %s" % (type(init_val),))
    if not isinstance(final_xor, int):
        raise TypeError("Expected int, got %s" % (type(final_xor),))
    if not isinstance(in_ref, bool):
        raise TypeError("Expected bool, got %s" % (type(in_ref),))
    if not isinstance(out_ref, bool):
        raise TypeError("Expected bool, got %s" % (type(out_ref),))

    crc = c_uint64(0) if init_val == 0 else c_uint64(init_val)
    if in_ref:
        data = ref(data)
    for b in data:
        crc.value ^= c_uint64(b << 56).value
        for _ in range(8):
            if crc.value & 0x8000000000000000 != 0:
                crc.value = crc.value << 1 ^ poly
            else:
                crc.value = crc.value << 1

    if out_ref:
        crc_bytes = bytes(crc)
        crc_bytes = ref(crc_bytes)
        return c_uint64(bytes_to_int(crc_bytes)).value ^ final_xor
    else:
        return crc.value ^ final_xor
