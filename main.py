"""
Printing horizontally or vertically one or more X, Y, or Z characters as star-shaped
according to the pre-entered user inputs.
The user should enter the followings:
- an odd number ( which is equal to or greater than 3) indicating the size of the X, Y, or Z.
- one or more X, Y, or Z characters
- horizontal or vertical axis selection

Horizontal output for odd-number = 5    Horizontal output for odd-number = 3
*       * *       * * * * * *           *   * *   * * * *
  *   *     *   *         *               *     *     *
    *         *         *               *   *   *   * * *
  *   *       *       *
*       *     *     * * * * *

Vertical output for odd-number = 5      Vertical output for odd-number = 3
*       *                               *   *
  *   *                                   *
    *                                   *   *
  *   *                                 *   *
*       *                                 *
*       *                                 *
  *   *                                 * * *
    *                                     *
    *                                   * * *
    *
* * * * *
      *
    *
  *
* * * * *
"""

import numpy as np

def check_word():
    WordList = ["X", "Y", "Z", "x", "y", "z"]
    while True:
        word = str(input("Enter X Y or/and Z"))
        StrList = list(word)
        flag = []
        for index in range(0, len(StrList), 1):
            if StrList[index] not in WordList:
                print("The input should only consist of X, Y and/or Z")
                flag.append(0)
            else:
                flag.append(1)
        if len(flag) == sum(flag):
            break
    return StrList

def check_number():
    while True:
        number = int(input("Enter an odd number"))
        if number < 3:
            print("the number is greater than 3")
        elif number%2 == 0:
            print("the number is an even number")
        else:
            break
    return number

def select_axis():
    while True:
        AxisList = ["H", "h", "V", "v"]
        axis = str(input("Enter Printing Axis -> 'H' for horizontal or 'V' for Vertical"))
        if len(axis) > 1:
            print("Only one character should be entered")
        elif axis not in AxisList:
            print("Enter only one character: H or V")
        else:
            break
    return axis.upper()

def x_pattern(odd_number):
    x_pat = np.zeros((odd_number, odd_number), 'U1')
    for row in range(0, odd_number, 1):
        for col in range(0, odd_number, 1):
            if row + col == odd_number - 1:
                x_pat[row][col] = "*"
            elif row == col:
                x_pat[row][col] = "*"
            else:
                x_pat[row][col] = " "
    return x_pat

def y_pattern(odd_number):
    y_pat = np.zeros((odd_number, odd_number), 'U1')
    middle = int((odd_number - 1) / 2)
    for row in range(0, odd_number, 1):
        for col in range(0, odd_number, 1):
            if col == middle and row >= middle:
                y_pat[row][col] = "*"
            elif col == odd_number - 1 - row and row < middle:
                y_pat[row][col] = "*"
            elif row == col and row < middle:
                y_pat[row][col] = "*"
            else:
                y_pat[row][col] = " "
    return y_pat

def z_pattern(odd_number):
    z_pat = np.zeros((odd_number, odd_number), 'U1')
    for row in range(0, odd_number, 1):
        for col in range(0, odd_number, 1):
            if row == 0 or row == odd_number - 1 or row + col == odd_number - 1:
                z_pat[row][col] = "*"
            else:
                z_pat[row][col] = " "
    return z_pat

def print_HV(chr_list, odd_number, axis):
    str_lists = [[] for i in range(len(chr_list))]
    for index in range(0, len(chr_list), 1):
        if chr_list[index] == "X" or chr_list[index] == "x":
            str_lists[index] = x_pattern(odd_number)
        elif chr_list[index] == "Y" or chr_list[index] == "y":
            str_lists[index] = y_pattern(odd_number)
        else:
            str_lists[index] = z_pattern(odd_number)
    if axis == "H":
        j = 0
        for i in range(len((str_lists[j]))):
            for j in range(len(str_lists)):
                for k in range(len((str_lists[j][i]))):
                    print(str_lists[j][i][k], end=' ')
            print()
    else:  # if axis=="V"
        strlists_2d_V = np.reshape(str_lists, (odd_number * len(chr_list), odd_number))
        for l in strlists_2d_V:
            print(*l)

size_number = check_number()
c_list = []
c_list = check_word()
sel_axis = select_axis()
print(print_HV(c_list, size_number, sel_axis))
