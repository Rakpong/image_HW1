from readpgm import read_pgm, list_to_2D_list, copy
from writepgm import writepgm
from etc_function import createHistogram
# filename = "./image/2_/Cameraman.pgm"
filename = "./image/2_/SEM256_256.pgm"
converted_img = []
mattrix_img = []
col = 0
row = 0

converted_img, col, row = read_pgm(filename, col, row)
mattrix_img = list_to_2D_list(converted_img, mattrix_img, col, row)
histogram_old = createHistogram(converted_img)
current_D = []

for i in range(256):  # find miss colour
    if i not in histogram_old:
        histogram_old.update({i: 0})

histogram_old = {key: histogram_old[key]
                 for key in sorted(histogram_old.keys())}  # sorted to dict
histogram_db = histogram_old.copy()

for i in histogram_db:
    histogram_db[i] = histogram_db[i] / (col*row)  # convert to PDF
Sum_HD = 0
for i in histogram_db:
    Sum_HD += histogram_db[i]
    histogram_db[i] = Sum_HD                # convert to PMF
for i in histogram_db:
    histogram_db[i] = histogram_db[i]*255   # convert to CMF 
    temp = int(histogram_db[i] )
    if (histogram_db[i] - temp) >= 0.5 :
        histogram_db[i] = temp + 1
    else:
        histogram_db[i] = temp             # make into floor number
# convert from {DA : DB} to {DB : DA}
histogram_db = dict((y, x) for x, y in histogram_db.items())
# current dict is {DB : DA }
for i in range(len(mattrix_img)):
    for j in range(len(mattrix_img[i])):
        for key in histogram_db:
            if mattrix_img[i][j] == histogram_db[key]:
                mattrix_img[i][j] = key

new_histogram_list = [i for subarray in mattrix_img for i in subarray]
new_histogram = createHistogram(new_histogram_list)
print("Histogram D[A]" + str(histogram_old))
print("--------------------")
print("D[A] : D[B]")
print(histogram_db)

print("-------------")
print("Histogram D[B]" + str(new_histogram))
# filename_new = "cameraman2.pgm"
filename_new = "bean.pgm"
writepgm(filename_new, mattrix_img, col, row)
