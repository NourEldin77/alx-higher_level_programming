#!/usr/bin/python3
""" ToDo: Doc """

if __name__ == "__main__":

    import sys
    import calculator_1
    arg_lst = sys.argv

    if len(arg_lst) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(arg_lst[1])
        b = int(arg_lst[3])
        op = arg_lst[2]
        if op == "+":
            print("{:d} {} {:d} = {:d}".format(
                a, op, b, calculator_1.add(a, b)))
        elif op == "-":
            print("{:d} {} {:d} = {:d}".format(
                a, op, b, calculator_1.sub(a, b)))
        elif op == "*":
            print("{:d} {} {:d} = {:d}".format(
                a, op, b, calculator_1.mul(a, b)))
        elif op == "/":
            print("{:d} {} {:d} = {:d}".format(
                a, op, b, calculator_1.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
