import sys

t = int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    a = map(int, raw_input().split())
    a[0] = max(a[0], 0)
    a[1] = max(a[1], a[0], 0)
    for j in range(2, n):
        a[j] = max(a[j-2]+a[j], a[j-1], 0)
    answer = max(a)
    if answer <= 0:
        print 'DANGER'
    else:
        print answer
