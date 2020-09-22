n,k = input().split()[:2]
n = int(n)
k = int(k)
modulo = 10**9+7

coef = [[0,1],[1,1]]
k *= 2

def matrix_mul(x,y):
	ret = []
	ret.append([(x[0][0]*y[0][0]+x[0][1]*y[1][0])%modulo,\
				(x[0][0]*y[0][1]+x[0][1]*y[1][1])%modulo])
	ret.append([(x[1][0]*y[0][0]+x[1][1]*y[1][0])%modulo,\
				(x[1][0]*y[0][1]+x[1][1]*y[1][1])%modulo])
	return ret

def matrix_pw(x):
	if x == 1:
		return coef
	tmp = matrix_pw(x//2)
	if x%2==1:
		return matrix_mul(matrix_mul(tmp,tmp),coef)
	else:
		return matrix_mul(tmp,tmp)

bf = matrix_pw(k-1)
bf = bf[1][0] + bf[1][1]

print((bf*n)%modulo)