from give_bmi import give_bmi, apply_limit

# height = [2.71, 1.15]
# weight = [165.3, 38.4]

height = [1.71, 1.65, 1.73, 1.95, 1.63]
weight = [65.3, 58.4, 63.4, 94.5, 72.9]

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
