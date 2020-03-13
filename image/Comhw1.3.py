from readpgm import read_pgm, list_to_2D_list, copy
from writepgm import writepgm
from etc_function import createHistogram

fileBlue = "./image/3_/SanFranPeak_blue.pgm"
fileRed = "./image/3_/SanFranPeak_red.pgm"
fileGreen = "./image/3_/SanFranPeak_green.pgm"
converted_img_Blue = []
converted_img_Red = []
converted_img_Green = []
mattrix_img_Blue = []
mattrix_img_Red = []
mattrix_img_Green = []
col = 0
row = 0

converted_img_Blue, col, row = read_pgm(fileBlue, col, row)
converted_img_Red, col, row = read_pgm(fileRed, col, row)
converted_img_Green, col, row = read_pgm(fileGreen, col, row)
mattrix_img_Blue = list_to_2D_list(converted_img_Blue, mattrix_img_Blue, col, row)
mattrix_img_Red = list_to_2D_list(converted_img_Red, mattrix_img_Red, col, row)
mattrix_img_Green = list_to_2D_list(converted_img_Green, mattrix_img_Green, col, row)
mattrix_img_Result = mattrix_img_Blue

for i in range(len(mattrix_img_Blue)): # mixed color
    for j in range(len(mattrix_img_Blue[i])):
        template = ( mattrix_img_Blue[i][j] +mattrix_img_Red[i][j] + mattrix_img_Green[i][j] ) / 3
        template2 = int(template)
        if (template - template2) >= 0.5 :
            template = template2 + 1
        else: 
            template = template2 
        mattrix_img_Result[i][j] = template

row = len(mattrix_img_Result)
col = len(mattrix_img_Result[0])
fileResult = "SanFranPeak_Result.pgm"
writepgm(fileResult, mattrix_img_Result, col, row)