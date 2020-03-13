from readpgm import read_pgm

filename = "./image/1_/scaled_shapes.pgm"
col = 0
row = 0
img, col, row = read_pgm(filename, col, row)
img2  = read_pgm(filename, col, row)

# print(img[2])
