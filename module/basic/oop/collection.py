from functools import *
import sys, os

class Rec(object):
    a = ""
    b = 2
    c = 3
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
    def __repr__(self):
        return "Item(%s, %d, %d)" % (self.a, self.b, self.c)
    def __eq__(self, obj) -> bool:
        return self.b == obj.b and self.c == obj.c
    def __hash__(self) -> int:
        return self.b + self.c
    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(object)
    pass


if __name__ == "__main__":
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    #2 sort:
    ages = sorted(ages, reverse=False)
    print(f"after sort:{ages}")
    print(f"min:{ages[0]} max:{ages[-1]}")
    #3 add min and max again:
    print(f"before extend ages: {id(ages)} size:{sys.getsizeof(ages)}")
    sum_arr = ages + [ages[0]] + [ages[1]]
    print(f"sum plus:{id(sum_arr)} size:{sys.getsizeof(sum_arr)}")
    print(f"after add min and max again:{ages}")
    ages.extend([ages[0], ages[-1]])
    print(f"after extend:{id(ages)} size:{sys.getsizeof(ages)}")
    #4 find median:
    len_arr = len(ages)
    median = 0
    if len_arr % 2 == 1: median = ages[len_arr//2-1:len_arr//2-1]
    else: median = ages[(len_arr//2)-1:(len_arr//2)+1]
    print(f"median:{median}")
    #5 find avg:
    avg = reduce(lambda a, b: a+b, ages, 0)/len_arr
    print(f"avg:{avg}")
    #6 find range:
    ages = sorted(ages)
    print(f"range: {ages[-1] - ages[0]}")
    #7 compare:
    print(f"compare: {abs((ages[-1] - avg)) - abs(ages[0] - avg)}")

    x = Rec("x", 1 ,3)
    x1 = Rec("x1", 1 ,2)
    z = Rec("y", 1 ,2)
    set_elem = {x, x1, z}
    print(set_elem)