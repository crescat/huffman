from huffman_code import *
import struct
import pickle
import array

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
    result = array.array('B')
    for byte in stream:
        for bit in bin(byte)[2:].rjust(8, '0'):
            result.append(int(bit))
    return result[:-padding]


def compress(byte_stream):
    tree = make_tree(byte_stream)
    bytes_data, padding = bits_to_bytes(encode(byte_stream))
    pickled_tree = pickle.dumps(tree)

    data_len = len(bytes_data)
    tree_len = len(pickled_tree)
    packed_data = struct.pack(f"III{tree_len}s{data_len}B",\
                              data_len, padding, tree_len, \
                              pickled_tree, *bytes_data)

    return packed_data


def decompress(byte_stream):
    data_len, padding, tree_len = struct.unpack(f"III", byte_stream[:12])
    tree = pickle.loads(struct.unpack(f"{tree_len}s", byte_stream[12:12+tree_len])[0])
    unpacked_data = list(struct.unpack(f"{data_len}B", byte_stream[12+tree_len:]))
    result = decode(tree, bytes_to_bits(unpacked_data, padding))

    return result


if __name__  == '__main__':
    # trying compress
    f1 = open('shakespeare.txt', 'rb')
    f2 = open('shakespeare_compressed', 'wb')
    data = f1.read()
    compressed_data = compress(data)
    f2.write(compressed_data)
    f1.close()
    f2.close()

    # trying decompress
    f1 = open('shakespeare_compressed', 'rb')
    f2 = open('shakespeare_decompressed.txt', 'wb')
    data = f1.read()
    decompressed_data = decompress(data)
    f2.write(decompressed_data)
    f1.close()
    f2.close()
