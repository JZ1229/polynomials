from numbers import Number
from numbers import Integral



class Polynomial :
    
    def __init__(self , coefs):
        
        self.coefficients  = coefs

    def degree(self):

        return len(self.coefficients) - 1 


    def __str__(self):

        coefs = self.coefficients
        terms = []
        
        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1]==1 else coefs[1]}x")

        terms += [f"{'' if c==1 else c}x^{d}" for d,c in enumerate(coefs[2:], start=2) if c]

        return '+'.join(reversed(terms)) or '0' 

    def __eq__(self, other):

        return self.coefficients == other.coefficients  


    def __add__(self, other):
        
        if isinstance(other, Polynomial):
            common = min(other.degree(), self.degree()) + 1
            coefs = tuple(a + b for a ,b in zip(self.coefficients[:common], other.coefficients[:common]))
            coefs += other.coefficients[common:] + self.coefficients[common:]
            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,) + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self,other):
        return self + other 

    def __sub__(self, other):

        if isinstance(other, Polynomial):
            common = min(other.degree(), self.degree()) + 1
            coefs = tuple(a - b for a ,b in zip(self.coefficients[:common], other.coefficients[:common]))
            coefs += self.coefficients[common:]
            other_t = ()
            for a in other.coefficients[common:]:
                other_t += (-a,)
            coefs += other_t
            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,) + self.coefficients[1:])

        else:
            return NotImplemented

    def __rsub__(self, other):
        return Polynomial((other,)) - self

    def __mul__(self, other):
         
         if isinstance(other, Number):
             coefs = tuple(a * other for a in self.coefficients)
             return Polynomial(coefs)
            
         elif isinstance(other, Polynomial):
             deg = self.degree() + other.degree() + 1
             list_coef = [0] * deg
             for i in range(self.degree()+1):
                 for n in range(other.degree()+1):
                     coefs = self.coefficients[i] * other.coefficients[n]
                     list_coef[i+n] += coefs
             return Polynomial(tuple(list_coef))

         else:
             return NotImplemented
             

    def __rmul__(self,other):
        return self * other

    def __pow__(self, other):
        if isinstance(other, Integral):
            if other == 1:
                return self * 1
            else:
                return (self**(other-1))*self
        else:
            return NotImplemented

    def __call__(self,other):
        if isinstance(other, Number):
            sum=0
            for i in range(self.degree()+1):
                sum += self.coefficients[i]*other**i
            return sum
        else:
            return NotImplemented
        
    def dx(self):
        list_coef= [0] * self.degree() 
        for i in range(self.degree()):
            list_coef[i] = (i+1) * self.coefficients[i+1] 
        return Polynomial(tuple(list_coef))

    def derivative(self):
        return self.dx()
        


