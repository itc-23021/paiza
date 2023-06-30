def check_divisibility(n, m):
    return "ok" if m % n == 0 else "ng"


n, m = map(int, input().split())
result = check_divisibility(n, m)
print(result)
