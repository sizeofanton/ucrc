# ucrc
[![License: GPL](https://img.shields.io/badge/License-GPL-blue)](https://gnu.org/licenses/gpl-3.0.txt) [![Build Status](https://travis-ci.com/sizeofanton/ucrc.svg?branch=master)](https://travis-ci.com/sizeofanton/ucrc)

Python module for calculating CRC check with result as unsigned.

### Installation

```sh
$ pip install ucrc
```



### Usage

Example to calculate CRC32 of data block with standard algorithm options:

```python
from ucrc import crc32

data_block = bytes('Hello World'.encode('utf-8'))
crc_value = crc32(data_block)
```

For algorithm customization:
```python
from ucrc import crc32

data_block = bytes('Hello World'.encode('utf-8'))
crc_value = crc32(data_block, poly= 0x12FF00CE, in_ref=True, out_ref=True)
```

For predefined algorithm:

```python
from ucrc import crc32_posix

data_block = bytes([0xAA, 0xBB, 0xCC])
crc_value = crc32(data_block)
```



### Algorithm customization

For all not pre-defined algorithms following options available:

- `poly` - The polynomial, that is used during checksum calculation

- `init_val` - The initial value of checksum

- `final_xor` - The value that is xored to checksum right before it will be returned

- `in_ref` - Boolean, if true the input bits will be flipped

- `out_ref` - Boolean, if true the return value will be flipped

  

### Predefined algorithms:

| Algorithm           | Polynomial         | Initial value      | Final xor value    | Input ref | Output ref |
| ------------------- | ------------------ | ------------------ | ------------------ | --------- | ---------- |
| crc8_saej1850       | 0x1D               | 0xFF               | 0xFF               | False     | False      |
| crc8_saej1850 _zero | 0x1D               | 0x00               | 0x00               | False     | False      |
| crc8_8h2f           | 0x2F               | 0xFF               | 0xFF               | False     | False      |
| crc8_cdma2000       | 0x9B               | 0xFF               | 0x00               | False     | False      |
| crc8_darc           | 0x39               | 0x00               | 0x00               | True      | True       |
| crc8_dvb_s2         | 0xD5               | 0x00               | 0x00               | False     | False      |
| crc8_ebu            | 0x1D               | 0xFF               | 0x00               | True      | True       |
| crc88_icode         | 0x1D               | 0xFD               | 0x00               | False     | False      |
| crc8_itu            | 0x7                | 0x00               | 0x55               | False     | False      |
| crc8_maxim          | 0x31               | 0x00               | 0x00               | True      | True       |
| crc8_rohc           | 0x7                | 0xFF               | 0x00               | True      | True       |
| crc8_wcdma          | 0x9B               | 0x00               | 0x00               | True      | True       |
| crc16_ccit_zero     | 0x1021             | 0x0000             | 0x0000             | False     | False      |
| crc16_arc           | 0x8005             | 0x0000             | 0x0000             | True      | True       |
| crc16_aug_ccitt     | 0x1021             | 0x1D0F             | 0x0000             | False     | False      |
| crc16_buypass       | 0x8005             | 0x0000             | 0x0000             | False     | False      |
| crc16_ccitt_false   | 0x1021             | 0xFFFF             | 0x0000             | False     | False      |
| crc16_cdma2000      | 0xC867             | 0xFFFF             | 0x0000             | False     | False      |
| crc16_dds_110       | 0x8005             | 0x800D             | 0x0000             | False     | False      |
| crc16_detect_r      | 0x589              | 0x0000             | 0x0001             | False     | False      |
| crc16_detect_x      | 0x589              | 0x0000             | 0x0000             | False     | False      |
| crc16_dnp           | 0x3D65             | 0x0000             | 0xFFFF             | True      | True       |
| crc16_en_13757      | 0x3D65             | 0x0000             | 0xFFFF             | False     | False      |
| crc16_genibus       | 0x1021             | 0xFFFF             | 0xFFFF             | False     | False      |
| crc16_maxim         | 0x8005             | 0x0000             | 0xFFFF             | True      | True       |
| crc16_mcrf4xx       | 0x1021             | 0xFFFF             | 0x0000             | True      | True       |
| crc16_riello        | 0x1021             | 0xB2AA             | 0x0000             | True      | True       |
| crc16_t10_dif       | 0x8BB7             | 0x0000             | 0x0000             | False     | False      |
| crc16_teledisk      | 0xA097             | 0x0000             | 0x0000             | False     | False      |
| crc16_tms37157      | 0x1021             | 0x89EC             | 0x0000             | False     | False      |
| crc16_usb           | 0x8005             | 0xFFFF             | 0xFFFF             | True      | True       |
| crc16_a             | 0x1021             | 0xC6C6             | 0x0000             | True      | True       |
| crc16_kermit        | 0x1021             | 0x0000             | 0x0000             | True      | True       |
| crc16_modbus        | 0x8005             | 0xFFFF             | 0x0000             | True      | True       |
| crc16_x_25          | 0x1021             | 0xFFFF             | 0xFFFF             | True      | True       |
| crc16_xmodem        | 0x1021             | 0x0000             | 0x0000             | False     | False      |
| crc32_bzip2         | 0x4C11DB7          | 0xFFFFFFFF         | 0xFFFFFFFF         | False     | False      |
| crc32_c             | 0x1EDC6F41         | 0xFFFFFFFF         | 0xFFFFFFFF         | True      | True       |
| crc32_d             | 0xA83398B          | 0xFFFFFFFF         | 0xFFFFFFFF         | True      | True       |
| crc32_mpeg2         | 0x4C11DB7          | 0xFFFFFFFF         | 0x00000000         | False     | False      |
| crc32_posix         | 0x4C11DB7          | 0x00000000         | 0xFFFFFFFF         | False     | False      |
| crc32_q             | 0x814141AB         | 0x00000000         | 0x00000000         | False     | False      |
| crc32_jamrc         | 0x4C11DB7          | 0xFFFFFFFF         | 0x00000000         | True      | True       |
| crc32_xfer          | 0xAF               | 0x00000000         | 0x00000000         | False     | False      |
| crc64_ecma_182      | 0x42F0E1EBA9EA3693 | 0x0000000000000000 | 0x0000000000000000 | False     | False      |
| crc64_go_iso        | 0x000000000000001B | 0xFFFFFFFFFFFFFFFF | 0xFFFFFFFFFFFFFFFF | True      | True       |
| crc64_we            | 0x42F0E1EBA9EA3693 | 0xFFFFFFFFFFFFFFFF | 0xFFFFFFFFFFFFFFFF | False     | False      |
| crc64_xz            | 0x42F0E1EBA9EA3693 | 0xFFFFFFFFFFFFFFFF | 0xFFFFFFFFFFFFFFFF | True      | True       |



