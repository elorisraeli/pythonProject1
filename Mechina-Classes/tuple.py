def summer(lst, lst2=[]):
    if lst2 != []:
        return lst + lst2
    res = 0
    res2 = ''
    flag = False
    for i in lst:
        if type(i) == str:
            res2 += i
            flag = True
        else:
            res += 1
    if flag:
        return res2
    else:
        return res


def main():
    print(summer([10, 11, 12, 0.75]))
    print(summer([True, False, True, True]))
    print(summer(['aa', 'bb', 'cc', 'dd']))
    print(summer([1, 2, 3, 'a'], [4, 'b', 'c', 'd']))


if __name__ == '__main__':
    main()

