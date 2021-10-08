#include <stdio.h>
#include <stdlib.h>

typedef struct _City {
	char name[16];
	int x, y;
} City;

City cities[] = {
	{ "Vyiaku", 1291462, 1388614 },
	{ "Zkvch", 1000032, 1388633 },
	{ "Hrrbu", 1291493, 1291498 },
	{ "Yjutwb", 1388656, 1291507 },
	{ "Gkczvyzsb", 1000078, 1388673 },
	{ "Ojwmvys", 1097255, 1097256 },
	{ "Hzckr", 1097271, 1291570 },
	{ "Vxxqjk", 1291581, 1388732 },
	{ "Eztjjs", 1291597, 1097297 },
	{ "Uyzucqjgzs", 1194475, 1000176 },
	{ "Bkmwce", 1291638, 1194491 },
	{ "Gmnpimohk", 1194519, 1097370 },
	{ "Nqbst", 1097378, 1388831 },
	{ "Slickhvgr", 1388858, 1388860 },
	{ "Wngriprm", 1291743, 1194595 },
	{ "Gyzjclr", 1000310, 1000312 },
	{ "Wybisc", 1291773, 1388925 },
	{ "Tcojtvbt", 1097491, 1194645 },
	{ "Zkphgbawx", 1097520, 1097521 },
	{ "Jkepogq", 1097529, 1388980 },
	{ "Rzakumc", 1000394, 1388997 },
	{ "Djdji", 1000408, 1194709 },
	{ "Ntiskuf", 1389021, 1097572 },
	{ "Dfhsb", 1389034, 1097588 },
	{ "Mqjonrug", 1389072, 1194776 },
	{ "Pasmuvjbwh", 1291948, 1194801 },
	{ "Kdmtnw", 1097664, 1389114 },
	{ "Dnqpozsyz", 1097704, 1194857 },
	{ "Fgqryuloy", 1389178, 1000580 },
	{ "Eaghqmoiua", 1292051, 1389202 },
	{ "Clkuocwang", 1000639, 1097790 },
	{ "Jhfghztk", 1000648, 1097802 },
	{ "Dgablviicy", 1389273, 1292124 },
	{ "Tlabji", 1292144, 1292148 },
	{ "Bsweufqtu", 1292173, 1195023 },
	{ "Jlbvpkrgy", 1389351, 1292205 },
	{ "Nxareco", 1195067, 1292221 },
	{ "Vdypyj", 1292235, 1292239 },
	{ "Prsnro", 1292265, 1195115 },
	{ "Fsdfgq", 1195131, 1195133 },
	{ "Yxyrs", 1000844, 1000845 },
	{ "Chpfbofqh", 1098043, 1195194 },
	{ "Galneib", 1389511, 1195213 },
	{ "Oygcnely", 1195233, 1389534 },
	{ "Cinzakgoyl", 1195253, 1098104 },
	{ "Fqkxod", 1098124, 1389574 },
	{ "Prlxlxzz", 1000996, 1292447 },
	{ "Myitjlbno", 1292463, 1389615 },
	{ "Xpabtngh", 1292481, 1098182 },
	{ "Mlybbyr", 1389648, 1389649 },
	{ "Fuoxtvda", 1292524, 1098226 },
	{ "Hgywazb", 1389694, 1098245 },
	{ "Lpgsjaupng", 1001141, 1292591 },
	{ "Kdvcehpk", 1195462, 1001166 },
	{ "Ytrgbnosyh", 1001192, 1098347 },
	{ "Hsttupyy", 1195530, 1389833 },
	{ "Fihbcv", 1001242, 1195541 },
	{ "Xwkdalg", 1001269, 1001270 },
	{ "Bkbuo", 1098429, 1292729 },
	{ "Ikrvs", 1098454, 1292761 },
	{ "Navpsbcfy", 1292783, 1098484 },
	{ "Kdfxyngx", 1292800, 1389948 },
	{ "Wxduor", 1389973, 1292824 },
	{ "Tfcavficoq", 1098550, 1195704 },
	{ "Uogfkdedcu", 1195723, 1195725 },
	{ "Kcucybbfgi", 1098597, 1292902 },
	{ "Xzsrcvklhs", 1001473, 1390072 },
	{ "Qjlxyaic", 1001493, 1390093 },
	{ "Qlvqpf", 1390107, 1098658 },
	{ "Xflfolov", 1390129, 1098683 },
	{ "Gidkdeiia", 1390151, 1098701 },
	{ "Xybzvxfhj", 1195870, 1098721 },
	{ "Moels", 1195896, 1098747 },
	{ "Fhyavpis", 1293062, 1195914 },
	{ "Hiemhjeh", 1293085, 1001635 },
	{ "Dgijwi", 1001656, 1195958 },
	{ "Czhrmpr", 1098832, 1001682 },
	{ "Vwfdizdjxi", 1390305, 1098856 },
	{ "Dpyqar", 1390317, 1098867 },
	{ "Shtmopi", 1390341, 1001745 },
	{ "Eridll", 1196054, 1001755 },
	{ "Yaiehzsrk", 1001787, 1196086 },
	{ "Qndmceoh", 1390410, 1390411 },
	{ "Lmxrcukkq", 1098988, 1293291 },
	{ "Hfbtfw", 1001856, 1390460 },
	{ "Dnzckddgy", 1196175, 1390479 },
	{ "Iwokwwja", 1001908, 1099061 },
	{ "Abacfdpi", 1001939, 1001937 },
	{ "Sbipzz", 1196251, 1099101 },
	{ "Vabzmfqo", 1001969, 1390569 },
	{ "Owofzghsb", 1099142, 1001996 },
	{ "Tufziqcj", 1196317, 1293471 },
	{ "Tbcohm", 1099192, 1390644 },
	{ "Vqsavjule", 1002068, 1002070 },
	{ "Ucbsqy", 1002088, 1002091 },
	{ "Bkpoqkc", 1293559, 1002113 },
	{ "Ktklutce", 1002135, 1002136 },
	{ "Nyiibs", 1002146, 1196456 },
	{ "Xcbkyuzaq", 1099334, 1390787 },
	{ "Hrcxrizgg", 1196525, 1196528 }
};

int city_cmp(void* a, void* b)
{
	City* c1 = (City*)a;
	City* c2 = (City*)b;
	return c1->x - c2->x;
}

int main(void)
{
	qsort(cities, sizeof(cities) / sizeof(cities[0]), sizeof(cities[0]), city_cmp);
	for (int i = 0; i < sizeof(cities) / sizeof(cities[0]); i++) {
		printf("%-12s %3d, %3d\n", cities[i].name, cities[i].x, cities[i].y);
	}
	return 0;
}