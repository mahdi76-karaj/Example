### Python3 program for the
### practical application of reverse()
##
##list1 = [1, 2, 3, 2, 1]
##
### store a copy of list
##list2 = list1.copy()
##
### reverse the list
##list2.reverse()
##
### compare reversed and original list
##if list1 == list2:
##	print("Palindrome")
##else:
##	print("Not Palindrome")
##print(list1)
##print(list2)

mylist = [0,4,5,1,5,6,7,8,3,5]

mylist.sort(reverse=True)
print(mylist)


mylist_words = ["a","d","r","d","eed","t","y"]

mylist_words.sort(reverse=True)
print(mylist_words)


