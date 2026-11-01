# ------------ Updating list using index ---------------

# nums = [10,20,30,40,50,60,70,80,90]
# nums[2] = 69   
# print(nums) Output : [10,20,69,40,50,60,70,80,90]

# ------------Printing list element using index ---------------

# nums = [10,20,30,40,50,60,70,80,90]
# print(nums[4]) Output: 50

# ------------ Printing list element using slicing ---------------

# nums = [10,20,30,40,50,60,70,80,90]
# print(nums[2::2])  List Slicing Output: [30, 50, 70, 90]

# ------------ Adding an element in the list's end using Append ---------------

# nums = [10,20,30,40,50,60,70,80,90]
# nums.append(100)
# print(nums)  Output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# ------------ Adding two lists using extend ---------------


# a = [1,2,3,4]
# b = [5,6,7,8]
# a.extend(b)
# print(a)  Output: [1, 2, 3, 4, 5, 6, 7, 8]

# ------------ Adding item in  lists using insert() ---------------

# a = [1,2,3,4]
# a.insert(2,69)
# print(a) Output : [1, 2, 69, 3, 4] 

# ------------ Adding a list item by using remove() ---------------

# a = [1,2,3,2,4]
# a.remove(2)
# print(a)  Output:  [1, 3, 2, 4] 

# ------------ Removing a list item by using pop() ---------------

# a = [1,2,3,2,4]
# print(f"base list: {a}")
# b = a.pop()
# c = a.pop(3)
# print(f"After a.pop() : {b}\n" ,f"After c.pop(3) : {c} \n")


# ------------ Removing a list item by using clear() ---------------

# a = [1,2,3,2,4] 
# a.clear()
# print(a)  Output:  [] 

# ------------ Finding the firsr occurence of the list item using index() ---------------


# a = [1,2,3,2,4] 
# print(a.index(2)) Output: 1

# ------------ Finding the firsr occurence of the list item using index() ---------------

# a = [1, 2, 3, 2]
# print(a.count(2)) Output: 2

# ------------ Arranging the string item into ascending order and into descending order usingt sort() ---------------

# a = [1, 2, 3, 2]
# a.sort()
# print(a)  Output: [1, 2, 2, 3]
# a.sort(reverse= True)
# print(a)  Output: [3, 2, 2, 1]

# ------------ Creating Shallow copy using copy() ---------------

# a = [1,2,3]
# b = a.copy()
# print(b)  Output: [1,2,3]

# ------------ Finding the number of elements in list using len() ---------------

# nums = [1,2,3]
# print(len(nums)) Output : 3

# ------------ Finding the maximum of elements in list using max() ---------------

# print(max([1,5,7,2])) Output : 7


# ------------ Finding the Minimum of elements in list using min() ---------------
 
# print(min([1,5,7,2])) Output: 1

# ------------ sorting the length using the sort() function ---------------

# nums = [4,1,3]
# print(sorted(nums)) Output: [1,3,4]

# ------------ List Comprehension ---------------

# squares = [x*x for x in range(5)]
# print(squares) Output: [0,1,4,9,16]