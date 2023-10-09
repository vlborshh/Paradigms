import math
def correlation(arrX, arrY):
    n = len(arrX)

    meanX = sum(arrX) / n
    meanY = sum(arrY) / n

    varX = sum([(xi - meanX) ** 2 for xi in arrX]) / float(len(arrX))
    varY = sum([(yi - meanY) ** 2 for yi in arrY]) / float(len(arrY))

    cov = sum([(xi - meanX) * (yi - meanY) for xi, yi in zip(arrX, arrY)]) / float(len(arrX)) 
    corr = cov / (math.sqrt(varX * varY))

    return corr

arrX = [10, 12, 17, 5, 0, 7, 3]
arrY = [1, 5, 14, 21, 9, 10, 12]

corr = round(correlation(arrX, arrY), 5)
print(f"Корреляция Пирсона: {corr}")