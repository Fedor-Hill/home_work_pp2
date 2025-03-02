a = tuple([True, True, True, False])

def check_tuple_for_true(t: tuple) -> bool:
    return t.count(False) == 0

if check_tuple_for_true(a):
    print(True)
else:
    print(False)
