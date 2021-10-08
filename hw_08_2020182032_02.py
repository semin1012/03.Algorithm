# from random import randint as nextint

from unsorted import numbers

def nextint(beg, end):
	cnt = end - beg + 1
	v =  numbers.pop(0) % cnt 
	return beg + v

count = 3000

def make_ch(isUpper):
	ch = nextint(ord('a'), ord('z'))
	if isUpper: ch -= ord('a') - ord('A')
	return chr(ch)

def make_name():
	name_len = nextint(5, 10)
	name = make_ch(True)
	for i in range(name_len - 1):
		name += make_ch(False)
	return name

def make_city():
	name = make_name()
	x = nextint(1000000, 2000000)
	y = nextint(1000000, 2000000)
	return {"name":name, "x":x, "y":y}

def make_city_obj():
	name = make_name()
	x = nextint(1000000, 2000000)
	y = nextint(1000000, 2000000)
	return 'City("%s", %d, %d),'% (name, x, y)

def make_city_c():
	name = make_name()
	x = nextint(1000000, 2000000)
	y = nextint(1000000, 2000000)
	return '{ "%s", %d, %d },'% (name, x, y)

def make_city_java():
	name = make_name()
	x = nextint(1000000, 2000000)
	y = nextint(1000000, 2000000)
	return 'new City("%s", %d, %d), ' % (name, x, y)

def make_city_js():
	name = make_name()
	x = nextint(1000000, 2000000)
	y = nextint(1000000, 2000000)
	return '{name:"%s", x:%d, y:%d}, ' % (name, x, y)

for i in range(count):
	city = make_city_obj()
	print(city)

