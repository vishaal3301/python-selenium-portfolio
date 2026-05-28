# [] is called slicing operator.
#  starting index 0.
# in str starting index is always 0.
name = "Vishaal"
print(name[1:3]) #is

text = "welcome"
print(text[:6]) #welcom #here starting index is NOT provided hence starting index by default is 0.
print(text[2:]) #lcome

#we can provide negative index also
print(text[1:-1]) #it will remove last character from str, hence output is elcom.
print(text[1:-2]) # it willl remove last two characters from str, hence output is elco.


