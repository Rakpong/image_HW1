
def read_pgm(filename, col, row):
    file = open(filename, encoding="ISO-8859-1")
    img = ""
    list_img = []
    comment = False
    for i, line in enumerate(file):
        if i == 1 and line[0:1] == "#":
            comment = True
        elif i == 1 and line[0:1] != "#":
            col = int(line[0:3])
            row = int(line[4:])
        if i == 2 and comment == True:
            col = int(line[0:3])
            row = int(line[4:])
        if i >= 4 and comment == True:
            img = img+line
        elif i >= 3 and comment == False:
            img = img+line
    file.close()
    for i in range(len(img)):
        list_img.append((ord(img[i])))
    size = col * row
    list_img = Check_List(list_img, size)
    return list_img, col, row


def list_to_2D_list(lists, list_2D, col, row):
    for i in range(row):
        inner_list = []
        for j in range(col):
            inner_list.append(lists[i*(col)+j])
        list_2D.append(inner_list)
    return list_2D


def copy(lists):
    copy_list = []
    for i in range(len(lists)):
        inner_list = []
        for j in range(len(lists[i])):
            inner_list.append(lists[i][j])
        copy_list.append(inner_list)
    return copy_list


def Check_List(list_img,size):
    if len(list_img) < size:
        while(True):
            list_img.append(0)
            if len(list_img) == size: break
    elif len(list_img) < size:
        while(True):
            list_img.pop
            if len(list_img) == size: break
    return list_img
