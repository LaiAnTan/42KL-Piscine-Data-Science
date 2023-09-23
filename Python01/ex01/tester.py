from array2D import slice_me

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

family_wrong1 = [1.80, 78.4]

try:
    sliced = slice_me(family_wrong1, 0, 2)
except AssertionError as err:
    print("AssertionError:", err.args[0])

family_wrong2 = [[1.80, 78.4],
                 [2.15, 102.7],
                 [2.10, 98.5, 10.5],
                 [1.88, 75.2]]

try:
    sliced = slice_me(family_wrong2, 0, 2)
except AssertionError as err:
    print("AssertionError:", err.args[0])
