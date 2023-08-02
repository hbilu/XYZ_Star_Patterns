"""
Printing horizontally or vertically one or more X, Y, or Z characters as star-shaped
according to the pre-entered user inputs.
The user should enter the followings:
- an even/odd number (which is equal to or greater than 3) indicating the size of the X, Y, or Z.
- one or more X, Y, or Z characters
- horizontal or vertical axis selection

Output Examples:
Horizontal output for odd-number = 5  Horizontal output for odd-number = 3  Horizontal output for even-number = 6
*       * *       * * * * * *         *   * *   * * * *                     *         * *         * * * * * * *
  *   *     *   *         *             *     *     *                         *     *     *     *           *
    *         *         *             *   *   *   * * *                         * *         * *           *
  *   *       *       *                                                         * *         * *         *
*       *     *     * * * * *                                                 *     *       * *       *
                                                                            *         *     * *     * * * * * *

Vertical output for odd-number = 5    Vertical output for odd-number = 3    Vertical output for even-number = 6
*       *                             *   *                                 *         *
  *   *                                 *                                     *     *
    *                                 *   *                                     * *
  *   *                               *   *                                     * *
*       *                               *                                     *     *
*       *                               *                                   *         *
  *   *                               * * *                                 *         *
    *                                   *                                     *     *
    *                                 * * *                                     * *
    *                                                                           * *
* * * * *                                                                       * *
      *                                                                         * *
    *                                                                       * * * * * *
  *                                                                                 *
* * * * *                                                                         *
                                                                                *
                                                                              *
                                                                            * * * * * *
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
        try:
            number = int(input("Enter an even/odd number greater than 3"))
            if number < 3:
                print("The number is less than 3")
            else:
                break
        except ValueError:
            print("This is not a number. Try again!")
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

def x_pattern(number):
    x_pat = np.zeros((number, number), 'U1')
    for row in range(0, number, 1):
        for col in range(0, number, 1):
            if row + col == number - 1:
                x_pat[row][col] = "*"
            elif row == col:
                x_pat[row][col] = "*"
            else:
                x_pat[row][col] = " "
    return x_pat

def y_pattern(number):
    y_pat = np.zeros((number, number), 'U1')
    middle = int((number - 1) / 2)
    if number % 2 == 1: # if it is an odd number
        for row in range(0, number, 1):
            for col in range(0, number, 1):
                if col == middle and row >= middle:
                    y_pat[row][col] = "*"
                elif col == number - 1 - row and row < middle:
                    y_pat[row][col] = "*"
                elif row == col and row < middle:
                    y_pat[row][col] = "*"
                else:
                    y_pat[row][col] = " "
        return y_pat
    else: # if it is an even number
        for row in range(0, number, 1):
            for col in range(0, number, 1):
                if col == middle and row >= middle:
                    y_pat[row][col] = "*"
                elif col == middle+1 and row >= middle:
                    y_pat[row][col] = "*"
                elif col == number - 1 - row and row < middle:
                    y_pat[row][col] = "*"
                elif row == col and row < middle:
                    y_pat[row][col] = "*"
                else:
                    y_pat[row][col] = " "
        return y_pat

def z_pattern(number):
    z_pat = np.zeros((number, number), 'U1')
    for row in range(0, number, 1):
        for col in range(0, number, 1):
            if row == 0 or row == number - 1 or row + col == number - 1:
                z_pat[row][col] = "*"
            else:
                z_pat[row][col] = " "
    return z_pat

def print_HV(chr_list, number, axis):
    str_lists = [[] for i in range(len(chr_list))]
    for index in range(0, len(chr_list), 1):
        if chr_list[index] == "X" or chr_list[index] == "x":
            str_lists[index] = x_pattern(number)
        elif chr_list[index] == "Y" or chr_list[index] == "y":
            str_lists[index] = y_pattern(number)
        else:
            str_lists[index] = z_pattern(number)
    if axis == "H":
        j = 0
        for i in range(len((str_lists[j]))):
            for j in range(len(str_lists)):
                for k in range(len((str_lists[j][i]))):
                    print(str_lists[j][i][k], end=' ')
            print()
    else:  # if axis=="V"
        strlists_2d_V = np.reshape(str_lists, (number * len(chr_list), number))
        for l in strlists_2d_V:
            print(*l)

size_number = check_number()
c_list = []
c_list = check_word()
sel_axis = select_axis()
print(print_HV(c_list, size_number, sel_axis))
