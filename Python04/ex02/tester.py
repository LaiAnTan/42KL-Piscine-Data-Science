from callLimit import callLimit


@callLimit(3)
def f():
    print("f()")
# this is actually callLimit(3)(f), to call it we do callLimit(3)(f)()
# we have wrapped f in limit_function and wrapped that in callLimit


@callLimit(1)
def g():
    print("g()")


for i in range(3):
    f()
    g()
