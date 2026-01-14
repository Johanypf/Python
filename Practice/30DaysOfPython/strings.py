letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)



#String Concatenation



first_name = 'And'
last_name = 'ted'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) 
print(len(first_name))  # 
print(len(last_name))   # 
print(len(first_name) > len(last_name)) # 
print(len(full_name)) # 

'''
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")

'''

'''
 Exercises - Day 4
Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
Declare a variable named company and assign it to an initial value "Coding For All".
Print the variable company using print().
Print the length of the company string using len() method and print().
Change all the characters to uppercase letters using upper() method.
Change all the characters to lowercase letters using lower() method.
Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
Cut(slice) out the first word of Coding For All string.
Check if Coding For All string contains a word Coding using the method index, find or other methods.
Replace the word coding in the string 'Coding For All' to Python.
Change Python for Everyone to Python for All using the replace method or other methods.
Split the string 'Coding For All' using space as the separator (split()) .
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
What is the character at index 0 in the string Coding For All.
What is the last index of the string Coding For All.
What character is at index 10 in "Coding For All" string.
Create an acronym or an abbreviation for the name 'Python For Everyone'.
Create an acronym or an abbreviation for the name 'Coding For All'.
Use index to determine the position of the first occurrence of C in Coding For All.
Use index to determine the position of the first occurrence of F in Coding For All.
Use rfind to determine the position of the last occurrence of l in Coding For All People.
Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
 'You cannot end a sentence with because because because is a conjunction'
Use rindex to find the position of the last occurrence of the word because in the following sentence: 
'You cannot end a sentence with because because because is a conjunction'
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence 
with because because because is a conjunction'
Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot 
end a sentence with because because because is a conjunction'
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with 
because because because is a conjunction'
Does ''Coding For All' start with a substring Coding?
Does 'Coding For All' end with a substring coding?
'   Coding For All      '  , remove the left and right trailing spaces in the given string.
Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python
The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 
'Pyramid', 'Falcon']. Join the list with a hash with space string.
Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.
Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144





'''




company =  "Coding for All string"
print(company.replace("Coding","Python"))
