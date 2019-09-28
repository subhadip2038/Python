# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:51:53 2019

@author: subha
"""
#diferent data types used in python
#Numbers
#String
#List
#Tuple
#Dictionary

#numbers, Different type of number variables.
var1 = 10
var2 = 12.5
var3 = 3+5j
print(var1)
print(var2)
print(var3)

#Strings, Different operations with strings
str = 'Hello World!'
print (str) # Prints complete string
print (str[0]) # Prints first character of the string
print (str[2:5]) # Prints characters starting from 3rd to 5th
print (str[2:]) # Prints string starting from 3rd character
print (str * 2) # Prints string two times
print (str + "TEST") # Prints concatenated string


#Lists, Different operations with lists
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list) # Prints complete list
print (list[0]) # Prints first element of the list
print (list[1:3]) # Prints elements starting from 2nd till 3rd
print (list[2:]) # Prints elements starting from 3rd element
print (tinylist * 2) # Prints list two times
print (list + tinylist) # Prints concatenated lists

#Tuple, Different operation
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print (tuple) # Prints complete tuple
print (tuple[0]) # Prints first element of the tuple
print (tuple[1:3]) # Prints elements starting from 2nd till 3rd
print (tuple[2:]) # Prints elements starting from 3rd element
print (tinytuple * 2) # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple

tuple[2] = 1000 # Invalid syntax with tuple
list[2]=1000 # Valid syntax with list
list # changed 3rd element 2.23 by 1000

#Python Dictionary, Dictionaries are enclosed by curly braces ({ }) 
#and values can be assigned and accessed using square braces ([]).
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (tinydict)
print (tinydict.keys()) # Prints all the keys
print (tinydict.values()) # Prints all the values

# nesting of lists and tuples as complex datatypes
NT =(1,2,("pop","rock"),(3,4),("disco",(1,2)))
NT[2]
NT[2][0]
NT[2][1]

#Append and Extend

list.extend(["pop",2]) # extend the list with two new entries
list
list.append(["pop",2]) # appends the list with another nested list
list


