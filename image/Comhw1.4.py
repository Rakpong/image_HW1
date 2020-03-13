from readpgm import read_pgm, list_to_2D_list, copy
from writepgm import writepgm
from etc_function import createHistogram

file_Lenna = "./image/4_/distlenna.pgm"

converted_img_Lenna = []
mattrix_FalseGrid = []
mattrix_TrueGrid = []
mattrix_Lenna = []
col = 0
row = 0
converted_img_Lenna, col, row = read_pgm(file_Lenna, col, row)
mattrix_Lenna = list_to_2D_list(converted_img_Lenna, mattrix_Lenna, col, row)

mattrix_TrueGrid = mattrix_Lenna        # mattrix_TrueGrid have gray level 0 at cutting point 255 otherwise
for i in range(len(mattrix_TrueGrid)): 
    for j in range(len(mattrix_TrueGrid[i])):
        mattrix_TrueGrid[i][j] = 255 
for i in range(len(mattrix_TrueGrid)): 
    for j in range(len(mattrix_TrueGrid[i])):
        if( ( (j!=0) and (j%16) == 0) ):
            if( ( (i+1) %16 ) == 0 ):
                mattrix_TrueGrid[i][j] = 0
        elif (j == 0):
            if( (i%16)==0 or (i==0)):
                mattrix_TrueGrid[i][j] = 0
# cutting point from FalseGrid 
disgrid = [[[0,0],[16,0],[32,0],[48,0],[64,0],[80,0],[96,0],[112,0],[128,0],[144,0],[160,0],[176,0],[192,0],[208,0],[224,0],[240,0],[255,0]],
           [[0,15],[16,15],[32,15],[48,15],[64,15],[80,15],[97,16],[114,17],[130,18],[145,18],[161,17],[176,15],[192,15],[208,15],[224,15],[240,15],[255,15]],
           [[0,31],[16,31],[32,31],[48,31],[66,32],[85,34],[103,36],[121,39],[136,41],[150,42],[163,40],[177,37],[192,33],[208,31],[224,31],[240,31],[255,31]],
           [[0,47],[16,47],[32,47],[51,48],[72,49],[93,52],[112,56],[128,59],[141,62],[154,64],[166,64],[178,62],[192,56],[207,50],[224,47],[240,47],[255,47]],
           [[0,63],[16,63],[34,63],[56,63],[79,64],[99,67],[117,71],[131,75],[144,79],[156,83],[167,84],[178,83],[191,79],[206,72],[223,65],[240,63],[255,63]],
           [[0,79],[16,79],[38,78],[62,77],[84,77],[103,80],[118,83],[132,89],[144,94],[155,99],[165,102],[176,102],[188,100],[203,93],[221,85],[240,79],[255,79]],
           [[0,95],[18,95],[41,92],[65,90],[86,89],[103,91],[118,94],[131,101],[141,107],[151,113],[161,116],[172,117],[184,117],[200,111],[218,104],[238,97],[255,95]],
           [[0,111],[19,110],[43,106],[65,102],[84,100],[101,101],[115,105],[127,111],[136,118],[145,125],[155,130],[167,131],[180,131],[196,127],[215,121],[237,113],[255,111]],
           [[0,127],[19,125],[42,119],[63,114],[81,111],[96,111],[109,114],[121,119],[129,127],[138,135],[149,140],[161,143],[176,143],[193,140],[213,136],[236,129],[255,127]],
           [[0,143],[18,141],[40,135],[60,128],[77,124],[91,122],[103,125],[113,129],[121,135],[131,143],[142,149],[156,153],[172,155],[190,153],[212,149],[236,145],[255,143]],
           [[0,159],[17,158],[38,151],[57,143],[72,139],[85,137],[96,137],[106,141],[115,146],[126,153],[138,159],[153,164],[170,166],[190,165],[214,162],[238,160],[255,159]],
           [[0,175],[16,175],[35,170],[54,161],[69,155],[81,152],[93,152],[102,154],[113,159],[124,164],[137,170],[153,174],[172,177],[192,177],[217,176],[239,175],[255,175]],
           [[0,191],[16,191],[33,189],[51,181],[66,175],[79,170],[90,169],[101,170],[112,174],[125,178],[139,183],[156,187],[175,189],[198,191],[221,191],[240,191],[255,191]],
           [[0,207],[16,207],[32,207],[49,204],[65,197],[78,192],[90,189],[102,189],[114,191],[127,194],[143,198],[161,201],[182,204],[204,206],[224,207],[240,207],[255,207]],
           [[0,223],[16,223],[32,223],[48,223],[64,220],[79,216],[93,213],[106,211],[119,212],[134,214],[151,217],[169,219],[190,222],[208,223],[224,223],[240,223],[255,223]],
           [[0,239],[16,239],[32,239],[48,239],[64,239],[80,239],[95,237],[110,236],[126,235],[142,236],[158,237],[175,238],[192,239],[208,239],[224,239],[240,239],[255,239]],
           [[0,255],[16,255],[32,255],[48,255],[64,255],[80,255],[96,255],[112,255],[128,255],[144,255],[160,255],[176,255],[192,255],[208,255],[224,255],[240,255],[255,255]]
          ]
mattrix_FalseGrid = mattrix_TrueGrid          # mattrix_FalseGrid have gray level 0 at cutting point 255 otherwise
for i in range(len(mattrix_FalseGrid)): 
    for j in range(len(mattrix_FalseGrid[i])):
        mattrix_FalseGrid[i][j] = 255 
for i in range(len(disgrid)): 
    for j in range(len(disgrid[i])):
        temp_i = disgrid[i][j][0]
        temp_j = disgrid[i][j][1]
        mattrix_FalseGrid[temp_i][temp_j] = 0
# print(mattrix_FalseGrid[42][120])

def Bilinear(pixel_input,Glevel_Mattrix):
    tempi_1 = int(pixel_input[0])
    tempi_2 = int(pixel_input[0]) + 1
    tempj_1 = int(pixel_input[1])
    tempj_2 = int(pixel_input[1]) + 1
    i_position = pixel_input[0] - tempi_1
    j_position = pixel_input[1] - tempj_1
    i_Glevel = abs( Glevel_Mattrix[tempi_1][tempj_1] - Glevel_Mattrix[tempi_2][tempj_1] ) * i_position
    i_Glevel = min( Glevel_Mattrix[tempi_1][tempj_1], Glevel_Mattrix[tempi_2][tempj_1] ) + i_Glevel
    j_Glevel = abs( Glevel_Mattrix[tempi_1][tempj_2] - Glevel_Mattrix[tempi_2][tempj_2] ) * i_position
    j_Glevel = min( Glevel_Mattrix[tempi_1][tempj_2], Glevel_Mattrix[tempi_2][tempj_2] ) + j_Glevel
    Glevel = abs( i_Glevel - j_Glevel ) * j_position
    Glevel = min( i_Glevel , j_Glevel ) + Glevel
    return Glevel
    


# fileResult = "Lenna_Result.pgm"
# writepgm(fileResult, mattrix_img_Result, col, row)