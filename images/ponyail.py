def check_results(results):
    return "OK" if sum(display == answer for display, answer in results) >= 3 else "NG"


results = [input().split() for _ in range(5)]
print(check_results(results))
