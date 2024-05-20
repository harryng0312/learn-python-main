class A(object):
    def __init__(self):
        print("-> A")
        super(A, self).__init__()
        print("<- A")

class B(A):
    def __init__(self):
        print("-> B")
        super(B, self).__init__()
        print("<- B")

class C(A):
    def __init__(self):
        print("-> C")
        # Use super here, instead of explicit calls to __init__
        super(C, self).__init__()
        print("<- C")

class D(B,C):
    def __init__(self):
        print("-> D")
        # Use super here, instead of explicit calls to __init__
        super(D, self).__init__()
        print("<- D")

if __name__ == "__main__":
    D()