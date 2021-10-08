import java.util.*

public static class hw_08_2020182032_04 {
	public class City implements Comparable {
		public String name;
		public int x, y;
		City ( String name, int x, int y) {
			this.name = name;
			this.x = x;
			this.y = y;
		}
	}
	public City[] cities = new City[] {
		new City("Vyiaku", 1291462, 1388614), 
		new City("Zkvch", 1000032, 1388633), 
		new City("Hrrbu", 1291493, 1291498), 
		new City("Yjutwb", 1388656, 1291507), 
		new City("Gkczvyzsb", 1000078, 1388673), 
		new City("Ojwmvys", 1097255, 1097256), 
		new City("Hzckr", 1097271, 1291570), 
		new City("Vxxqjk", 1291581, 1388732), 
		new City("Eztjjs", 1291597, 1097297), 
		new City("Uyzucqjgzs", 1194475, 1000176), 
		new City("Bkmwce", 1291638, 1194491), 
		new City("Gmnpimohk", 1194519, 1097370), 
		new City("Nqbst", 1097378, 1388831), 
		new City("Slickhvgr", 1388858, 1388860), 
		new City("Wngriprm", 1291743, 1194595), 
		new City("Gyzjclr", 1000310, 1000312), 
		new City("Wybisc", 1291773, 1388925), 
		new City("Tcojtvbt", 1097491, 1194645), 
		new City("Zkphgbawx", 1097520, 1097521), 
		new City("Jkepogq", 1097529, 1388980), 
		new City("Rzakumc", 1000394, 1388997), 
		new City("Djdji", 1000408, 1194709), 
		new City("Ntiskuf", 1389021, 1097572), 
		new City("Dfhsb", 1389034, 1097588), 
		new City("Mqjonrug", 1389072, 1194776), 
		new City("Pasmuvjbwh", 1291948, 1194801), 
		new City("Kdmtnw", 1097664, 1389114), 
		new City("Dnqpozsyz", 1097704, 1194857), 
		new City("Fgqryuloy", 1389178, 1000580), 
		new City("Eaghqmoiua", 1292051, 1389202), 
		new City("Clkuocwang", 1000639, 1097790), 
		new City("Jhfghztk", 1000648, 1097802), 
		new City("Dgablviicy", 1389273, 1292124), 
		new City("Tlabji", 1292144, 1292148), 
		new City("Bsweufqtu", 1292173, 1195023), 
		new City("Jlbvpkrgy", 1389351, 1292205), 
		new City("Nxareco", 1195067, 1292221), 
		new City("Vdypyj", 1292235, 1292239), 
		new City("Prsnro", 1292265, 1195115), 
		new City("Fsdfgq", 1195131, 1195133), 
		new City("Yxyrs", 1000844, 1000845), 
		new City("Chpfbofqh", 1098043, 1195194), 
		new City("Galneib", 1389511, 1195213), 
		new City("Oygcnely", 1195233, 1389534), 
		new City("Cinzakgoyl", 1195253, 1098104), 
		new City("Fqkxod", 1098124, 1389574), 
		new City("Prlxlxzz", 1000996, 1292447), 
		new City("Myitjlbno", 1292463, 1389615), 
		new City("Xpabtngh", 1292481, 1098182), 
		new City("Mlybbyr", 1389648, 1389649), 
		new City("Fuoxtvda", 1292524, 1098226), 
		new City("Hgywazb", 1389694, 1098245), 
		new City("Lpgsjaupng", 1001141, 1292591), 
		new City("Kdvcehpk", 1195462, 1001166), 
		new City("Ytrgbnosyh", 1001192, 1098347), 
		new City("Hsttupyy", 1195530, 1389833), 
		new City("Fihbcv", 1001242, 1195541), 
		new City("Xwkdalg", 1001269, 1001270), 
		new City("Bkbuo", 1098429, 1292729), 
		new City("Ikrvs", 1098454, 1292761), 
		new City("Navpsbcfy", 1292783, 1098484), 
		new City("Kdfxyngx", 1292800, 1389948), 
		new City("Wxduor", 1389973, 1292824), 
		new City("Tfcavficoq", 1098550, 1195704), 
		new City("Uogfkdedcu", 1195723, 1195725), 
		new City("Kcucybbfgi", 1098597, 1292902), 
		new City("Xzsrcvklhs", 1001473, 1390072), 
		new City("Qjlxyaic", 1001493, 1390093), 
		new City("Qlvqpf", 1390107, 1098658), 
		new City("Xflfolov", 1390129, 1098683), 
		new City("Gidkdeiia", 1390151, 1098701), 
		new City("Xybzvxfhj", 1195870, 1098721), 
		new City("Moels", 1195896, 1098747), 
		new City("Fhyavpis", 1293062, 1195914), 
		new City("Hiemhjeh", 1293085, 1001635), 
		new City("Dgijwi", 1001656, 1195958), 
		new City("Czhrmpr", 1098832, 1001682), 
		new City("Vwfdizdjxi", 1390305, 1098856), 
		new City("Dpyqar", 1390317, 1098867), 
		new City("Shtmopi", 1390341, 1001745), 
		new City("Eridll", 1196054, 1001755), 
		new City("Yaiehzsrk", 1001787, 1196086), 
		new City("Qndmceoh", 1390410, 1390411), 
		new City("Lmxrcukkq", 1098988, 1293291), 
		new City("Hfbtfw", 1001856, 1390460), 
		new City("Dnzckddgy", 1196175, 1390479), 
		new City("Iwokwwja", 1001908, 1099061), 
		new City("Abacfdpi", 1001939, 1001937), 
		new City("Sbipzz", 1196251, 1099101), 
		new City("Vabzmfqo", 1001969, 1390569), 
		new City("Owofzghsb", 1099142, 1001996), 
		new City("Tufziqcj", 1196317, 1293471), 
		new City("Tbcohm", 1099192, 1390644), 
		new City("Vqsavjule", 1002068, 1002070), 
		new City("Ucbsqy", 1002088, 1002091), 
		new City("Bkpoqkc", 1293559, 1002113), 
		new City("Ktklutce", 1002135, 1002136), 
		new City("Nyiibs", 1002146, 1196456), 
		new City("Xcbkyuzaq", 1099334, 1390787), 
		new City("Hrcxrizgg", 1196525, 1196528), 
	}
	public static void main(String[] args) {
		//System.out.println("Hello~~~");
		new hw_08_2020182032_04().main();
	}

	public void main() {
		Arrays.sort(cities, new Comparable<City>() {
			public int compare(City c1, City c2) {
				return c1.x - c2.x;
			}
		});
		for ( City c: cities) {
			System.out.println(c.name + ' ' + c.x + ', ' + c.y);
		}
	}
}