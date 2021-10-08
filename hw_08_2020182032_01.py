# import unsorted
# unsorted.numbers

# from unsorted import numbers

# numbers.sort()

class City:
	def __init__(self, name, x, y):
		self.name = name
		self.x = x
		self.y = y
	def __str__(self):
		return str(self.__dict__)
	#def __lt__

cities = [
	City("Vyiaku", 1291462, 1388614),
	City("Zkvch", 1000032, 1388633),
	City("Hrrbu", 1291493, 1291498),
	City("Yjutwb", 1388656, 1291507),
	City("Gkczvyzsb", 1000078, 1388673),
	City("Ojwmvys", 1097255, 1097256),
	City("Hzckr", 1097271, 1291570),
	City("Vxxqjk", 1291581, 1388732),
	City("Eztjjs", 1291597, 1097297),
	City("Uyzucqjgzs", 1194475, 1000176),
	City("Bkmwce", 1291638, 1194491),
	City("Gmnpimohk", 1194519, 1097370),
	City("Nqbst", 1097378, 1388831),
	City("Slickhvgr", 1388858, 1388860),
	City("Wngriprm", 1291743, 1194595),
	City("Gyzjclr", 1000310, 1000312),
	City("Wybisc", 1291773, 1388925),
	City("Tcojtvbt", 1097491, 1194645),
	City("Zkphgbawx", 1097520, 1097521),
	City("Jkepogq", 1097529, 1388980),
	City("Rzakumc", 1000394, 1388997),
	City("Djdji", 1000408, 1194709),
	City("Ntiskuf", 1389021, 1097572),
	City("Dfhsb", 1389034, 1097588),
	City("Mqjonrug", 1389072, 1194776),
	City("Pasmuvjbwh", 1291948, 1194801),
	City("Kdmtnw", 1097664, 1389114),
	City("Dnqpozsyz", 1097704, 1194857),
	City("Fgqryuloy", 1389178, 1000580),
	City("Eaghqmoiua", 1292051, 1389202),
	City("Clkuocwang", 1000639, 1097790),
	City("Jhfghztk", 1000648, 1097802),
	City("Dgablviicy", 1389273, 1292124),
	City("Tlabji", 1292144, 1292148),
	City("Bsweufqtu", 1292173, 1195023),
	City("Jlbvpkrgy", 1389351, 1292205),
	City("Nxareco", 1195067, 1292221),
	City("Vdypyj", 1292235, 1292239),
	City("Prsnro", 1292265, 1195115),
	City("Fsdfgq", 1195131, 1195133),
	City("Yxyrs", 1000844, 1000845),
	City("Chpfbofqh", 1098043, 1195194),
	City("Galneib", 1389511, 1195213),
	City("Oygcnely", 1195233, 1389534),
	City("Cinzakgoyl", 1195253, 1098104),
	City("Fqkxod", 1098124, 1389574),
	City("Prlxlxzz", 1000996, 1292447),
	City("Myitjlbno", 1292463, 1389615),
	City("Xpabtngh", 1292481, 1098182),
	City("Mlybbyr", 1389648, 1389649),
	City("Fuoxtvda", 1292524, 1098226),
	City("Hgywazb", 1389694, 1098245),
	City("Lpgsjaupng", 1001141, 1292591),
	City("Kdvcehpk", 1195462, 1001166),
	City("Ytrgbnosyh", 1001192, 1098347),
	City("Hsttupyy", 1195530, 1389833),
	City("Fihbcv", 1001242, 1195541),
	City("Xwkdalg", 1001269, 1001270),
	City("Bkbuo", 1098429, 1292729),
	City("Ikrvs", 1098454, 1292761),
	City("Navpsbcfy", 1292783, 1098484),
	City("Kdfxyngx", 1292800, 1389948),
	City("Wxduor", 1389973, 1292824),
	City("Tfcavficoq", 1098550, 1195704),
	City("Uogfkdedcu", 1195723, 1195725),
	City("Kcucybbfgi", 1098597, 1292902),
	City("Xzsrcvklhs", 1001473, 1390072),
	City("Qjlxyaic", 1001493, 1390093),
	City("Qlvqpf", 1390107, 1098658),
	City("Xflfolov", 1390129, 1098683),
	City("Gidkdeiia", 1390151, 1098701),
	City("Xybzvxfhj", 1195870, 1098721),
	City("Moels", 1195896, 1098747),
	City("Fhyavpis", 1293062, 1195914),
	City("Hiemhjeh", 1293085, 1001635),
	City("Dgijwi", 1001656, 1195958),
	City("Czhrmpr", 1098832, 1001682),
	City("Vwfdizdjxi", 1390305, 1098856),
	City("Dpyqar", 1390317, 1098867),
	City("Shtmopi", 1390341, 1001745),
	City("Eridll", 1196054, 1001755),
	City("Yaiehzsrk", 1001787, 1196086),
	City("Qndmceoh", 1390410, 1390411),
	City("Lmxrcukkq", 1098988, 1293291),
	City("Hfbtfw", 1001856, 1390460),
	City("Dnzckddgy", 1196175, 1390479),
	City("Iwokwwja", 1001908, 1099061),
	City("Abacfdpi", 1001939, 1001937),
	City("Sbipzz", 1196251, 1099101),
	City("Vabzmfqo", 1001969, 1390569),
	City("Owofzghsb", 1099142, 1001996),
	City("Tufziqcj", 1196317, 1293471),
	City("Tbcohm", 1099192, 1390644),
	City("Vqsavjule", 1002068, 1002070),
	City("Ucbsqy", 1002088, 1002091),
	City("Bkpoqkc", 1293559, 1002113),
	City("Ktklutce", 1002135, 1002136),
	City("Nyiibs", 1002146, 1196456),
	City("Xcbkyuzaq", 1099334, 1390787),
	City("Hrcxrizgg", 1196525, 1196528),
]

# def compare_city(a, b):
#	if a.x < b.x: return -1
#	if a.x > b.x: return 1
#	return 0

def compare_city(a, b):
	return a.x - b.x
	return 0

def key_city(c):
	return c.x

cities.sort(key=lambda c: c.x)

for city in cities:
	print(city)

# names = ['hello', 'world', 'hahaha', 'kakaka']

# names.sort()
# print(names)
