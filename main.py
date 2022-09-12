import numpy as np

def test(x : float):
    return x*x + 2

class FractionalLaplacian(object):
    def __init__(self, h, alpha):
        self.h = h
        self.alpha = alpha

    def __call__(self, function : callable):
        return lambda x : self.__tail(function)(x) + self.__singular(function)(x)

    def __tail(self,function):
        return lambda x: function(x+0)

    def __singular(self, function):
        return lambda x: function(x + 1) + function(x + 2)

if __name__ == "__main__":
    operator = FractionalLaplacian(h=0.1, alpha=0.5)
    g = operator(test)
    print(g(1))