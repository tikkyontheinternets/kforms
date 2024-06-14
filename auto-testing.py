import kforms


###########################################
#             TEST     ZONE               #
###########################################

# other test ideas
    # test that the terms of a polynomial are always sorted by degree?? I'm not sure if this is the case but i wanna check
    # test that the largest element of a multipoly is always nonzero
    # test set_coef:
        # a test for every case

def test_multipoly_term_to_index(max_degree,dimension):
    # generate all exponents in 3d with side length 3 (degree <3) (basically a [dimension]-cube)
    # store them in all_exponent_combos
    side_length = max_degree+1
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

    """
    print(all_exponent_combos)
    """

    # check the size of all_exponent_combos
    # make a new list of indices of exponents
    # check that the new list has all indices from 0 to len(all_exponent_combos)-1, uniquely:
        # len(index_list) == len(all_exponent_combos)
        # for i=0..len(all_expoenent_combos)-1, check that index_list contains i
    index_list = []
    for combo in all_exponent_combos:
        index_list.append(kforms.multipoly_term_to_index(dimension, combo.copy()))

    # for my sake:
    """
    for index in range(len(all_exponent_combos)):
        print(str(index) + ". " + str(all_exponent_combos[index]) + " -> " + str(index_list[index]))
    """

    for index_to_find in range(len(all_exponent_combos)):
        found_this_index = False
        for index in range(len(index_list)):
            if index_to_find == index_list[index]:
                found_this_index = True
                break
        if not found_this_index:
            return False
    return True




####################################################################################

# maybe change this to a bunch of assert statements
def testing():
    all_tests_passed = True

    max_degree = 4
    dimension = 4
    all_tests_passed = all_tests_passed and test_multipoly_term_to_index(max_degree,dimension)
    
    return all_tests_passed

# probably need to make this more detailed. use throw() above instead?
if testing():
    print("all tests passed!")
else:
    print("a test failed!")

