import ucrc.crc64_tables as TABLES
from ucrc import crc64_fast


def crc64_ecma_182(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc64_fast(data=data, table=TABLES.TABLE_42F0E1EBA9EA3693)


def crc64_go_iso(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s " % (type(data),))

    return crc64_fast(data, TABLES.TABLE_000000000000001B, init_val=0xFFFFFFFFFFFFFFFF, final_xor=0xFFFFFFFFFFFFFFFF,
                      in_ref=True, out_ref=True)


def crc64_we(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s " % (type(data),))

    return crc64_fast(data, TABLES.TABLE_42F0E1EBA9EA3693, init_val=0xFFFFFFFFFFFFFFFF, final_xor=0xFFFFFFFFFFFFFFFF)


def crc64_xz(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s " % (type(data),))

    return crc64_fast(data, TABLES.TABLE_42F0E1EBA9EA3693, init_val=0xFFFFFFFFFFFFFFFF, final_xor=0xFFFFFFFFFFFFFFFF,
                      in_ref=True, out_ref=True)