import ucrc.crc32_tables as TABLES
from ucrc import crc32_fast

def crc32_bzip2(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc32_fast(data=data, table=TABLES.TABLE_4C11DB7, init_val=0xFFFFFFFF, final_xor=0xFFFFFFFF)


def crc32_c(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc32_fast(data=data, table=TABLES.TABLE_1EDC6F41,
                      init_val=0xFFFFFFFF, final_xor=0xFFFFFFFF, in_ref=True, out_ref=True)


def crc32_d(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc32_fast(data=data, table=TABLES.TABLE_A83398B,
                      init_val=0xFFFFFFFF, final_xor=0xFFFFFFFF, in_ref=True, out_ref=True)


def crc32_mpeg2(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc32_fast(data=data, table=TABLES.TABLE_4C11DB7, init_val=0xFFFFFFFF)


def crc32_posix(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc32_fast(data=data, table=TABLES.TABLE_4C11DB7, final_xor=0xFFFFFFFF)


def crc32_q(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc32_fast(data=data, table=TABLES.TABLE_814141AB)


def crc32_jamcrc(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc32_fast(data=data, table=TABLES.TABLE_4C11DB7, init_val=0xFFFFFFFF, in_ref=True, out_ref=True)


def crc32_xfer(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc32_fast(data=data, table=TABLES.TABLE_AF)