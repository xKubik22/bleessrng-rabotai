

if __name__ == '__main__':
    # price = {'ДИ': 1000, 'КП': 200}
    # print(price.values())
    # print(price.keys())
    # print(price.items())
    # price.update({'Аттестация': 2000})
    # print(price.items())
    #
    # values = [100, 200, 300, 400]
    # names = ['1', '2', '3', '4']
    # d = {names[i]: values[i] for i in range(len(names))}
    #
    # print(d.items())

    l = [1, 2, 4, 5, 6, 7, 8, 9, 10]
    d = {l[i]: l[i + 1] for i in range(0, len(l) - 1, 2)}
    print(d.items())