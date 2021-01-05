n = int(input())
c = list(map(int,input().split(" ")))
c.sort(reverse = True)
res = 0
low = 0
high = n - 1
while (low <= high):
	mid = (low + high) // 2
	if(c[mid] >= mid + 1):
		res = mid + 1
		low = mid + 1
	else:
		high = mid - 1
print(res)
