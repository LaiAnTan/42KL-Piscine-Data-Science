from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

height_wrong1 = [2.71, 1.15, 1.5]

try:
    bmi = give_bmi(height_wrong1, weight)
except AssertionError as err:
    print("AssertionError:", err.args[0])

height_wrong2 = [2.71, "baba"]

try:
    bmi = give_bmi(height_wrong2, weight)
except AssertionError as err:
    print("AssertionError:", err.args[0])

bmi_wrong1 = [17, "hello"]

try:
    limit = apply_limit(bmi_wrong1, 25)
except AssertionError as err:
    print("AssertionError:", err.args[0])
