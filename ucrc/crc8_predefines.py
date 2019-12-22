from ucrc.crc8 import crc8_fast
import ucrc.crc8_tables as TABLES


def crc8_sae_j1850(data):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc8_fast(data=data, table=TABLES.TABLE_1D, init_val=0xFF, final_xor=0xFF)


def crc8_sae_j1850_zero(data):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc8_fast(data=data, table=TABLES.TABLE_1D)


def crc8_8h2f(data):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc8_fast(data=data, table=TABLES.TABLE_2F, init_val=0xFF, final_xor=0xFF)


def crc8_cdma2000(data):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc8_fast(data=data, table=TABLES.TABLE_9B, init_val=0xFF)


def crc8_darc(data):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc8_fast(data=data, table=TABLES.TABLE_39, in_ref=True, out_ref=True)


def crc8_dvb_s2(data):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc8_fast(data=data, table=TABLES.TABLE_D5)


def crc8_ebu(data):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc8_fast(data=data, table=TABLES.TABLE_1D, init_val=0xFF, in_ref=True, out_ref=True)


def crc8_icode(data):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc8_fast(data=data, table=TABLES.TABLE_1D, init_val=0xFD)


def crc8_itu(data):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc8_fast(data=data, table=TABLES.TABLE_7, final_xor=0x55)


def crc8_maxim(data):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc8_fast(data=data, table=TABLES.TABLE_31, in_ref=True, out_ref=True)


def crc8_rohc(data):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc8_fast(data=data, table=TABLES.TABLE_7, init_val=0xFF, in_ref=True, out_ref=True)


def crc8_wcdma(data):

    if not isinstance(data, bytes):
        raise TypeError("Expected bytes, got %s" % (type(data),))

    return crc8_fast(data=data, table=TABLES.TABLE_9B, in_ref=True, out_ref=True)



