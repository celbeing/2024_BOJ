# 18137: 나이트의 경로
import sys
input = sys.stdin.readline
def solution():
    k = []
    d = [(-1, -2), (-2, -1), (1, -2), (-2, 1), (2, -1), (-1, 2), (2, 1), (1, 2)]
    board = [[0] * 10000 for _ in range(10000)]
    def cor(x, y):
        t = x + y
        return (t - 1) * (t - 2) // 2 + y

    board[1][1] = 1
    k.append(1)
    x, y = 1, 1
    while True:
        for i in range(8):
            nx, ny = x + d[i][0], y + d[i][1]
            if nx <= 0 or ny <= 0 or board[nx][ny]: continue
            k.append(cor(nx, ny))
            board[nx][ny] = 1
            x, y = nx, ny
            break
solution()

'''
import sys
input = sys.stdin.readline
def solution():
    k = [ 1, 8, 6, 2, 12, 9, 4, 3, 13, 7, 5, 10, 26, 18, 11, 30, 24, 16, 38, 31, 22, 17, 25, 20, 28, 34, 14, 21, 43, 33, 27, 19, 15, 35, 42, 32, 23, 29, 39, 47, 56, 69, 37, 48, 40, 51, 60, 70, 57, 67, 81, 46, 58, 49, 41, 52, 44, 55, 64, 36, 65, 53, 45, 76, 63, 54, 66, 103, 88, 74, 61, 71, 82, 68, 79, 94, 107, 121, 139, 92, 80, 95, 83, 72, 59, 50, 62, 75, 86, 98, 111, 125, 108, 122, 137, 156, 106, 93, 109, 96, 84, 73, 87, 99, 112, 126, 141, 123, 138, 154, 174, 157, 177, 124, 110, 97, 85, 100, 113, 127, 142, 158, 175, 155, 172, 193, 212, 232, 256, 191, 173, 194, 176, 159, 140, 195, 214, 192, 211, 234, 255, 277, 303, 233, 213, 236, 216, 197, 179, 162, 143, 128, 114, 101, 89, 78, 118, 77, 91, 134, 90, 102, 115, 129, 144, 160, 180, 163, 147, 132, 150, 104, 117, 131, 146, 165, 116, 130, 145, 161, 178, 196, 215, 235, 259, 238, 218, 199, 181, 164, 148, 133, 119, 136, 151, 105, 152, 168, 149, 204, 183, 166, 186, 169, 120, 170, 187, 135, 153, 208, 190, 251, 189, 207, 226, 167, 184, 202, 221, 241, 262, 198, 217, 237, 258, 280, 306, 283, 261, 240, 220, 201, 223, 243, 182, 200, 219, 239, 260, 282, 257, 279, 254, 327, 352, 381, 301, 278, 304, 281, 307, 284, 310, 287, 265, 244, 224, 205, 227, 247, 185, 203, 222, 242, 263, 285, 308, 332, 305, 329, 302, 326, 354, 380, 407, 438, 353, 328, 356, 331, 359, 334, 362, 286, 264, 289, 267, 246, 270, 206, 188, 171, 229, 210, 274, 209, 228, 248, 225, 245, 266, 288, 311, 335, 360, 386, 357, 383, 410, 441, 355, 330, 358, 333, 309, 336, 312, 339, 315, 292, 318, 295, 273, 249, 319, 293, 268, 290, 313, 337, 365, 340, 316, 343, 269, 291, 314, 338, 363, 389, 416, 444, 413, 504, 412, 382, 409, 379, 467, 497, 531, 436, 408, 439, 411, 384, 414, 387, 361, 390, 364, 393, 367, 342, 370, 294, 272, 297, 230, 250, 271, 296, 322, 252, 276, 298, 231, 299, 325, 349, 275, 300, 323, 253, 324, 348, 321, 345, 373, 399, 320, 344, 317, 341, 366, 392, 419, 447, 476, 388, 415, 385, 473, 503, 470, 500, 534, 440, 469, 437, 466, 499, 530, 562, 598, 498, 468, 501, 471, 442, 474, 445, 417, 448, 420, 451, 423, 396, 426, 454, 368, 394, 421, 391, 418, 446, 475, 443, 472, 502, 533, 565, 601, 568, 536, 505, 539, 508, 478, 449, 481, 452, 424, 397, 371, 346, 374, 400, 427, 455, 369, 395, 422, 450, 479, 509, 540, 506, 537, 569, 602, 566, 599, 563, 596, 633, 529, 564, 532, 567, 535, 570, 538, 507, 477, 510, 480, 513, 483, 516, 425, 398, 372, 347, 375, 350, 378, 404, 431, 401, 428, 456, 485, 453, 482, 512, 543, 575, 608, 572, 605, 639, 674, 636, 671, 707, 597, 631, 669, 634, 600, 637, 603, 640, 606, 573, 541, 576, 544, 579, 547, 582, 484, 514, 545, 511, 542, 574, 607, 571, 604, 638, 673, 635, 670, 632, 667, 706, 743, 781, 823, 704, 668, 783, 742, 705, 745, 708, 672, 711, 675, 714, 678, 643, 609, 646, 612, 649, 546, 515, 549, 518, 488, 459, 491, 402, 376, 351, 433, 403, 377, 406, 494, 405, 432, 460, 429, 457, 486, 519, 489, 522, 430, 458, 487, 517, 548, 580, 613, 577, 610, 644, 679, 641, 676, 712, 749, 709, 746, 784, 826, 787, 829, 710, 747, 785, 744, 782, 821, 864, 824, 867, 827, 788, 750, 713, 677, 642, 680, 645, 611, 578, 614, 581, 617, 584, 552, 521, 555, 461, 490, 520, 551, 583, 616, 650, 685, 647, 682, 718, 755, 715, 752, 790, 832, 793, 835, 716, 753, 791, 830, 870, 748, 786, 825, 865, 822, 862, 906, 948, 991, 1038, 904, 863, 907, 866, 910, 869, 913, 789, 751, 792, 754, 717, 681, 720, 684, 723, 687, 652, 615, 724, 688, 653, 550, 585, 553, 588, 556, 462, 434, 465, 559, 464, 493, 523, 554, 586, 619, 656, 622, 589, 492, 463, 435, 526, 496, 593, 495, 525, 625, 524, 558, 527, 561, 664, 560, 592, 557, 660, 623, 587, 620, 654, 689, 651, 686, 648, 683, 719, 756, 794, 833, 873, 914, 956, 828, 868, 909, 951, 994, 1041, 908, 950, 905, 947, 993, 1037, 1082, 1131, 992, 949, 995, 952, 998, 955, 1001, 871, 831, 874, 834, 795, 757, 798, 760, 801, 763, 726, 690, 655, 618, 727, 691, 730, 621, 658, 624, 591, 627, 594, 630, 739, 629, 528, 628, 595, 701, 663, 626, 590, 696, 661, 699, 735, 772, 659, 694, 733, 697, 662, 700, 665, 703, 818, 702, 738, 775, 813, 698, 734, 695, 657, 692, 728, 765, 725, 762, 722, 759, 797, 836, 876, 917, 959, 1002, 872, 916, 875, 919, 878, 838, 796, 758, 721, 761, 799, 841, 802, 764, 805, 767, 808, 693, 729, 766, 804, 843, 883, 840, 880, 837, 877, 918, 960, 915, 957, 912, 954, 997, 1044, 911, 953, 996, 1040, 1085, 1134, 1088, 1043, 999, 1046, 1091, 1137, 1184, 1042, 1087, 1039, 1084, 1036, 1178, 1226, 1278, 1129, 1083, 1132, 1086, 1135, 1089, 1138, 1092, 1047, 1000, 1139, 1090, 1045, 1093, 1048, 1004, 958, 1094, 1049, 1005, 962, 920, 879, 839, 800, 842, 803, 845, 806, 768, 731, 771, 809, 848, 888, 929, 885, 926, 882, 923, 965, 1008, 1052, 1097, 961, 1007, 964, 922, 881, 925, 884, 844, 887, 847, 890, 769, 732, 850, 811, 770, 891, 851, 812, 774, 737, 777, 740, 780, 901, 779, 666, 778, 741, 859, 817, 776, 736, 773, 814, 853, 893, 934, 810, 849, 807, 846, 886, 927, 969, 924, 966, 921, 963, 1006, 1050, 1003, 1142, 1096, 1051, 1099, 1054, 1010, 967, 1013, 970, 928, 973, 931, 976, 1019, 889, 930, 972, 1015, 1059, 1012, 1056, 1009, 1053, 1098, 1144, 1095, 1141, 1188, 1236, 1185, 1233, 1182, 1230, 1179, 1227, 1276, 1329, 1177, 1130, 1180, 1133, 1183, 1136, 1186, 1234, 1283, 1231, 1280, 1228, 1277, 1327, 1381, 1330, 1384, 1229, 1181, 1232, 1281, 1331, 1382, 1328, 1379, 1434, 1487, 1541, 1599, 1432, 1380, 1435, 1383, 1332, 1279, 1436, 1489, 1433, 1486, 1543, 1598, 1654, 1714, 1542, 1488, 1545, 1491, 1438, 1386, 1335, 1282, 1439, 1387, 1333, 1493, 1437, 1385, 1334, 1284, 1235, 1187, 1140, 1190, 1143, 1193, 1146, 1100, 1055, 1011, 968, 1014, 971, 1017, 974, 932, 977, 935, 894, 854, 815, 857, 897, 938, 980, 852, 892, 933, 975, 1018, 1062, 1107, 1153, 1104, 1150, 1101, 1147, 1194, 1242, 1191, 1239, 1288, 1338, 1285, 1442, 1390, 1336, 1286, 1237, 1189, 1240, 1192, 1145, 1195, 1148, 1102, 1057, 1105, 1060, 1016, 1063, 1108, 1154, 1201, 1058, 1103, 1149, 1196, 1244, 1293, 1241, 1290, 1238, 1287, 1337, 1388, 1440, 1496, 1443, 1391, 1340, 1394, 1343, 1397, 1243, 1292, 1342, 1289, 1339, 1393, 1445, 1498, 1552, 1389, 1441, 1494, 1548, 1603, 1659, 1490, 1544, 1602, 1547, 1605, 1550, 1608, 1553, 1499, 1446, 1502, 1341, 1291, 1344, 1294, 1245, 1197, 1248, 1200, 1251, 1106, 1061, 1109, 1064, 1020, 1067, 1023, 1070, 936, 895, 855, 816, 858, 819, 861, 988, 860, 900, 941, 983, 856, 896, 937, 979, 1022, 1066, 1111, 1157, 1204, 1252, 1301, 1152, 1199, 1247, 1296, 1346, 1400, 1246, 1198, 1151, 1299, 1250, 1202, 1155, 1205, 1158, 1112, 1161, 1021, 978, 1024, 981, 939, 898, 942, 984, 1027, 1071, 1116, 1068, 1113, 1065, 1110, 1156, 1203, 1254, 1206, 1159, 1209, 1162, 1212, 1069, 1025, 982, 940, 899, 943, 902, 946, 1079, 945, 820, 944, 903, 1033, 987, 1030, 1074, 1119, 1165, 1026, 1073, 1029, 986, 1032, 989, 1035, 1174, 1034, 1078, 1031, 985, 1028, 1072, 1117, 1163, 1114, 1160, 1207, 1255, 1304, 1354, 1405, 1351, 1298, 1249, 1403, 1349, 1509, 1348, 1295, 1345, 1396, 1448, 1501, 1555, 1392, 1444, 1497, 1551, 1606, 1662, 1492, 1546, 1601, 1657, 1717, 1660, 1604, 1549, 1495, 1664, 1721, 1661, 1718, 1658, 1715, 1655, 1712, 1773, 1597, 1656, 1600, 1775, 1834, 1772, 1831, 1894, 1713, 1771, 1833, 1774, 1716, 1777, 1719, 1780, 1722, 1665, 1609, 1554, 1500, 1447, 1395, 1450, 1398, 1347, 1297, 1350, 1300, 1353, 1303, 1356, 1306, 1257, 1309, 1260, 1115, 1164, 1118, 1167, 1121, 1076, 1124, 1170, 1217, 1075, 1120, 1166, 1213, 1261, 1210, 1258, 1307, 1357, 1408, 1253, 1302, 1352, 1406, 1355, 1305, 1256, 1208, 1259, 1211, 1262, 1214, 1265, 1314, 1364, 1311, 1361, 1308, 1358, 1409, 1461, 1514, 1458, 1511, 1455, 1508, 1452, 1505, 1449, 1615, 1557, 1503, 1560, 1506, 1453, 1401, 1456, 1404, 1459, 1407, 1462, 1410, 1359, 1413, 1362, 1312, 1263, 1215, 1168, 1122, 1077, 1125, 1080, 1128, 1273, 1127, 990, 1126, 1081, 1223, 1173, 1220, 1268, 1123, 1169, 1216, 1264, 1313, 1363, 1310, 1360, 1411, 1463, 1516, 1460, 1513, 1457, 1402, 1454, 1399, 1451, 1504, 1558, 1613, 1669, 1610, 1666, 1607, 1663, 1720, 1778, 1837, 1897, 1958, 2020, 1832, 1892, 1956, 1895, 1835, 1776, 1838, 1779, 1841, 1782, 1724, 1667, 1611, 1556, 1614, 1559, 1617, 1562, 1620, 1565, 1623, 1568, 1626, 1571, 1517, 1464, 1412, 1467, 1415, 1470, 1418, 1367, 1317, 1370, 1218, 1171, 1221, 1269, 1318, 1266, 1315, 1365, 1416, 1468, 1521, 1465, 1518, 1572, 1515, 1569, 1512, 1566, 1621, 1563, 1618, 1674, 1731, 1671, 1612, 1668, 1725, 1783, 1842, 1902, 1839, 1899, 1836, 1896, 1957, 1893, 1954, 2019, 2082, 2146, 2214, 2017, 1955, 2148, 2081, 2018, 2084, 2021, 1959, 1898, 1962, 1901, 1965, 1781, 1723, 1784, 1726, 1787, 1729, 1672, 1616, 1561, 1507, 1564, 1510, 1567, 1622, 1678, 1619, 1675, 1732, 1790, 1849, 1670, 1727, 1785, 1844, 1904, 1968, 1907, 1847, 1788, 1730, 1673, 1733, 1676, 1736, 1679, 1739, 1682, 1742, 1570, 1625, 1681, 1738, 1796, 1735, 1793, 1852, 1912, 1973, 1789, 1728, 1786, 1845, 1905, 1966, 2028, 1840, 1900, 1961, 2023, 2086, 2150, 2083, 2147, 2212, 2281, 2215, 2284, 2085, 2022, 1960, 2025, 1963, 2156, 2089, 2026, 1964, 1903, 1843, 1906, 1846, 1909, 1970, 2032, 1967, 2029, 2092, 2159, 2095, 2162, 1969, 1908, 1848, 1911, 1851, 1792, 1734, 1677, 1737, 1680, 1624, 1683, 1627, 1686, 1630, 1575, 1633, 1466, 1414, 1469, 1417, 1366, 1316, 1267, 1219, 1172, 1222, 1175, 1225, 1376, 1224, 1272, 1321, 1371, 1422, 1368, 1419, 1471, 1524, 1578, 1636, 1581, 1527, 1474, 1530, 1369, 1319, 1270, 1322, 1372, 1423, 1475, 1420, 1472, 1525, 1579, 1522, 1576, 1519, 1573, 1628, 1684, 1741, 1799, 1858, 1918, 1855, 1915, 1976, 1791, 1850, 1910, 1971, 2033, 2096, 2030, 2093, 2027, 2090, 2024, 2087, 2151, 2216, 2282, 2213, 2279, 2349, 2417, 2486, 2559, 2347, 2280, 2350, 2283, 2217, 2149, 2351, 2419, 2348, 2416, 2488, 2558, 2629, 2704, 2487, 2418, 2490, 2421, 2353, 2286, 2220, 2152, 2088, 2155, 2091, 2158, 2094, 2031, 2097, 2034, 1972, 2037, 1975, 1914, 1854, 1795, 1857, 1798, 1740, 1801, 1743, 1804, 1629, 1574, 1520, 1577, 1523, 1580, 1526, 1473, 1421, 1476, 1424, 1373, 1320, 1271, 1323, 1274, 1326, 1483, 1325, 1176, 1324, 1275, 1429, 1375, 1426, 1478, 1531, 1585, 1528, 1582, 1637, 1693, 1634, 1690, 1631, 1687, 1744, 1802, 1861, 1921, 1982, 1797, 1856, 1794, 1853, 1913, 1974, 2036, 2099, 2163, 2228, 2160, 2225, 2157, 2222, 2154, 2219, 2285, 2352, 2420, 2489, 2562, 2492, 2423, 2218, 2153, 2221, 2287, 2354, 2422, 2491, 2561, 2632, 2707, 2635, 2564, 2494, 2425, 2357, 2290, 2224, 2293, 2227, 2296, 2230, 2165, 2098, 2035, 2101, 2038, 2104, 2041, 1979, 2044, 2107, 1916, 1977, 2039, 2102, 2166, 2231, 2297, 2364, 2161, 2226, 2292, 2223, 2289, 2356, 2424, 2493, 2563, 2634, 2560, 2631, 2557, 2777, 2851, 2929, 2702, 2630, 2705, 2633, 2708, 2636, 2565, 2495, 2426, 2355, 2288, 2358, 2291, 2361, 2294, 2502, 2430, 2359, 2427, 2496, 2566, 2637, 2709, 2782, 2706, 2779, 2703, 2776, 2853, 2928, 3004, 3084, 2852, 2778, 2855, 2781, 2858, 2784, 2711, 2639, 2568, 2498, 2429, 2501, 2432, 2504, 2295, 2229, 2164, 2100, 2167, 2103, 2040, 1978, 1917, 1981, 1920, 1860, 1923, 1863, 1685, 1745, 1688, 1632, 1691, 1635, 1694, 1638, 1583, 1529, 1586, 1532, 1479, 1427, 1482, 1430, 1485, 1538, 1377, 1428, 1374, 1425, 1477, 1533, 1480, 1536, 1590, 1645, 1587, 1642, 1584, 1639, 1695, 1752, 1692, 1749, 1689, 1746, 1807, 1866, 1926, 1987, 1803, 1862, 1800, 1859, 1919, 1980, 2042, 2105, 2169, 2234, 2300, 2367, 2435, 2507, 2298, 2232, 2301, 2235, 2170, 2106, 2043, 2109, 2046, 1984, 2049, 2112, 1922, 1983, 2045, 2108, 2172, 2237, 2303, 2370, 2168, 2233, 2299, 2366, 2434, 2363, 2431, 2360, 2428, 2497, 2567, 2638, 2710, 2783, 2857, 2780, 2854, 2932, 3008, 3085, 3005, 3082, 3163, 2927, 3006, 2930, 3009, 2933, 3012, 2936, 2861, 2787, 2714, 2642, 2571, 2645, 2574, 2362, 2433, 2365, 2436, 2368, 2439, 2371, 2304, 2238, 2173, 2241, 2176, 2244, 2047, 1985, 1924, 1864, 1805, 1747, 1808, 1750, 1811, 1753, 1696, 1640, 1699, 1643, 1588, 1534, 1481, 1537, 1484, 1540, 1594, 1431, 1595, 1650, 1592, 1535, 1589, 1644, 1700, 1641, 1697, 1754, 1812, 1751, 1809, 1748, 1806, 1865, 1925, 1986, 2048, 2111, 2175, 2240, 2306, 2373, 2171, 2236, 2302, 2369, 2437, 2506, 2576, 2503, 2573, 2500, 2570, 2641, 2713, 2786, 2860, 2935, 3011, 3088, 2856, 2931, 3007, 3087, 3010, 2934, 2859, 2785, 2712, 2640, 2569, 2499, 2572, 2643, 2715, 2788, 2862, 2937, 3013, 3090, 3168, 3247, 3165, 3244, 3162, 3241, 3324, 3083, 3161, 3243, 3164, 3086, 3167, 3089, 3170, 3092, 3015, 2939, 2864, 2790, 2717, 2793, 2720, 2648, 2577, 2651, 2580, 2510, 2438, 2652, 2578, 2505, 2575, 2646, 2718, 2791, 2865, 2940, 3016, 3093, 3171, 3250, 3330, 3411, 3166, 3245, 3325, 3242, 3322, 3406, 3488, 3571, 3658, 3404, 3323, 3407, 3326, 3246, 3329, 3249, 3332, 3091, 3014, 2938, 2863, 2789, 2716, 2644, 2719, 2647, 2722, 2650, 2579, 2509, 2440, 2372, 2305, 2239, 2174, 2110, 2177, 2113, 2050, 1988, 1927, 1867, 1930, 1870, 1933, 1873, 1814, 1756, 1817, 1759, 1702, 1646, 1591, 1649, 1705, 1762, 1820, 1879, 1701, 1758, 1698, 1755, 1813, 1872, 1810, 1869, 1929, 1990, 2052, 2115, 2179, 2247, 2051, 1989, 1928, 1868, 1931, 1871, 1934, 1874, 1815, 1757, 1818, 1760, 1703, 1647, 1706, 1763, 1821, 1880, 1940, 1877, 1937, 1998, 2060, 1995, 2057, 1992, 2054, 2117, 2181, 2114, 2178, 2243, 2309, 2376, 2444, 2513, 2441, 2655, 2581, 2508, 2725, 2653, 2582, 2512, 2443, 2375, 2308, 2242, 2311, 2245, 2180, 2116, 2053, 1991, 2056, 1994, 2059, 1997, 1936, 1876, 1939, 2000, 1816, 1875, 1935, 1996, 1932, 1993, 2055, 2118, 2182, 2250, 2185, 2121, 2058, 2124, 2061, 1999, 1938, 1878, 1819, 1761, 1704, 1648, 1593, 1539, 1378 ]
    print(k[int(input())])
solution()
'''