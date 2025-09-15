n,m = map(int,input().split())

n_set = set(input() for _ in range(n))
m_set = set(input() for _ in range(m))

result = n_set.intersection(m_set)

print(*n_set.intersection(m_set), sep = '\n')