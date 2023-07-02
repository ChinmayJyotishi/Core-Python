
# startswith n endswith::
# s="this is the concept of string method"
# print(s.startswith('this')) #to check the start of string
# print(s.startswith('This')) #but it is casesensitive so here it will give u false
# print(s.endswith('method')) #to check the end of string
# print(s.endswith('Method')) #it is also casesensitive

# isalpha()::
# s="this is the concept of string method"
# print(s.isalpha()) #it will check only alphabets in a string
# here it will give u false bcoze space is there

# s="thisistheconceptofstringmethod"
# print(s.isalpha()) 

# isalnum()::
# s="1hello ji how r u"
# print(s.isalnum())  #false becoz space is there
# s="1hello"
# print(s.isalnum()) 
# s="hello"
# print(s.isalnum()) #isalnum means either alphabet or number or both

# s='1111'
# print(s.isalnum())

# s='123'
# print(s.isdigit())

# islower()::
# s="hello"
# print(s.islower()) #all the letters lower or not
# s="1hello"
# print(s.islower()) #

# isupper()::
# s='GJYGYUG'
# print(s.isupper())

# istitle()::
# s="Chinmay"
# print(s.istitle()) #first letter should b capital

# isspace()::
# s="  "
# print(s.isspace()) #is there only space or not

# upper()::
# s="the world is changing"
# print(s.upper()) # make small letter to capital
# print(s) #but here the op is old becoz u cant modify the string 

# lower()::
# s="THE WORLD"
# print(s.lower()) # everything will in lower case
# print(s)

# swapcase()::
# s="Hiii hello namaskar"
# print(s.swapcase()) #if lower then converted to upper and vice versa


# title()::
# s="sggdaug ahgih"
# print(s.title()) #each word 1st letter is capital


# capitalize()::
# s="sggdaug ahgih"
# print(s.capitalize()) #first letter will be capital


# s="Hiii hello namaskar"
# print(len(s)) # count the length of string

# count()::
# s="kaka allla"
# print(s.count('a'))  #how many times the character is

# s="kaka allla"
# print(s.count('a',3))  #how many times the character is after 3 index


# s='i am a bad boy'
# print(s.replace('bad','good'))