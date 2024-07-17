def foo(n):
    for i in range(n):
        print("Hi")


foo(5)
print("------------")


def rec_foo(n):
    if n > 0:
        print("Hi")
        rec_foo(n-1)


rec_foo(5)
