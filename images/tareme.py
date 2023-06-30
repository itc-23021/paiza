def check_result(s, n):
    return "OK" * (s >= n) or "NG"


s, n = map(int, input().split())
print(check_result(s, n))
