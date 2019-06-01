# huffman
## Introduction

A toy compressing tool using huffman coding. I wrote it because I recently learned about huffman coding.

## Usage

```
$ python cli.py

Usage: cli.py ACTION <INPUT FILE> <OUTPUT FILE>
ACTION: compress, decompress
```

## Examples

```
$ python cli.py compress examples/shakespeare.txt examples/shakespeare.txt.compressed
$ ls -l examples
total 312
-rw-r--r-- 1 cres 200000 Jun  2 00:09 shakespeare.txt
-rw-r--r-- 1 cres 115374 Jun  2 01:36 shakespeare.txt.compressed
```

## Acknowledgement

* [Wikipedia page for Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding)
* [Youtube video about Huffman coding](https://www.youtube.com/watch?v=ikswC-irwY8)
* [100 days of algorithms, day 14: Huffman codes](https://medium.com/100-days-of-algorithms/day-14-huffman-codes-d712bbb0cd10)
