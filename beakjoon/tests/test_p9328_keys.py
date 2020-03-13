from beakjoon.p9328_keys import main
from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
3
5 17
*****************
.............**$*
*B*A*P*C**X*Y*.X.
*y*x*a*p**$*$**$*
*****************
cz
5 11
*.*********
*...*...*x*
*X*.*.*.*.*
*$*...*...*
***********
0
7 7
*ABCDE*
X.....F
W.$$$.G
V.$$$.H
U.$$$.J
T.....K
*SQPML*
irony    
    """.strip()
    expected = """
3
1
0    
""".strip()
    assert get_output_with_stdin(main, in_str) == expected


