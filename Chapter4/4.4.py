def mile2km(m):
    result = 1.61 * m
    return result


for i in range(1, 6):
    print(i, "마일 =", mile2km(i), "킬로미터")
