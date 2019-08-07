#This program counts a number's factors and determines whether the number is prime.
import sys

def read_textfile(numbers_text_file):
    ''' Loads in and reads text file named numbers.txt '''
    try:
        number_file = open(numbers_text_file, 'r')
        lines = number_file.readlines()
        #print ('There are ' + str(len(lines)) + ' integers read from the file. They are: \n' + str(lines))
        number_file.close()
    except IOError as e:
        #print('Unable to open the file ', numbers_text, '- Ending the program now - \n', e)
        sys.exit()     #used as a last resort to end program; part of sys module
    except FileNotFoundError as e:
        #print('Unable to open the file ', numbers_text, '- Ending the program now - \n', e)
        sys.exit()
    return lines

def factors_prime(number):
    ''' function to give count of factors of the integer & determine if an integer is a prime number '''
    count = 0
    y_n =''
    k = int(number)     #turn i from string to integer and assign to variable k in order for me to do a for loop in the next line of code
    for ii in range(1,k+1):  #added 1 to number because range would only go to one less than number; this is needed in order to get all the numbers to iterate in order to get total count
        if k % ii == 0:
            count = count + 1
    if count == 2:         #prime numbers only have a count of 2
        #print(str(k) + '  is a prime number and it has ' + str(count) + ' factors.')
        y_n = 1
    else:                      #numbers that are not prime have more than count of 2
        #print(str(k) + '  is not a prime number and it has ' + str(count) + ' factors.')
        y_n = 0
    return count, y_n   #return a tuple with 2 elements - the factor count and if it is a prime number

def write_to_file(numbers, count, filename):
    ''' Writes to a file called Output_03.txt '''

    write_text = open(filename,'a')
    if count[1] == 0:
        write_text.write("%s has factors %s \n %s is a not a prime number \n" % (numbers, count[0], numbers))
    elif count[1] == 1:
        write_text.write("%s has factors %s \n %s is a prime number \n" % (numbers, count[0], numbers))

    #input('\nCompleted. Press Enter key to exit.')
    write_text.close()

##### main

num_list = read_textfile(r'/Users/suyeda/Desktop/numbers.txt')


for x in num_list:
    x = x.rstrip("\r\n")
    count = factors_prime(x)
    """print(x)
    print(count)"""
    write_to_file(str(x), count, '/Users/suyeda/Desktop/Output_03.txt')
