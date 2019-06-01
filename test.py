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


f1 = open('cat.jpg', 'rb')

data = f1.read()

tree = make_tree(data)
bytes_data, padding = bits_to_bytes(encode(data))

L = len(bytes_data)
pickled_tree = pickle.dumps(tree)
P = len(pickled_tree)
packed_data = struct.pack(f"III{P}s{L}B", L, padding, P, pickled_tree, *bytes_data)


### from now on, only 'packed_data' is usable
a, b, c = struct.unpack(f"III", packed_data[:12])
unpacked_tree = pickle.loads(struct.unpack(f"{c}s", packed_data[12:12+c])[0])
print(unpacked_tree)
unpacked_data = list(struct.unpack(f"{a}B", packed_data[12+c:]))

print(data == decode(unpacked_tree, bytes_to_bits(unpacked_data, b)))
