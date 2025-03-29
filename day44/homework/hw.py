def reverse_seq(n):
    return list(range(n, 0, -1))






def reverse_seq(n):
    res = []

    for i in range(n, 0, -1):
        res.append(i)

    return res