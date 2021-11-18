def calculate(data, findall):
    matches = findall(r"([a-c])([+-]?)=([a-c]?)([+-]?\d+)?")
    # Если придумать хорошую регулярку, будет просто
    for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        # Если бы могло быть только =, вообще одной строкой все считалось бы, вот так:
        if v2 == '' and s == '' and '+' not in n and '-' not in n:
            data[v1] = int(n)
        elif v2 == '' and s == '':
            data[v1] = int(data[v1]) + int(n)
        elif s == '' and n == '':
            data[v1] = data[v2]
        elif s != '' and v2 == '':
            if s == '+':
                data[v1] = int(data[v1]) + int(n)
            else:
                data[v1] = int(data[v1]) - int(n)
        elif v2 != '' and n == '' and s != '' and v2.isalpha() == True:
            if s == '+':
                data[v1] = int(data[v1]) + int(data[v2])
            else:
                data[v1] = int(data[v1]) - int(data[v2])
        elif v2 != '' and n != '' and s != '' and v2.isalpha() == True:
            if s == '+':
                data[v1] = int(data[v1]) + int(data[v2]) + int(n)
            else:
                if int(data[v1]) == 0 and int(data[v2]) == 0:
                    data[v1] = -1 * int(n)
                else:
                    data[v1] = int(data[v1]) - int(data[v2]) + int(n)
        else:
            data[v1] = data.get(v2, 0) + int(n or 0)
    return data
# {'a': -98, 'b': 196, 'c': -98}
# c - b