num_array = []

NUMBER_OF_ELEMENTS = int(input())
# print(NUMBER_OF_ELEMENTS)
f_array = [int] * NUMBER_OF_ELEMENTS

# print(type(NUMBER_OF_ELEMENTS))
num_array= list(map(int,input().split()))

# Store the smallest value of a substring of num_array
smallest_substr = 0
s_index = -1
max_substr = 0
max_index = 0
flag = False
left = 0
right = 0
res = float('-inf')

for i in range(0, NUMBER_OF_ELEMENTS):
	if(i == 0):
		f_array[0] = num_array[0];
		max_substr = f_array[0];
		# smallest_substr = f_array[0];
	else:
		f_array[i] = f_array[i-1] + num_array[i];
		max_substr = f_array[i] - smallest_substr
	if (max_substr>res):
		res = max_substr
		print(res)
		right = i
		left = s_index
		flag = True
	if(i ==0 ): 
		flag = False
		continue
	if f_array[i] < smallest_substr:
		smallest_substr = f_array[i] 
		s_index = i
print(f_array)	
print(left+2, right+1, res)