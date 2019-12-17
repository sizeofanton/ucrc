# ucrc
[![License: GPL](https://img.shields.io/badge/License-GPL-blue)](gnu.org/licenses/gpl-3.0.txt)

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

