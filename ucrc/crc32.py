from ctypes import c_uint32
from ctypes import c_ubyte
from ucrc.utils import bytes_to_int, ref


def crc32(data: bytes, poly=0x4C11DB7, init_val=0, final_xor=0, in_ref=False, out_ref=False):
    """
    Function for calculating CRC32
    :param data: Input data as bytes
    :param poly: Generating polynomial
    :param init_val: CRC initial value
    :param final_xor: Value that will be XORed to result crc
    :param in_ref: Flag to reflect input
    :param out_ref: Flag to reflect output
    :return: CRC as unsigned int32 value
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

    crc = c_uint32(0) if init_val == 0 else c_uint32(init_val)
    if in_ref:
        data = ref(data)
    for b in data:
        crc.value ^= c_uint32(b << 24).value
        for _ in range(8):
            if crc.value & 0x80000000 != 0:
                crc.value = crc.value << 1 ^ poly
            else:
                crc.value = crc.value << 1
    if out_ref:
        crc_bytes = bytes(crc)
        crc_bytes = ref(crc_bytes)
        return c_uint32(bytes_to_int(crc_bytes)).value ^ final_xor
    else:
        return crc.value ^ final_xor


def crc32_fast(data: bytes, table: list, init_val=0, final_xor=0, in_ref=False, out_ref=False):
    """
    Function to calculating CRC16 with values from pre-calculated table
    :param data: Input data as bytes
    :param table: Pre-calculated table for polynomial used
    :param init_val: CRC initial value
    :param final_xor: Value that will be XORed to result crc
    :param in_ref: Flag to reflect input
    :param out_ref: Flag to reflect output
    :return: CRC as unsigned int32 value
    """
    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))
    if not isinstance(table, list):
        raise TypeError("Expected list, got %s" % (type(table),))
    if not isinstance(init_val, int):
        raise TypeError("Expected int, got %s" % (type(init_val),))
    if not isinstance(final_xor, int):
        raise TypeError("Expected int, got %s" % (type(final_xor),))
    if not isinstance(in_ref, bool):
        raise TypeError("Expected bool, got %s" % (type(in_ref),))
    if not isinstance(out_ref, bool):
        raise TypeError("Expected bool, got %s" % (type(out_ref),))
    crc = c_uint32(0) if init_val == 0 else c_uint32(init_val)
    if in_ref:
        data = ref(data)
    for b in data:
        p = c_ubyte((crc.value ^ (b << 24)) >> 24)
        crc.value = (crc.value << 8) ^ table[p.value]
    if out_ref:
        crc_bytes = bytes(crc)
        crc_bytes = ref(crc_bytes)
        return c_uint32(bytes_to_int(crc_bytes)).value ^ final_xor
    else:
        return crc.value ^ final_xor


def crc32_gen_table(poly=0x4C11DB7):
    """
    Function to generate table for generation polynomial
    :param poly: Generation polynomial
    :return: Table as list
    """
    if not isinstance(poly, int):
        raise TypeError("Expected int, got %s" % (type(poly),))
    table = [0]*256
    for d in range(256):
        curr_byte = c_uint32(d << 24)
        for _ in range(8):
            if curr_byte.value & 0x80000000 != 0:
                curr_byte.value <<= 1
                curr_byte.value ^= poly
            else:
                curr_byte.value <<= 1
        table[d] = curr_byte.value
    return table


