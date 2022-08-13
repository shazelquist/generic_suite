#!C:/Python_X64/python
#!/usr/bin/python3
# Shane_Hazelquist #Date: Saturday, 8/13/2022  #Time: 3:3.11
# Imports:
import suite

# Directive:
# -Test functionality of suite


@add_func
def test(name="generic"):
    print("hello, {}".format(name))


@add_func
@param_convert
def hungry(arg, *args, **kwargs):
    """
    hungry
    Consumes all arguments
    """
    print("CONSUME FLESH")
    print("\t", arg, args, kwargs)


@suite.add_func
@suite.param_convert
def mult(a, b):
    print(a * b)


@suite.add_func
@suite.param_convert
def divide(a, b):
    print(a / b)


@suite.add_func
def echo(*args, **kwargs):
    print(args, kwargs)


def generic():
    print("this really doesn't do anything")


suite.add_func(generic)


def main():
    print("test_suite")
    suite.run_suite()


if __name__ == "__main__":
    main()
