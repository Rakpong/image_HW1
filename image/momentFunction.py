def pqmoment(p, q, img, row, col):
    m = 0
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j] == 1:
                m += (pow(i, p) * pow(j, q))
            else:
                pass
    return m


def pqHu(p, q, img, row, col): 
    u = 0
    m10 = pqmoment(1, 0, img, row, col)
    m00 = pqmoment(0, 0, img, row, col)
    m01 = pqmoment(0, 1, img, row, col)
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j] == 1:
                u += (pow((i - (m10/m00)), p) * pow((j - (m01/m00)), q)) * 1
            else:
                pass
    return u


def pqN(p, q, img, row, col):
    Upq = pqHu(p, q, img, row, col)
    U00 = pow(pqHu(0, 0, img, row, col), (((p+q)/2)+1))
    n = Upq / U00
    return n
