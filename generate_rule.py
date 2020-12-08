table= [[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16]]
rules = []
for mat in table:
	for i in range(0,4):
		for j in range(0,4):
			if(j<=i):
				continue
			row =[]
			print(i,j)
			val1 = mat[i]
			val2 = mat[j]
			if(mat[i] <=9):
				val1 = "0{}".format(val1)
			if(mat[j] <=9):
				val2 = "0{}".format(val2)
			val1 = "00:00:00:00:00:{}".format(val1)
			val2 = "00:00:00:00:00:{}".format(val2)
			row.append(val1)
			row.append(val2)
			rules.append(row)
			# 00:00:00:00:00:06
print(rules)