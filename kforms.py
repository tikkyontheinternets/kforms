


"""
TODOS
- create a git repo for this file
- reimplement polynomials but multivariate
- implement a way to show off and construct k-forms (with integer coefficients)

"""

# TODO rename the functions that enumerate terms in a consistent way
# TODO change the in-place operations into ones that return new objects?

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

    # TODO
    # variable is the number identifying the variable we're taking the derivative with respect to 
    def derivative(self,variable):
        pass


# KForms are made up of variables. The variables start at ZERO.
class KForm:
    def __init__(self, num_variables):
        self.num_variables = num_variables
        self.zero_forms = []
        for index in range(2**num_variables):
            self.zero_forms.append(0)
   
   # TODO improve this
    def __str__(self):
        result = ""
        for index in range(len(self.zero_forms)):
            if self.zero_forms[index] != 0: # TODO:change for polynomials??
                if result != "":
                    result += " + "
                result += kform_term_to_string(self,index)
        if result == "":
            return "0"
        else:
            return result

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
        term_index = kform_term_index(term)
        if term_index+1 >= len(self.zero_forms):
            return 0 # TODO change if poly???
        else:
            return self.zero_forms[term_index]
    
    # TODO
    # acts in place
    def exterior_product(self,kform2):
        pass

    # TODO
    # acts in place, takes this k-form and turns it into a (k+1)-form
    def exterior_derivative(self):
        pass
    
    # TODO
    def copy(self):
        pass

# TODO
# take in an array of exponents and spit out the index in the multipoly array their coefficient would appear at
def multipoly_term_index(exponents):
    return 0

# TODO
# like triangle numbers but for higher dimensions
def n_simplex_number(number_of_dimensions,side_length):
    return 0

# takes a term from a kform and returns a string representation of it
# (assumes the term is nonzero)
def kform_term_to_string(kform,term_index):
    term_vars = kform_index_to_vars(term_index)
    return_string = ""
    return_string += str(kform.get_zero_form(term_vars))
    
    for index in range(len(term_vars)):
        return_string += "*d_" + str(term_vars[index])

    return return_string

# the reverse of kform_term_index: converts a single number to an array of numbers representing the variables in that term.
# index: a nonnegative integer
# return: an array of nonnegative integers
def kform_index_to_vars(index):
    variables = []
    exponent = 0
    while (index > 0):
        if (index % 2**(exponent+1)) >= (2**exponent):
            variables.append(exponent)
            index -= index % (2**(exponent+1))
        exponent += 1
    return variables


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


forms = []
num_forms = 7

for i in range(num_forms):
    forms.append(KForm(3))


forms[0].set_zero_form([],1)
forms[1].set_zero_form([],1)
forms[1].set_zero_form([2],5)
forms[2].set_zero_form([],1)
forms[2].set_zero_form([2],5)
forms[2].set_zero_form([2,1],5)


for i in range(len(forms)):
    print(forms[i])
