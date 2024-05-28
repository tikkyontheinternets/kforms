


"""
TODOS
- create a git repo for this file
- reimplement polynomials but multivariate
- implement a way to show off and construct k-forms (with integer coefficients)

"""

class MultiPoly:
    def __init__(num_variables):
        self.num_variables = num_variables
        self.coefficients = [0]
        self.degree = 0

    # TODO
    def set_coef(value,exponents):
        pass
    def get_coef(exponents):
        return 0

    # TODO
    def copy():
        pass

    # operates in place
    # multiplies by other poly
    # TODO
    def mul_poly(poly):
        pass
    def add_poly(poly):
        pass

    def mul_const(const):
        pass
        # must update degree potentially

class KForm:
    def __init__(num_variables):
        self.num_variables = num_variables
        self.zero_forms = [0]
    
    # TODO
    # zero_form: whatever function type we're working with
    # term: an array of nonnegative integers, the differentials in this term
    def set_zero_form(zero_form,term):
        pass
    def get_zero_form(term):
        return 0
    
    # TODO
    # acts in place
    def exterior_product(kform2):
        pass
    
    # TODO
    def copy():
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





