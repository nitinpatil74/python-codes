# Swap Two Values without a Third
#This is one is a classic examination question.

#Is there a way to swap two variables without a third helper variable?

#The answer is yes. You can use tuple unpacking to achieve this.
a = 1
b = 2

a, b = b, a

print(a, b)