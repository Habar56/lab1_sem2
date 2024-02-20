d = {1:"aaaa", 2:"bbbb", 3:"cccc"}
d1 = {}
def inverce(dict):
    for k, v in dict.items():
        print(k, v)
        d1 [v] = k
    print(d1)
inverce(d)