#!/usr/bin/python
#Author: Amitava Chakraborty

#Defining Strings
str='spam eggs'  # single quotes
str='spam eggs'
str='doesn\'t'  # use \' to escape the single quote...
str="doesn't"
str="doesn't"  # ...or use double quotes instead
str="doesn't"
str='"Yes," he said.'
str='"Yes," he said.'
str="\"Yes,\" he said."
str='"Yes," he said.'
str='"Isn\'t," she said.'
str='"Isn\'t," she said.'

str = 'Hello World!'

print str          # Prints complete string
print str[0]       # Prints first character of the string
print str[2:5]     # Prints characters starting from 3rd to 5th
print str[2:]      # Prints string starting from 3rd character
print str * 2      # Prints string two times
print str + "TEST" # Prints concatenated string

print str.strip()  #trim all whitespaces


ss = "Sammy Shark"
print(ss.upper())
print(ss.lower())

#Boolean Methods
#str.isalnum() 	String consists of only alphanumeric characters (no symbols)
#str.isalpha() 	String consists of only alphabetic characters (no symbols)
#str.islower() 	String’s alphabetic characters are all lower case
#str.isnumeric() 	String consists of only numeric characters
#str.isspace() 	String consists of only whitespace characters
#str.istitle() 	String is in title case
#str.isupper() 	String’s alphabetic characters are all upper case

number = "5"
letters = "abcdef"

print(number.isnumeric())
print(letters.isnumeric())

movie = "2001: A SAMMY ODYSSEY"
book = "A Thousand Splendid Sharks"
poem = "sammy lived in a pretty how town"
print(movie.islower())
print(movie.isupper())

print(book.istitle())
print(book.isupper())

print(poem.istitle())
print(poem.islower())

open_source = "Sammy contributes to open source."
print(len(open_source))

balloon = "Sammy has a balloon."
print(" ".join(balloon))
print("".join(reversed(balloon)))

print(",".join(["sharks", "crustaceans", "plankton"]))
print(balloon.split())

print(balloon.split("a"))
print(balloon.replace("has","had"))

print(str(545).zfill(4))

url = "abc@dlf.com@csv.com"
data = url.split('@')
print len(data)
print data
