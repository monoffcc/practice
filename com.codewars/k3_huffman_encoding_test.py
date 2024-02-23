from k3_huffman_encoding import *
data = [('a', 2), ('b', 2), ('e', 4), ('f', 8), ('g', 16), ('i', 32), ('l', 64), ('n', 128), ('o', 256), ('q', 512), ('s', 1024), ('t', 2048), ('v', 4096), ('w', 8192), ('y', 16384)]



c1='g'
c2='i'
cd1 = encode(data,c1)
cd2 = encode(data,c2)
print(f'{c1}:{cd1}')
print(f'{c2}:{cd2}')
