n,m = map(int,input().split())

n_ = set()
m_ = set()

for i in range(1,(n+m)+1):
    if i <= n:
        n_.add(int(input()))
    else:
        m_.add(int(input()))

print(*n_.intersection(m_),sep = '\n')