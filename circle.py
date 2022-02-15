#! /usr/bin/python3
import sys

def printCircle(radius : int) -> None:
    circle = ['*' * radius]
    for i in range(int(radius / 2)):
        circle.append('*' + ' ' * len(circle[-1]) + '*')
    middleLine = '*' + ' ' * len(circle[-1]) + '*'
    endingLines = list(reversed(circle))
    for i in range(radius):
        circle.append(middleLine)
    circle.extend(endingLines)
    for i in circle:
        print(i.center(len(middleLine)))

def main():
    printCircle(int(sys.argv[1]))

main()
