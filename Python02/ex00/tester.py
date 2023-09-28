from load_csv import load

print(load("../life_expectancy_years.csv"))

try:
    load("../balls.csv")
except AssertionError as err:
    print(err.args[0])

try:
    load("../tester.py")
except AssertionError as err:
    print(err.args[0])
