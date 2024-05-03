# task 1 Calculate the value of a particular arithmetic expression twice: once normally, and once using parentheses. Compare the two results to see if they match.

math = 9 + 2 * 3 

print(math) 

math_1 = 9 + (2 * 3)

print(math_1)

if math == math_1:
    print(True)


# task 2

bananas = 7
potato = 14
salad = 5
if bananas + potato < salad or bananas + salad < potato:
    print(True)
else:
    print(False)