def calculate_points(p):
    return p // 100 + (p >= 1000) * 10


p = int(input())
result = calculate_points(p)
print(result)
