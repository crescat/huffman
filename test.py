from huffman_code import *
import struct

def bits_to_bytes(bits):
    length = len(bits)
    padding = 8 - (length % 8)
    bits += [0] * padding
    result = []
    for i in range(0, len(bits), 8):
        b = bits[i:i+8]
        result.append(int(''.join([str(x) for x in b]), 2))
    return result, padding


f1 = open('cat.jpg', 'rb')
f2 = open('cat2', 'wb')

data = f1.read()
tree = make_tree(data)
huff_data = encode(data)
bytes_data, padding = bits_to_bytes(huff_data)
L = len(bytes_data)
packed_data = struct.pack(f"I{L}B", L, *bytes_data)
a = struct.unpack(f"I", packed_data[:4])
unpacked_data = struct.unpack(f"{a[0]}B", packed_data[4:])
print(unpacked_data)
