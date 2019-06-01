from huffman_code import *
import struct
import pickle

def bits_to_bytes(bits):
    length = len(bits)
    padding = 8 - (length % 8)
    bits += [0] * padding
    result = []
    for i in range(0, len(bits), 8):
        b = bits[i:i+8]
        result.append(int(''.join([str(x) for x in b]), 2))
    return result, padding


def bytes_to_bits(stream, padding):
    result = []
    for byte in stream:
        for bit in bin(byte)[2:].rjust(8, '0'):
            result.append(int(bit))
    return result[:-padding]


def compress(filename, output_filename):
    f1 = open(filename, 'rb')
    f2 = open(output_filename, 'wb')
    data = f1.read()
    tree = make_tree(data)
    bytes_data, padding = bits_to_bytes(encode(data))
    pickled_tree = pickle.dumps(tree)

    data_len = len(bytes_data)
    tree_len = len(pickled_tree)
    packed_data = struct.pack(f"III{tree_len}s{data_len}B",\
                              data_len, padding, tree_len, \
                              pickled_tree, *bytes_data)
    f2.write(packed_data)


def decompress(filename, output_filename):
    f1 = open(filename, 'rb')
    f2 = open(output_filename, 'wb')

    data = f1.read()

    data_len, padding, tree_len = struct.unpack(f"III", data[:12])
    tree = pickle.loads(struct.unpack(f"{tree_len}s", data[12:12+tree_len])[0])
    unpacked_data = list(struct.unpack(f"{data_len}B", data[12+tree_len:]))
    result = decode(tree, bytes_to_bits(unpacked_data, padding))
    f2.write(result)

compress('cat.jpg', 'cat_compress')
decompress('cat_compress', 'cat_decompress.jpg')
