def average(iterable_object):
    try:
        sum_average = sum(iterable_object) / len(iterable_object)
        return sum_average

    except:
        if len(iterable_object) == 0:
            raise Exception("empty argument")
        else:
            raise Exception("bad argument")


def test_average(arg):
    try:
        print(arg, ': ', end = '')
        print(average(arg))

    except Exception as e:
        print(e)


test_average([])
# [] : empty argument

test_average(['a', 'b'])
# ['a', 'b'] : bad argument

test_average((1, 2, 3))
# (1, 2, 3) : 2.0

test_average([1])
# [1] : 1.0

test_average([1.5, 2.5])
# [1.5, 2.5] : 2.0

test_average({1, 2, 2})
# {1, 2} : 1.5

test_average(range(1, 10))
# range(1, 10) : 5.0
