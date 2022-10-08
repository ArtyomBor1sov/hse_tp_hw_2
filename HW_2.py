def _min(array):
    minimum = array[0]
    for i in range(1, len(array)):
        if array[i] < minimum:
            minimum = array[i]
    return minimum

def _max(array):
    maximum = array[0]
    for i in range(1, len(array)):
        if array[i] > maximum:
            maximum = array[i]
    return maximum

def _sum(array):
    summa = 0
    for i in range(len(array)):
        summa += array[i]
    return summa

def _mult(array):
    multiply = 1
    for i in range(len(array)):
        multiply *= array[i]
    return multiply
