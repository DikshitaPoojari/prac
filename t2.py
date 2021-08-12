def test(x):
    print("test1")
    print("test2")
    print("test3")
    return x

import pdb
pdb.set_trace()
data = test(10)
print(data)
