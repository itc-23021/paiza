votes = [input() for _ in range(5)]
result = max(set(votes), key=votes.count)
print(result)
