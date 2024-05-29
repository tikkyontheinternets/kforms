import math


# TODO change the in-place operations into ones that return new objects?

class MultiPoly:
    def __init__(self, num_variables):
        self.num_variables = num_variables
        self.coefficients = [0]
        self.max_degree = 0

# TODO test getter and setter here

    # TODO
    def set_coef(self, value,exponents):
        # do multipoly_term_to_index(exponents)
        index = multipoly_term_to_index(self.num_variables,exponents)

        # if value is nonzero:
        # ask if the new index is inside the current array
        # if not, expend the array to include this
        if value != 0:
            if index+1 <= len(self.coefficients):
                self.coefficients[index] = value
            else:
                #expand
                # TODO
                pass

        # if value is zero:
        # if inside current array:
        #   figure out if it's the highest nonzero entry, maybe shrink the array
        #   if it's not the highest nonzero entry, do nothing
        # if not inside current array:
        #   do nothing lol
        else:
            if index+1 <= len(self.coefficients):
                #figure out if highest nonzero entry
                # TODO
                pass
            else:
                pass

    # TODO        
    def get_coef(self, exponents):
        index = multipoly_term_to_index(self.num_variables, exponents)
        if len(self.coefficients) <= index+1:
            return 0
        else:
            return self.coefficients[index]

    # TODO
    def copy(self):
        new_poly = MultiPoly(self.num_variables)
        new_poly.coefficients = self.coefficients.copy()
        new_poly.max_degree = self.max_degree
        return new_poly

    # alt TODO: change these to raw __mul__ and __add__ etc

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


# like triangle numbers but for higher dimensions
# (I worked out the formula by browsing wikipedia)
def n_simplex_number(number_of_dimensions,side_length):
    numerator = 1
    for i in range(number_of_dimensions):
        numerator *= side_length + i
    denominator = math.factorial(number_of_dimensions)
    return numerator/denominator

# TODO
# take in an array of exponents and spit out the index in the multipoly array their coefficient would appear at
# dimension: the num of variables in the multivariable polynomial
# exponents: an array of nonnegative integers, the exponents on the desired term
def multipoly_term_to_index(dimension, exponents):
    # if exponents is all zero, return zero
    all_zero = True
    for i in range(len(exponents)):
        if exponents[i] != 0:
            all_zero = False
    if all_zero:
        return 0

    # compute the degree of this term
    degree = 0
    for i in range(len(exponents)):
        degree += exponents[i]

    # figure out how many entries there are "beneath" it in the simplex (using n_simplex_number)
    entries_before_this = n_simplex_number(dimension,degree)

    # recurse on just the "side" it's on 
    exponents.pop(0)
    final_index = entries_before_this + multipoly_term_to_index(dimension-1,exponents)

    return final_index

# TODO
# take in a number representing an index in a multipoly array, and spit out an array of exponents from the term that coefficient comes with.
# dimension: the num of variables in the multivariable polynomial
# index: a nonnegative integer, the index of the desired term.
def multipoly_index_to_term(dimension, index):
    return []

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
        self.zero_forms[kform_term_to_index(term)] = zero_form
    
    def get_zero_form(self,term):
        term_index = kform_term_to_index(term)
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


# the reverse of kform_term_to_index: converts a single number to an array of numbers representing the variables in that term.
# index: a nonnegative integer
# return: an array of nonnegative integers
def kform_index_to_term(index):
    variables = []
    exponent = 0
    while (index > 0):
        if (index % 2**(exponent+1)) >= (2**exponent):
            variables.append(exponent)
            index -= index % (2**(exponent+1))
        exponent += 1
    return variables


# return the index in a k-form array that a given term would be located at
# kform_term: an array of nonnegative integers (the variables in this differential).
#             No repeats.
def kform_term_to_index(kform_term):
    final_index = 0
    for index in range(len(kform_term)):
        final_index += 2**kform_term[index]

    return final_index




# takes a term from a kform and returns a string representation of it
# (assumes the term is nonzero)
def kform_term_to_string(kform,term_index):
    term_vars = kform_index_to_term(term_index)
    return_string = ""
    return_string += str(kform.get_zero_form(term_vars))
    
    for index in range(len(term_vars)):
        return_string += "*d_" + str(term_vars[index])

    return return_string


###########################################
#             TEST     ZONE               #
###########################################

# generate all exponents in 3d with side length 3 (degree <3) (basically a [dimension]-cube)
side_length = 4
max_degree = 3
dimension = 3
all_exponent_combos = [[]]
for dimension_index in range(dimension):
    new_combos = []
    for combo_index in range(len(all_exponent_combos)):
        for side_index in range(side_length):
            current_combo = all_exponent_combos[combo_index].copy()
            current_combo.append(side_index)
            new_combos.append(current_combo)
    all_exponent_combos = new_combos

# remove all entries with degree above max_degree (to make it a simplex type thing)
combo_index = 0
while combo_index < len(all_exponent_combos):
    degree = 0
    for exponent_index in range(len(all_exponent_combos[combo_index])):
        degree += all_exponent_combos[combo_index][exponent_index]
    if degree > max_degree:
        all_exponent_combos.pop(combo_index)
    else:
        combo_index += 1



for i in range(len(all_exponent_combos)):
    print(str(all_exponent_combos[i]) + " -> " + str(multipoly_term_to_index(dimension,all_exponent_combos[i])))
#    print(all_exponent_combos[i])

# multipoly_term_to_index


