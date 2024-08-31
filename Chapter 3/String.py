str1 = "Sushree"
str2 = 'Sangeeta'
str3 = '''Priyadarsini'''

# String is immutable which means that you cannot change them by running function on them
# String can be sliced to get a part of the string
# For counting the index of the string in normal we start counting from 0 to length-1 
# For reverse counting we start counting -1 to -length from end
 
print(str1[0:3])
print(str1[-4:-1])
print(str1[3:6])
print(str1[:7])  #same as print(str1[0:7])
print(str1[0:])  #same as print(str1[0:7])

print(str2[1:7:2])  #print letter lefting by 2 letters 


