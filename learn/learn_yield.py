def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)
g = foo()
print(next(g))
print("*"*20)
print(g.send(7))


# def tree_iter(it):
#
# yield from tree_iter(it.left)
# yield it.val
#
# yield from tree_iter(it.right)