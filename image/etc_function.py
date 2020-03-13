def createHistogram(converted_img):
    gray_level = []
    frequency = []
    histogram = {}
    for i in range(len(converted_img)):
        if converted_img[i] not in gray_level:
            gray_level.append(converted_img[i])
    gray_level.sort()
    for i in range(len(gray_level)):
        frequency.append(converted_img.count(gray_level[i]))
    histogram = dict(zip(gray_level, frequency))
    return histogram
