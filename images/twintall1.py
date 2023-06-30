def calculate_cost_performance(c, p):
    return c / p


c1, p1 = map(int, input().split())
c2, p2 = map(int, input().split())

cost_performance_1 = calculate_cost_performance(c1, p1)
cost_performance_2 = calculate_cost_performance(c2, p2)

if cost_performance_1 > cost_performance_2:
    print(1)
else:
    print(2)
