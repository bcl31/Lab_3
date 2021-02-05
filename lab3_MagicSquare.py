# ----------------------------------------------------
# Lab 3: Magic Square class
#
# Author:  James Laidlaw
# Collaborators/References: CMPUT 175 team
# ----------------------------------------------------

class MagicSquare:
    def __init__(self, n):
        """
        Initializes an empty square with n*n cells.
        Inputs:
           n (int) - number of rows in square, or equivalently, the number of columns
        Returns: None
        """
        self.square = []  # list of lists, where each internal list represents a row
        self.size = n  # number of columns and rows of square

        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.square.append(row)

    def cellIsEmpty(self, row, col):
        """
        Checks if a given cell is empty, or if it already contains a number
        greater than 0.
        Inputs:
           row (int) - row index of cell to check
           col (int) - column index of cell to check
        Returns: True if cell is empty; False otherwise
        """
        return self.square[row][col] == 0

    def drawSquare(self):
        """
        Displays the current state of the square, formatted with column and row
        indices shown along the top and left side, respectively.
        Inputs: N/A
        Returns: None
        """
        # make string for top line of square, containing only the indices of the x axis
        indices = range(len(self.square))
        top = [" " * 2]
        for index in indices:
            top.append(str(index).center(5))
        top = "".join(top)

        # make a horizontal divider of variable length fit to the square
        divider = (" " * 2) + "+" + ("-" * ((5 * len(self.square))-1)) + "+"

        # print top line and first divider
        print(top)
        print(divider)

        # go through each row of numbers in the square and generate each line from the contents
        for index in indices:

            # add index label for the line
            line = [str(index) + " "]

            # for each entry in the row, add it to the line centered in a four character space
            # if the entry is 0, replace with a period
            for entry in self.square[index]:
                if entry != 0:
                    entry = str(entry)
                else:
                    entry = "."

                # add the entry along with a divider line to list
                line.append("|" + entry.center(4))

            # add final grid line to list, join list into string, print string, print divider
            line.append("|")
            line = "".join(line)
            print(line)
            print(divider)

    def update(self, row, col, num):
        """
        Assigns the integer, num, to the cell at the provided row and column,
        but only if that cell is empty and only if the number isn't already
        in another cell in the square (i.e. it is unique)
        Inputs:
           row (int) - row index of cell to update
           col (int) - column index of cell to update
           num (int) - entry to place in cell
        Returns: True if attempted update was successful; False otherwise
        """
        # check uniqueness
        unique = True
        for valuesInRow in self.square:
            if num in valuesInRow:
                unique = False

        # try to update cell
        if unique:
            if self.size > row >= 0:
                if self.size > col >= 0:
                    if self.cellIsEmpty(row, col):
                        self.square[row][col] = num
                        return True
        return False

    def isFull(self):
        """
        Checks if the square has any remaining empty cells.
        Inputs: N/A
        Returns: True if the square has no empty cells (full); False otherwise
        """
        for row in self.square:
            if 0 in row:
                return False
        return True

    def isMagic(self):
        """
        Checks whether the square is a complete, magic square:
          1. All cells contain a unique, positive number (i.e. greater than 0)
          2. All lines sum up to the same value (horizontals, verticals, diagonals)

        Inputs: N/A
        Returns: True if square is magic; False otherwise
        """
        # get square from self
        square = self.square

        # check if all cells contain unique, positive integers
        contents = []
        for row in square:
            for item in row:
                if item in contents or item <= 0:
                    return False
                else:
                    contents.append(item)

        # use a dict to track all sums because it will create entry if entry that doesnt exist is
        # referenced, therefore at the end if len(sums) == 1 then they all add to the same thing
        sums = {}

        forward_diagonal_sum = 0
        backward_diagonal_sum = 0
        # find all horizontal and vertical sums
        indices = range(len(square))
        for index in indices:

            # get horizontal sum for index
            item_sum = 0
            for item in square[index]:
                item_sum += item
            # if dict entry for sum exists, do nothing, else create new empty dict entry for sum
            sums[item_sum] = None

            # get vertical sums for index
            item_sum = 0
            for vert_index in indices:
                item_sum += square[vert_index][index]
            # if dict entry for sum exists, do nothing, else create new empty dict entry for sum
            sums[item_sum] = None

            # add to forward diagonal sum
            forward_diagonal_sum += square[index][index]

            # add backward diagonal sum
            inverted_index = len(square) - (1+index)
            backward_diagonal_sum += square[inverted_index][inverted_index]

        # add completed diagonal sums to list
        sums[forward_diagonal_sum] = None
        sums[backward_diagonal_sum] = None

        # check if only one sum was found, if so, return true, else, return false
        if len(sums) == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # complete the suggested tests; more tests may be required

    # start by creating an empty 3x3 square and checking the contents of the square attribute
    mySquare = MagicSquare(3)
    print(mySquare.square)

    # check if a specific cell (any cell) is empty, as expected.
    print("Is cell 1, 1 empty?:", mySquare.cellIsEmpty(1, 1))

    # does the entire square display properly when you draw it?
    mySquare.drawSquare()

    # assign a number to an empty cell and display the entire square
    mySquare.update(0, 0, 10)
    mySquare.drawSquare()

    # try to assign a number to a non-empty cell. What happens?
    mySquare.update(0, 0, 9)
    mySquare.drawSquare()

    # check if the square is full. Should it be full after only 1 entry?
    print("is the square full?:", mySquare.isFull())

    # check if the square is a magic square. Should it be after only 1 entry?
    print("Is the square magic?:", mySquare.isMagic())

    # add values to the square so that every line adds up to 21. Display the square.
    mySquare.update(0, 1, 3)
    mySquare.update(0, 2, 8)
    mySquare.update(1, 0, 5)
    mySquare.update(1, 1, 7)
    mySquare.update(1, 2, 9)
    mySquare.update(2, 0, 6)
    mySquare.update(2, 1, 11)
    mySquare.update(2, 2, 4)
    mySquare.drawSquare()
    # check if the square is full
    print("is the square full?:", mySquare.isFull())
    # check if the square is magic
    print("Is the square magic?:", mySquare.isMagic())
    # write additional tests, as needed
