def count_sheep(n):
    if n == 0: return ""

    res = ""
    for i in range(1, n+1):
        res += f"{i} sheep..."

    return res