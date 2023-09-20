import pprint
from random import randint
import matplotlib.pyplot
from matplotlib.pyplot import gist

def aValue(arr: list[int]) -> float:
    return sum(arr) / len(arr)


def disp(arr: list[int]) -> float:
    return sum((x - aValue(arr)) ** 2 for x in arr) / len(arr)


def mode(arr: list[int]) -> int:
    return max(arr, key=arr.count)


def mediana(arr: list[int]) -> float:
    return (arr[9] + arr[10]) / 2


def stndDivi(arr: list[int]) -> float:
    return disp(arr) ** 0.5


def cofVar(arr: list[int]) -> float:
    return disp(arr) / aValue(arr)


def scope(arr: list[int]) -> float:
    return max(arr) - min(arr)


def output(arr: list[int]) -> None:
    
    
    
    print(f"varRyad: {arr}")
    print(f"SrZnach: {aValue(arr)}")
    print(f"Dispertion: {disp(arr)}")
    print(f"Moda: {mode(arr)}")
    print(f"Mediane: {mediana(arr)}")
    print(f"StandOtclon: {stndDivi(arr)}")
    print(f"CoffVar: {cofVar(arr)}")
    print(f"Scope: {scope(arr)}")




if __name__ == "__main__":
    num = []
    for i in range(20):
        num.append(randint(1, 9))

    num.sort()

    output(num)
