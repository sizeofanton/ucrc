from ucrc.crc16 import crc16_fast
import ucrc.crc16_tables as TABLES


def crc16_ccit_zero(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_1021)


def crc16_arc(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_8005, in_ref=True, out_ref=True)


def crc16_aug_ccitt(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_1021, init_val=0x1D0F)


def crc16_buypass(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_8005)


def crc16_ccitt_false(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_1021, init_val=0xFFFF)


def crc16_cdma2000(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_C867, init_val=0xFFFF)


def crc16_dds_110(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_8005, init_val=0x800D)


def crc16_dect_r(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_589, final_xor=0x1)



def crc16_dect_x(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_589)


def crc16_dnp(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_3D65, final_xor=0xFFFF, in_ref=True, out_ref=True)


def crc16_en_13757(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_3D65, final_xor=0xFFFF)


def crc16_genibus(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_1021, init_val=0xFFFF, final_xor=0xFFFF)


def crc16_maxim(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_8005, final_xor=0xFFFF, in_ref=True, out_ref=True)


def crc16_mcrf4xx(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_1021, init_val=0xFFFF, in_ref=True, out_ref=True)


def crc16_riello(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_1021, init_val=0xB2AA, in_ref=True, out_ref=True)


def crc16_t10_dif(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_8BB7)


def crc16_teledisk(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_A097)


def crc16_tms37157(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_1021, init_val=0x89EC, in_ref=True, out_ref=True)


def crc16_usb(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_8005, init_val=0xFFFF, final_xor=0xFFFF, in_ref=True, out_ref=True)


def crc16_a(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_1021, init_val=0xC6C6, in_ref=True, out_ref=True)


def crc16_kermit(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_1021, in_ref=True, out_ref=True)


def crc16_modbus(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_8005, init_val=0xFFFF, in_ref=True, out_ref=True)


def crc16_x_25(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_1021, init_val=0xFFFF, final_xor=0xFFFF,  in_ref=True, out_ref=True)


def crc16_xmodem(data: bytes):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc16_fast(data=data, table=TABLES.TABLE_1021)
