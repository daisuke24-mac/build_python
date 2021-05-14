def add(a,b):
	return a+b
	
def sun(a,b):
	return a-b

def add_to_sub(a,b,c):
	added = add(a,b)
	suned = sun(added,c)
	return suned

if __name__ ==  "__main__":
	print(add(1,2))
	print(add_to_sub(10,2,4))
