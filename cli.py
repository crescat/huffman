from utils import *
import sys


def run_with_sys_argv(args):
    if args[1] not in ['compress', 'decompress']:
        raise Exception('something wrong!')
    f1 = open(args[2], 'rb')
    f2 = open(args[3], 'wb')
    data = f1.read()
    if args[1] == 'compress':
        processed_data = compress(data)
    elif args[1] == 'decompress':
        processed_data = decompress(data)
    f2.write(processed_data)
    f1.close()
    f2.close()


if __name__  == '__main__':
    if len(sys.argv) == 4:
        run_with_sys_argv(sys.argv)
    else:
        print(f"""
        Usage: {sys.argv[0]} ACTION <INPUT FILE> <OUTPUT FILE>
        ACTION: compress, decompress
        """)
