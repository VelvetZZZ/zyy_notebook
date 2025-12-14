def bigs(t):
    def f(a, x):  # x = max label among ancestors of a
        if a.label > x:
            return 1 + sum(f(b, a.label) for b in a.branches)
        else:
            return sum(f(b, x) for b in a.branches)
    return f(t, t.label - 1)
    