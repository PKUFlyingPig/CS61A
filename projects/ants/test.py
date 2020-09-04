class A():
	"""docstring for A"""
	haha = 10

s = [A() for i in range(3)]
for i, a in enumerate(s):
	print(s[i] is a)