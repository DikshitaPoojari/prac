""" def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return
   
printme("I'm first call to user defined function!")
printme("Again second call to the same function")
 """

# call by value

# def changeme( mylist ):
#    "This changes a passed list into this function"
#    print("Values inside the function: ", mylist)
#    mylist.append([1,2,3,4]);
#    return

# # calling changeme function
# mylist = [10,20,30];
# changeme( mylist );
# print("Values outside the function: ", mylist)


# call by refrenece
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print("Values inside the function: ", mylist)
   return

mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)
