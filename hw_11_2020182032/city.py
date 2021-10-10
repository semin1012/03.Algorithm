class City:
	def __init__(self, name, x, y):
		self.name = name
		self.x = x
		self.y = y
	def __str__(self):
		return str(self.__dict__)
	def s(self):
		return self.name + ':' + str(self.o) + ':' + str(self.index)
	# def __lt__

cities = [
  City("Yliwwozno", 1944241, 1779385),
  City("Mvtgslk", 1879596, 1553922),
  City("Uofmawx", 1152595, 1562509),
  City("Yunqdy", 1613706, 1975460),
  City("Fkcgen", 1234647, 1934057),
  City("Fndmmblan", 1045563, 1005316),
  City("Sfnsujq", 1025187, 1410410),
  City("Nkldnptztf", 1918525, 1694368),
  City("Fiiygcqqu", 1095673, 1551616),
  City("Wcpjyrgfa", 1283213, 1882018),
  City("Eezjgthlyc", 1996189, 1046839),
  City("Qqtosml", 1931634, 1944504),
  City("Pkypsbqdx", 1422556, 1297516),
  City("Sgdrkka", 1949078, 1331674),
  City("Ikxleo", 1874469, 1909603),
  City("Odcqpi", 1859811, 1682204),
  City("Oomuexprq", 1184543, 1311404),
  City("Kokjvfx", 1176295, 1331290),
  City("Gqqnpu", 1940565, 1723396),
  City("Tuduiq", 1163367, 1657270),
  City("Uvkkfjzb", 1036252, 1467036),
  City("Ftdiawa", 1584163, 1213187),
  City("Syokbimj", 1793909, 1314500),
  City("Xvcvdlfx", 1428357, 1816814),
  City("Dkgukup", 1844660, 1662932),
  City("Qgwvdjnpk", 1499636, 1906360),
  City("Dblkzq", 1506724, 1482614),
  City("Znazdtbij", 1749251, 1955943),
  City("Cwqbys", 1748903, 1721758),
  City("Zkhgurfuvo", 1182528, 1177169),
  City("Molvhtpnl", 1193822, 1839384),
  City("Qmrreljf", 1259672, 1161558),
  City("Wzdckwjft", 1553027, 1027127),
  City("Qyxfdrhflz", 1244176, 1050412),
  City("Wiezdgw", 1105158, 1326527),
  City("Keprpqxw", 1642780, 1377656),
  City("Chalpzpvyz", 1207546, 1634370),
  City("Bkwvrdv", 1852435, 1708186),
  City("Ofkwdou", 1686122, 1098124),
  City("Twdarpkc", 1468018, 1705391),
  City("Ftnwdnqd", 1388837, 1843503),
  City("Qvexubm", 1154072, 1820222),
  City("Jewtalpqdy", 1964950, 1894825),
  City("Dxlpjfbd", 1142874, 1851633),
  City("Gxyubqpfxl", 1044750, 1155499),
  City("Wuhlalroz", 1748430, 1781991),
  City("Ucmntg", 1159012, 1663096),
  City("Syopyqm", 1716884, 1172567),
  City("Myqjbkpn", 1113689, 1285811),
  City("Vvhdzhiq", 1146868, 1804971),
  City("Zlfoxnjlic", 1626951, 1588239),
  City("Etzappmjhu", 1317452, 1555704),
  City("Pqzacp", 1534297, 1741236),
  City("Nveqkzpoix", 1342810, 1214249),
  City("Myackc", 1525979, 1102843),
  City("Xsjuqhhiap", 1732701, 1091212),
  City("Uunfdylpfs", 1449788, 1097409),
  City("Hpdasptycd", 1783429, 1383309),
  City("Mcinjws", 1697723, 1237763),
  City("Yzluia", 1957126, 1211321),
  City("Fmbcbb", 1726922, 1505344),
  City("Dstxcl", 1434022, 1464088),
  City("Vbumorc", 1153102, 1738574),
  City("Nlybddgmdp", 1892664, 1843137),
  City("Ysirwub", 1489937, 1017549),
  City("Kbtmzpwd", 1657579, 1279568),
  City("Uunhpqn", 1995281, 1799826),
  City("Gyyqtjlct", 1932421, 1859391),
  City("Cvbuegrxk", 1748408, 1137812),
  City("Omcnvxf", 1657563, 1406511),
  City("Uynimijxth", 1986760, 1119900),
  City("Oewoxv", 1908486, 1658964),
  City("Dbcbgp", 1458521, 1479055),
  City("Spolywmg", 1525948, 1150035),
  City("Obvcttr", 1701131, 1535862),
  City("Zxteeejiq", 1167209, 1004659),
  City("Tsapzdzdkm", 1726071, 1735051),
  City("Maxzjgjwoc", 1082607, 1397158),
  City("Qlmzkdwrt", 1445197, 1219771),
  City("Zktlltlod", 1163924, 1956041),
  City("Jgbaoiy", 1993886, 1393607),
  City("Sybjcj", 1568951, 1600653),
  City("Qbaemmkp", 1816972, 1323057),
  City("Rtouxlllko", 1859413, 1005653),
  City("Jcrdgyouvf", 1823856, 1546648),
  City("Wnywfg", 1258021, 1872559),
  City("Jwjhsxg", 1025935, 1110834),
  City("Pqtnstuvy", 1174370, 1525826),
  City("Bykils", 1570007, 1320107),
  City("Pwykmjhw", 1075715, 1853713),
  City("Iajfsuelga", 1640241, 1589312),
  City("Icndpnsrd", 1242884, 1450310),
  City("Uwxriz", 1162375, 1039179),
  City("Jmrdxfyjz", 1221129, 1951141),
  City("Wicmkrn", 1605964, 1944944),
  City("Pmkdqnbddf", 1468091, 1873505),
  City("Gaosddqmto", 1767238, 1450492),
  City("Slqsqhv", 1585908, 1408732),
  City("Iqzwxexzfi", 1437023, 1033323),
  City("Wnsfcbnon", 1468227, 1753776),
]