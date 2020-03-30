# goldbach

Find minimum set of odd numbers to satisfy Solaz conjecture:
every even integer greater than two is the sum of two odd numbers from the minimum set.

Implementation use: combinations function from itertools
This method takes a list and return a list of tuples with all possible combinations of length r

Running Example wit N=64:
~/repository/goldbach$ python goldbach.py 64
find minimum odd set for 64
check 496 odd sets with 2 odd numbers
check 5456 odd sets with 3 odd numbers
check 46376 odd sets with 4 odd numbers
check 324632 odd sets with 5 odd numbers
check 1947792 odd sets with 6 odd numbers
check 10295472 odd sets with 7 odd numbers
check 48903492 odd sets with 8 odd numbers
check 211915132 odd sets with 9 odd numbers
minimum set length: 9 
 [3, 5, 7, 9, 17, 25, 29, 31, 35] 
6=3+3
8=3+5
10=5+5
12=3+9
14=7+7
16=7+9
18=9+9
20=3+17
22=5+17
24=7+17
26=9+17
28=3+25
30=5+25
32=3+29
34=17+17
36=5+31
38=3+35
40=5+35
42=7+35
44=9+35
46=17+29
48=17+31
50=25+25
52=17+35
54=25+29
56=25+31
58=29+29
60=25+35
62=31+31
64=29+35
