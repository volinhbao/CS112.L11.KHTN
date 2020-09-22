n = int(input())
a,c = input().split()[:2]
a,b = a.split('/')
c,d = c.split('/')

a=int(a)
b=int(b)
c=int(c)
d=int(d)

points = []

for i in range(1,n+1):
	x,y = map(int,input().split()[:2])
	if b*y-a*x > 0 and d*y-c*x < 0:
		points.append((x,y))

def mykey(x):
	return (c*x[0] - d*x[1],a*x[0] - b*x[1])

points.sort(key=mykey)
lis = []
for point in points:
	low = 0
	high = len(lis) - 1
	ret = 0
	while low <= high:
		mid = (low + high)//2
		if lis[mid] < b*point[1] - a*point[0]:
			ret = mid + 1
			low = mid + 1
		else:
			high = mid - 1
	if ret == len(lis):
		lis.append(b*point[1] - a*point[0])
	else:
		lis[ret] = b*point[1] - a*point[0]
print(len(lis))