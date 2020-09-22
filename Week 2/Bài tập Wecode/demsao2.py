from bisect import *
n = int(input())
a, b, c, d = map(int, input().replace(' ', '/').split('/'))
l = []
for x, y in sorted((x, -y) for x, y in [(c * x - d * y, b * y - a * x) for x, y in [map(int, input().split()) for _ in range(n)]] if x > 0 and y > 0):
	v = bisect_left(l, -y)
	if v == len(l):
		l.append(-y)
	else:
		l[v] = -y
print(len(l))