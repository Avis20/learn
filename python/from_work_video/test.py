
class BaseClass:

    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        print("\t-->", cls)
        print("\t-->", kwargs)
        print("\t-->", args)
        return super().__new__(cls)

    def __init__(self, name):
        print("__init__ called")
        self.name = name


class ChildClass(BaseClass):

    @classmethod
    def construct(cls, name):
        print("Class =", cls, "; Name =", name)
        return cls(name)


if __name__ == '__main__':
    object_1 = ChildClass('Hello')
    print('type=[', type(object_1), ']; object=[', object_1, ']', sep='')

