# Bisection Method


def func(x):  # Returns the value of the function
    return eval(eqn)


# Prints root of f(x)
def bisection(a, b):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b\n")
        return

    c = a
    while (b - a) >= 0.01:

        # Find middle point
        c = (a + b) / 2

        print("The value of root is : ", "%.4f" % c)

        # Check if middle point is root
        if func(c) == 0.0:
            break

        # Decide the side to repeat the steps
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

    print("The final value of root is : ", "%.4f" % c)


# Taking user input
eqn = input("Enter f(x): ")
a = int(input("Enter initial left point: "))
b = int(input("Enter initial right point: "))
bisection(a, b)

