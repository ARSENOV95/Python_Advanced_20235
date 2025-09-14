n,m = list(map(int,input().split()))

n_ = set()
m_ = set()


for i in range(1,(n+m)+1):
    element = int(input())
    if i <= n:
        n_.add(element)
    else:
        m_.add(element)

print(*n_.intersection(m_),sep = '\n')