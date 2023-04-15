n = int(input())

for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")
    for stars in range(1, row):
        print("*", end=" ")
    print("*")

for row in range(n - 1, 0, - 1):
    for space in range(n - row):
        print(" ", end="")
    for stars in range(1, row):
        print("*", end=" ")
    print("*")

'''
First part:

This code creates a triangle of stars with a size defined by the user through the input parameter "n".

The first line of the code reads an integer from standard input (using the input() function) and stores 
it in the variable "n".

Then the code uses two nested for loops to output the rows of the triangle. 
The outer loop iterates over the numbers from 1 to "n" and determines the number of the row that needs to be output.

The inner loop uses the "row" variable to determine how many spaces to print before the stars on the current row, 
using the formula "n - row". Then the loop uses another variable "stars" to determine the number of stars 
that need to be printed on the current row, using the formula "range(1, row)".

In the inner loop, the stars are printed one after the other with a space between them, 
using the "end=' '" function to ensure that once all stars are printed, the next line is output on the same line.

After the inner loop completes, the final line of the current triangle is output 
using the "print('*')" function. This line represents a single star at the end of each row.

The code continues in this manner until all rows of the triangle have been output.

Second part:

Then, we use the same code for second part - inverted triangle.
We have to edit only the first row - as you can seen in the example /row 10/.
'''