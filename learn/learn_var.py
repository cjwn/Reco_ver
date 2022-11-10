import csv
import os

from tools import time_it


class TestVar:
    def __init__(self):
        names = self.__dict__
        for i in range(6):
            names['n' + str(i)] = i


t = TestVar()
print(1, t.n0, t.n1)


class VarStruct:

    def __init__(self, name_list):
        self.name = name_list[0]
        self.path = name_list[1]
        self.size = name_list[2]


name_list = ['name', 'c://temp/', '1213']


def name_var(foo):
    res = []
    for i in range(6):
        res.append(list(map(lambda x:x+str(i), foo)))
    return res


@time_it
def dict_var():
    res = []
    temp2 = [0]*6
    print(4444,temp2)
    d = {'name':'foo', 'path':'c://temp/', 'size': 123}
    d_values = d.values()
    d_keys = d.keys()
    for i in range(6):
        new_d_values = map(lambda x:x+i if type(x) is int else x+str(i), d_values)
        temp2[i] = dict(zip(d_keys, new_d_values))
    for i in temp2:
        write_csv(i)
    return temp2

def write_csv(z):
    header = ['name', 'path', 'size']
    exist = False
    data = [z['name'], z['path'], z['size']]
    if os.path.exists('temp2.csv'):
        exist = True
    with open('temp2.csv', mode='a', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        if not exist:
            writer.writerow(header)
        writer.writerow(data)
        print(z['size'])


def write_row():
    with open('temp3.csv', 'a', encoding='utf-8-sig', newline='') as f:
        wtr = csv.writer(f)
        wtr.writerow(['id', 'name', 'age'])
        wtr.writerow(['1001', 'ZhangSan', '19'])
        wtr.writerow(['1002', 'Lisi', 20])

print(1, write_row())
print(3, dict_var())
# print(2, name_var(name_list))
# print(7, dict_var())
