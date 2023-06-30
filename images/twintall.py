def generate_progress_bar(s, t):
    return "-" * (t - 1) + "+" + "-" * (s - t)


s = int(input())
t = int(input())
progress_bar = generate_progress_bar(s, t)
print(progress_bar)
