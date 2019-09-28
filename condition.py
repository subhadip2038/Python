# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 22:35:49 2019

@author: subha
"""
age=17
if(age >18):
    print("you can enter")
else:
    print("move on")

amount=int(input("Enter amount: "))
if amount<1000:
 discount=amount*0.05
 print ("Discount",discount)
elif amount<5000:
 discount=amount*0.10
 print ("Discount",discount)
else:
 discount=amount*0.15
 print ("Discount",discount)
print ("Net payable:",amount-discount)


years = list(map(str, range(1980,2014)))
