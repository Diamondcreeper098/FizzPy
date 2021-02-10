# ==========================================================================
# =                                                                        =
# =                       Github: Diamondcreeper098                        =
# =                       Project name: FizzPy                             =
# =         Description : I wanted to make an scalable Fizzbuzz solution   =
# =                                                                        =
# ==========================================================================

# ===============================[Functions Area]===========================
# The fizzbuzz function gets following inputs
# number_dict: The Dictionary of the numbers and it's corresponding message
# Formatted like: {Number} : {Message}
# And the second parameter
# last: the limit number to run the loop

def fizzbuzz(number_dict, last):
    # We are going to loop from 1 to the last number
    for number in range(1, last+1):
        # We Are going to reset the msg variable every iteration
        msg = ""
        # Then We are going to loop through the number dictionary
        for Dividend in number_dict:
            # Check to see if Number is divisible by the Dividend
            # If Yes then it's going to append the text that is Connected to Dividend in the Dictionary
            if number % Dividend == 0:
                msg += number_dict[Dividend]
        # After Checking to see if the number is divisible by every dividend available in the Number Dictionary
        # If the Number wasn't divisible to any of them then set the msg to the number itself
        if msg == "":
            msg = str(number)
        # Then We are going to Print the Number and it's Corresponding State In the Format written below
        # {Number} : {msg}
        print ("%d : %s" % (number, msg))


# ==========================================================================

# ==============================[The Main Code]=============================
if __name__ == '__main__':
    NumberDict = {
        3: "Fizz",
        5: "Buzz",
        7: "Flip",
        13: "Fri"
    }
    fizzbuzz(NumberDict, 15)

# ==========================================================================
