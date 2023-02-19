# import complex modules
import cmath

# quadratic
a = 1
b = 2
c = 1

d = (b**2) - (4*a*c)

x1 = (-b-cmath.sqrt(d))/(2*a)
x2 = (-b+cmath.sqrt(d))/(2*a)

quad = ('The solutions are {0} and {1}'.format(x1,x2))




class simple_calc:
    def __init__(self, name: str):
        self._name = name

    def get_name(self):
# addition
        def add_fn(a1_arg, a2_arg):
            return a1_arg+a2_arg
        return self._name

    def set_name(self, new_name: str):
        self._name = new_name







# subtraction
        def sub_fn(s1_arg, s2_arg):
            return s1_arg-s2_arg

# multiplication
        def mult_fn(m1_arg, m2_arg):
            return m1_arg*m2_arg

# division
        def div_fn(d1_arg, d2_arg):
            return d1_arg/d2_arg