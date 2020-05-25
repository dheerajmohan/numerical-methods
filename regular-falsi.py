# Regular Falsi Method

MAX_ITER = 100  # Number of iterations


def func(x):  # Returns the value of the function
    return eval(eqn)


# Prints root of func(x) in interval [a, b]
def regulaFalsi(a, b):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return -1

    c = a  # Initialize result

    for i in range(MAX_ITER):

        # Find the point that touches x axis
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))

        if i % 10 == 0:
            print("The value of root is : ", '%.4f' % c)

        # Check if the above found point is root
        if func(c) == 0:
            break

        # Decide the side to repeat the steps
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
    print("The final value of root is : ", '%.4f' % c)


# Taking user input
eqn = input("Enter f(x): ")
a = int(input("Enter initial left point: "))
b = int(input("Enter initial right point: "))
regulaFalsi(a, b)
