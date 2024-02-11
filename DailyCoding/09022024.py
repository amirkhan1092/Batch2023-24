'''Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

Given a string, return whether it represents a number. Here are the different kinds of numbers:

"10", a positive integer
"-10", a negative integer
"10.1", a positive real number
"-10.1", a negative real number
"1e5", a number in scientific notation
And here are examples of non-numbers:
"a"
"x 1"
"a -2"
"-"'''
def number_validity(num_string):
    try:
        val = eval(num_string)
        if 'e' in num_string:
            return 'number in scientific notation'
        elif type(val) == int:
            return 'a Positive integer' if val > 0 else 'a negaitive intger'
        else:
            return 'a positive real number' if val > 0 else 'a negative real number'
    except:
        return 'non-numbers'



# main code 
raw_data = input('Enter the raw string ')
re = number_validity(raw_data)
print(re)