import string
import random

Letter=string.ascii_letters
Number= string.digits
Punctuation= string.punctuation

#Determine the password length
def password_length():
    length= input("Please write the password length: ")
    return int(length)

#Generate the password
def password_generator(option,length=11):
    #generate the password
    password= password_content(option)
    #convert it to list and shuffle it
    password=   list(password)
    random.shuffle(password)

    rand_password=  random.choices(password, k= length)
    rand_password=  ''.join(rand_password)
    return rand_password
    


#print("The first password( "+str(len(first_pass))+"):\t\t"+first_pass)
#print("The second password( "+str(len(second_pass))+"):\t\t"+second_pass)
#Choose password content(letter, number, punctuation)
def choose_content():
    letters=    input("Do you want letters? (True/False): ")
    numbers=    input("Do you want numbers? (True/False):")
    punctuations=   input("Do you want punctuations? (True/False): ")

    try:
        letters=    eval(letters.title())
        numbers=    eval(numbers.title())
        punctuations=   eval(punctuations.title())
        return [letters, numbers, punctuations]
    except NameError as e:
        print("Invalid value. Use True or False")
        print("Try again!!")
    return [True,True, True]

def password_content(content):
    password=   ''
    password+=  Letter if content[0] else ''
    password+=  Number if content[1] else ''
    password+=  Punctuation if content[2] else ''
    return password


if __name__=='__main__':
    length=     password_length()
    content=    choose_content()
    passwrod=   password_generator(content, length)
    print(passwrod)