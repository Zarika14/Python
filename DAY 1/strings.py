anna='''Anna has broken his hand,
now it has become very difficult for him 
as he can not go to class,campus and not even gym.
all he can do is lie down on the bed and use his phone
and sometimes study too.'''

# for characters in(anna):
#     print(characters)
    
#     print(anna[0])
    
# name="harry" 

# print(name[1:4])  #include 1 and not 4

# print(name[len(name)-4:len(name)-2])   

# string is immutable

# STRING METHODS:

a="*** PrashANT ****"

print(a.upper())
print(a.lower())
print(a.rstrip("*")) # removes the trailing special characters
print(a.replace("PrashANT","Anna")) # replace all occurences of the string
print(a.split(" "))

heading= "my name is Prashant"

print(heading.capitalize()) # coverts the first letter to capital and rest all to small.

string1="Welcome to the land of Lord's to \"Himachal Pradesh\". " 
print(len(string1))
print(string1.center(100))
print(string1.count("a")) # no. of occurences of a character.
print(a.endswith("!!!")) # return true if it a endswith !!! else false
print(string1.endswith("to" ,1,10))
print(string1.find("to")) # returns the index of the starting character of the letter.
print(string1.index("to"))
string2="GAVhohdj246ybnj"
print(string2.isalnum()) # return true if string is alpha numeric else false.
print(string2.islower())
print(string2.isupper())
print(a.isprintable())
print(string2.isspace()) # if white spaces are present return true else false
print(string2.istitle()) # if  only first character is capital return true else false 
print(string2.swapcase())
print(string1.title()) # converts all the first characters of a letter to capital.


