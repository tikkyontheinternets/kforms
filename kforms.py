


"""
TODOS
- create a git repo for this file
- reimplement polynomials but multivariate
- implement a way to show off and construct k-forms (with integer coefficients)

"""

class MultiPoly:
    def __init__(self, num_variables):
        self.num_variables = num_variables
        self.coefficients = [0]
        self.degree = 0

    # TODO
    def set_coef(self, value,exponents):
        pass
    def get_coef(self, exponents):
        return 0

    # TODO
    def copy(self):
        pass

    # operates in place
    # multiplies by other poly
    # TODO
    def mul_poly(self, poly):
        pass
    def add_poly(self, poly):
        pass

    def mul_const(self, const):
        pass
        # must update degree potentially

# KForms are made up of variables. The variables start at ZERO.
class KForm:
    def __init__(self, num_variables):
        self.num_variables = num_variables
        self.zero_forms = []
        for index in range(2**num_variables):
            self.zero_forms.append(0)
    
    # TODO
    # zero_form: whatever function type we're working with
    # term: an array of nonnegative integers, the differentials in this term
    def set_zero_form(self,term,zero_form):
        max_variable = 0
        for index in range(len(term)):
            if term[index] > max_variable:
                max_variable = term[index]
        if max_variable+1 > self.num_variables:
            # situation: the term we're setting has a variable not included in the existing zero_form array.
            # we have to extend the array.
            new_num_variables = max_variable + 1
            slots_to_add = 2**new_num_variables - 2**self.num_variables
            for i in range(slots_to_add):
                self.zero_forms.append(0)
            self.num_variables = new_num_variables
        # set the new zero form in there
        self.zero_forms[kform_term_index(term)] = zero_form
    
    def get_zero_form(self,term):
        return 0
    
    # TODO
    # acts in place
    def exterior_product(self,kform2):
        pass
    
    # TODO
    def copy(self):
        pass

# TODO
# return the index in a multipoly array that a given term would be located at
# poly_term: an array of positive integers, the exponents of the variables
def poly_term_index(poly_term):
    return 0


# return the index in a k-form array that a given term would be located at
# kform_term: an array of nonnegative integers (the variables in this differential).
#             No repeats.
def kform_term_index(kform_term):
    final_index = 0
    for index in range(len(kform_term)):
        final_index += 2**kform_term[index]

    return final_index


my_form = KForm(3)
print(my_form.zero_forms)
my_form.set_zero_form([],0)
my_form.set_zero_form([1],1)
my_form.set_zero_form([2],2)
my_form.set_zero_form([1,2],12)
my_form.set_zero_form([0],0)
my_form.set_zero_form([0,1],10)
my_form.set_zero_form([0,1,2],120)

print(my_form.zero_forms)

my_form.set_zero_form([3],69)
print(my_form.zero_forms)

