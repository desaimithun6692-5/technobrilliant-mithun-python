# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     pass
#
#
# class D(A):
#     pass


class A:
    pass


class B(A):
    pass


class C(B):
    pass


class A1:
    pass


class A2:
    pass


class B(A1, A2):
    pass

class C(B):
    pass