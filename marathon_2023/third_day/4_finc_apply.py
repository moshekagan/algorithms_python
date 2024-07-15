def my_apply(func, args):
    func(*args)


def print_me(data, a):
    print(f"the data is: {data}")
    print(a)


my_apply(print_me, args=[[1, 2, 3, 4], "aaa"])
