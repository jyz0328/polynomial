class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    #part c Write an `evaluate` method to each class that can evaluate the polynomial for a given value of `X`.
    def evaluate(self, value):
        return value
    
class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)
    
    def evaluate(self, value):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self, value):
        return self.p1.evaluate(value) + self.p2.evaluate(value)
    
#part b add class Sub
class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    
    def evaluate(self, value):
        return self.p1.evaluate(value) - self.p2.evaluate(value)
    
#partb :add class divide and modify Mul class since Sub situation need to be considered
'''class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
        '''   
    
class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        p1_repr = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub)) else repr(self.p1)
        p2_repr = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub)) else repr(self.p2)
        return f"{p1_repr} * {p2_repr}"
    
    def evaluate(self, value):
        return self.p1.evaluate(value) * self.p2.evaluate(value)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        p1_repr = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub, Mul)) else repr(self.p1)
        p2_repr = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub, Mul)) else repr(self.p2)
        return f"{p1_repr} / {p2_repr}"
    
    def evaluate(self, value):
        return self.p1.evaluate(value) / self.p2.evaluate(value)


poly = Add( Add( Int(4), Int(3)), Sub( X(), Div( Int(1), Add( Mul(X(), X()), Int(1)))))
#poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
#4 + 3 + X + 1 * ( X * X + 1 )
#4 + 3 + X - 1 / ( X * X + 1 )
print(poly.evaluate(-1))
print(poly)
