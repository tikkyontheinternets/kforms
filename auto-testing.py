import kforms


def testing():
    return True

# probably need to make this more detailed. use throw() above instead?
if testing():
    print("all tests passed!")
else:
    print("a test failed!")


# test addition
###########################################
#             TEST     ZONE               #
###########################################

# other test ideas
# - take the below stuff and, for a number of different sizes of potential polynomial, check that the generated indices are all unique and shit
"""
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

"""


