from art import logo


def subtract(n1,n2):
    return n1 - n2

def add(n1,n2):
    return n1 + n2

def mutiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2



operations = {
    "+": add,
    "-": subtract,
    "*": mutiply,
    "/": divide,
}


# my_favourite_opeartion = add(2,3)
# print(my_favourite_opeartion)


def caculator():
    print(logo)
    should_accumulate = True
    n1 = float(input("What is the first number?: ")) # 因为不需要重复，所以放外面。

    while should_accumulate:

        for symbol in operations:
            print(symbol)

        opeartion_get = input("Pick an Operation: ")

        n2 = float(input("What is the next number?: "))

        answer = operations[opeartion_get](n1,n2)
        print(f"{n1} {opeartion_get} {n2} = {answer}")


        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if choice == "y":
            n1 = answer # 其实就是把n1变成我们这次的结果，answer就是这一轮的结果。
        else:
            should_accumulate = False
            print("\n" * 20)
            caculator()

caculator()