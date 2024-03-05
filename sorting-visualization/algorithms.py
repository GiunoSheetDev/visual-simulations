import random


def bubbleSort(ls : list):
    for j in range(0, len(ls)-1):
        if ls[j] > ls[j+1]:
            ls[j], ls[j+1] = ls[j+1], ls[j]
    return ls

def bogoSort(ls : list):
    random.shuffle(ls)
    
    return ls

