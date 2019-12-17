
def bytes_to_int(data):

    """
    Convert bytes to integer
    :param data: bytes of data
    :return: result int
    """

    result = 0
    for b in data:
        result = result * 256 + int(b)
    return result


def ref_bits(x):

    """
    :param x: byte to reverse
    :return: reversed byte
    """

    b = bin(x)[2::].zfill(8)
    b = b[8::-1]
    return int(b,2)


def ref(data):

    """
    :param data: input bytes to reverse
    :return: reversed data bytes
    """

    tmp = []
    print(data)
    for byte in data:
        byte_r = ref_bits(byte)
        tmp.append(byte_r)

    data = bytes(tmp)
    return data

