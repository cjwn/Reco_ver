
class Root:
    def __init__(self):
        self.x = 'it\'s attribute'

    def fun(self):
        print(self.x)
        print('it\'s method')

class A(Root):
    def __init__(self):
        super(A, self).__init__()
        print('实例化执行')

test = A()
test.fun()
print(test.x)

