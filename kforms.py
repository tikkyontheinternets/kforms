import math




# TODO change the in-place operations into ones that return new objects?
# assertions to add maybe: TODO
    # coefficient with largest index is always nonzero?
    # coefficients are sorted by degree?
class MultiPoly:
    def __init__(self, num_variables):
        self.num_variables = num_variables #TODO add the ability to add more vars later? or at least to add this to a larger poly
        self.coefficients = []
        self.max_degree = 0

    # TODO
    def __str__(self):
        result = ""
        if self.coefficients == []:
            return "0"
        coef_index = 0
        while self.coefficients[coef_index] == 0:
            coef_index += 1
            # assumes: will find a nonzero entry
        result = result.append(self.term_to_string(multipoly_index_to_term(self.num_variables, coef_index))) #TODO must finish index_to_term first
        for coef_index in range(len(self.coefficients)):
            if self.coefficients[coef_index] != 0:

        return str(self.coefficients)

    # term is a nonempty array of integers representing the exponents on this term
    # returns a string representation of this term (with no coefficient)
    def term_to_string(self,term):
        result = "(x_0^"
        result = result + str(term[0]) + ")"
        for exponent_index in range(1,len(term)):
            result = result + "*(x_" + str(exponent_index) + "^" + str(term[exponent_index]) + ")"
        return result


    #TODO
    # assumption: the elements of self.coefficients are sorted by degree (I think I coded it like that)
    def update_degree(self):
        if len(self.coefficients) > 0:
            self.max_degree = degree(multipoly_index_to_term(self.num_variables, len(self.coefficients)-1))
        else:
            self.max_degree = 0

    # TODO test getter and setter here

    # TODO
    # note: maybe have it such that unless the entire polynomial is zero, the entry with the largest index is always nonzero? 
    # general concept:
        # if we're setting the largest index to 0, we should shrink the list.
        # if we're setting something to a nonzero value that's OUTSIDE the current list, we should grow the list.
        # if we're setting something to zero that's outside teh current list, we do nothing.
    def set_coef(self, value, exponents):
        # do multipoly_term_to_index(exponents)
        target_index = multipoly_term_to_index(self.num_variables,exponents)
        #degree = degree(exponents)
        
        if value == 0:
            # it's outside the current list
            if target_index >= len(self.coefficients):
                pass # do nothing
            # it's the largest nonzero element
            elif target_index == len(self.coefficients)-1: 
                # find largest nonzero element beneath the last one
                # shrink to there
                self.coefficients.pop()
                index = len(self.coefficients)-1
                while self.coefficients[index] == 0 and index >= 0:
                    self.coefficients.pop()
                    if index == 0:
                        break
                    index -= 1
            # it's inside the existing list
            else: 
                self.coefficients[target_index] = value
        else: # the value is nonzero
            # it's outside the current list
            if target_index >= len(self.coefficients):
                # expand the list to there
                while len(self.coefficients)-1 < target_index:
                    self.coefficients.append(0)
                self.coefficients[target_index] = value
            # it's inside the current list
            else:
                self.coefficients[target_index] = value
        
        # call update_degree TODO
        # TODO: possibly check if we only need to do update_degree in certain cases:
            # is the largest nonzero element always the one with the largest degree?
            # are the elements actually SORTED by degree?? I think so???
        self.update_degree()

    # TODO        
    def get_coef(self, exponents):
        index = multipoly_term_to_index(self.num_variables, exponents)
        if len(self.coefficients) < index+1:
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

def degree(exponents):
    sum = 0
    for i in range(len(exponents)):
        sum += exponents[i]
    return sum

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
    degree_of_term = degree(exponents)
    # figure out how many entries there are "beneath" it in the simplex (using n_simplex_number)
    entries_before_this = n_simplex_number(dimension,degree_of_term)

    # recurse on just the "side" it's on 
    exponents.pop(0)
    final_index = entries_before_this + multipoly_term_to_index(dimension-1,exponents)

    return int(final_index)


# TODO
# take in a number representing an index in a multipoly array, and spit out an array of exponents from the term that coefficient comes with.
# dimension: the num of variables in the multivariable polynomial
# index: a nonnegative integer, the index of the desired term.
def multipoly_index_to_term(dimension, index):
    return []
    # (see notebook)
    # find the "simplex coordinates" of this index, i.e. for dimension=3 and index=11:
        # 11          is in the 4th 2-simplex
        # (11-10)     is in the 2nd 1-simplex
        # ((11-10)-1) is in the 1st 0-simplex
    # then:
        # 4th 2-simplex -> sum of coords {0,1,2} is 3
        # 2nd 1-simplex -> sum of coords {1,2}   is 1
        # 1st 0-simplex -> sum of coords {2}     is 0
    # so, 11 maps to [2,1,0].

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



