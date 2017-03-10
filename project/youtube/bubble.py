x = [4,5,3,2,1]
def bubble():
    for i in range(len(x)):
        for j in range(1,len(x)+i):
            if x[j-1] > x[j]:
                x[j-1],x[j] = x[j],j[j-1]
    return

