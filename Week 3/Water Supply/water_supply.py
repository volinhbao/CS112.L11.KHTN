n,m = map(int,input().split(" "))
adj = {}
visited = {}
mod = int(10**9 + 7)

for i in range(m):
	a, b= map(int, input().split(" "))
	if a < 1 or a > n or b < 1 or b > n:
		continue
	if a in adj:
		adj[a].append(b)
	else:
		adj[a] = [b]
	
	if b in adj:
		adj[b].append(a)
	else:
		adj[b] = [a]

comp = []
#print(adj)

for i in range(1,n+1):
	if not i in visited:
		ls = [i]
		visited[i] = True
		ind = 0
		while ind < len(ls):
			if not ls[ind] in adj:
				ind += 1
				continue
			for e in adj[ls[ind]]:
				if not e in visited:
					visited[e] = True
					ls.append(e)
			ind += 1
		comp.append(len(ls))

#print(comp)

ans = 0
if len(comp)>1:
	ans = (n**(len(comp)-2)) % mod
	for x in comp:
		ans = (ans * x) % mod

print(len(comp)-1)
print(int(ans)) 