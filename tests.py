import betterpython

assert ~'Yes' == 'seY'
assert ~[1,2,3] == [3,2,1]
assert ~('x','y') == ('y','x')
assert ~{0:1} == {1:0}
assert 'test' - 't' == 'es'
assert [1,2,3,1,4,3] - (1,3) == [2,4]