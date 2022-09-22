# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(name)


def calc(a, b):
    return a * b


def test():
    for i in range(3, 1, -1):
        print(f'{i}')
    print(random.random())
    a, b = map(int, input().split())
    print(a % b)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # test()
    # print(calc(3, 2))
    a = input()
    b = input()
    for i in a:
        for j in b:
            if i == " " or j == " ":
                continue
            if i == j:
                print("test")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
