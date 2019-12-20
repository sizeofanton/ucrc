from ucrc.crc8 import crc8_fast
import ucrc.crc8_tables as TABLES


def crc8_sae_j1850(data):
    init_val = 0xFF
    final_xor = 0xFF
    res = crc8_fast(data=data, table=TABLES.TABLE_1D, init_val=init_val, final_xor=final_xor)
    return res


def crc8_sae_j1850_zero(data):
    init_val = 0x0
    final_xor = 0x0
    res = crc8_fast(data=data, table=TABLES.TABLE_1D, init_val=init_val, final_xor=final_xor)
    return res


def crc8_8h2f(data):
    init_val = 0xFF
    final_xor = 0xFF
    res = crc8_fast(data=data, table=TABLES.TABLE_2F, init_val=init_val, final_xor=final_xor)
    return res


def crc8_cdma2000(data):
    init_val = 0xFF
    final_xor = 0x0
    res = crc8_fast(data=data, table=TABLES.TABLE_9B, init_val=init_val, final_xor=final_xor)
    return res


def crc8_darc(data):
    init_val = 0x0
    final_xor = 0x0
    res = crc8_fast(data=data, table=TABLES.TABLE_39, init_val=init_val, final_xor=final_xor)
    return res


def crc8_dvb_s2(data):
    init_val = 0x0
    final_xor = 0x0
    res = crc8_fast(data=data, table=TABLES.TABLE_D5, init_val=init_val, final_xor=final_xor)
    return res


def crc8_ebu(data):
    init_val = 0xFF
    final_xor = 0x0
    res = crc8_fast(data=data, table=TABLES.TABLE_1D, init_val=init_val, final_xor=final_xor)
    return res


def crc8_icode(data):
    init_val = 0xFF
    final_xor = 0x0
    res = crc8_fast(data=data, table=TABLES.TABLE_1D, init_val=init_val, final_xor=final_xor)
    return res


def crc8_itu(data):
    init_val = 0x0
    final_xor = 0x55
    res = crc8_fast(data=data, table=TABLES.TABLE_7, init_val=init_val, final_xor=final_xor)
    return res


def crc8_maxim(data):
    init_val = 0x0
    final_xor = 0x0
    res = crc8_fast(data=data, table=TABLES.TABLE_31, init_val=init_val, final_xor=final_xor)
    return res


def crc8_rohc(data):
    init_val = 0xFF
    final_xor = 0x00
    res = crc8_fast(data=data, table=TABLES.TABLE_7, init_val=init_val, final_xor=final_xor)
    return res


def crc8_wcdma(data):
    init_val = 0x00
    final_xor = 0x00
    res = crc8_fast(data=data, table=TABLES.TABLE_9B, init_val=init_val, final_xor=final_xor)
    return res



