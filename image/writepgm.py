# Must be done someday
def writepgm(filename, mattriximg, col, row):
    string = ""
    for i in range(len(mattriximg)):
        for j in range(len(mattriximg[i])):
            mattriximg[i][j] = chr(mattriximg[i][j])
            string += mattriximg[i][j]
    # print(len(mattriximg))
    f = open(filename, "a", encoding="ISO-8859-1")

    f.write("P5 \r")
    f.write(str(col) + " " + str(row) + "\r")
    f.write("255 \r")
    f.write(string)
    f.close
