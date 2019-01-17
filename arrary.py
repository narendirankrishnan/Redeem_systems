'''
Create an arrary of 5 integer and display them
'''
#
# from array import *
#
# array_num = array('i', [1, 3, 5, 7, 9])
#
# for i in array_num:
#     print(i)
#
# print("accessing 1st 4 items indivudially.")
#
# print(array_num[0])
# print(array_num[1])
# print(array_num[2])
# print(array_num[3])

'''
Append a new item to the end of the array
'''
#
# from array import *
#
# array_n = array('i', [1, 3, 5, 7, 9])
# print("original array:" + str(array_n))
#
# print("Now add number 13 to the end of array")
#
# array_n.append(13)
#
# print("New array: " + str(array_n))

'''
Reverse the order of the items in the array
'''
#
# from array import *
#
# array_n = array('i', [1, 3, 5, 7, 9, 11, 13, 15, 17])
#
# print("Original array: " + str(array_n))
# array_n.reverse()
#
# print("Reveresed order of item is: ", str(array_n))
#
# print(len(array_n))
# a = len(array_n) / 2
# print(a)
#
# import array as arr
#
# number = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
#
# number[0] = 0
# print(number)
# number[5] = 111
# print(number)
# number.insert(7, 555)
# print(number)

# from array import *
#
# def reverse(aList):
#     # end = len(aList)
#     end = len(aList)-1
#     limit = int(end/2) + 1
#     for i in range(end):
#         aList[i], aList[end] = aList[end], aList[i]
#         end = end -1
#     return aList
# a = [1, 3, 4, 5, 6, 7]
# array_n = array('i', [1, 3, 5, 7, 9, 11, 13, 15, 17])
# print(reverse(array_n))

'''
Get the length in bytes of one array item in the internal representation
'''
#
# from array import *
#
# array_n = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(str(array_n))
# print(str(array_n.itemsize))

'''
Get the current memory address and the length in elements of the buffer used to hold an array’s contents
'''

# from array import *
#
# array_i = array('i', [1, 2, 3, 4, 5, 6 ,7])
# print("current memory address" +str(array_i.buffer_info()))
# print("size of the memory in bytes: "+str(array_i.buffer_info()[1] * array_i.itemsize))

'''
Get the number of occurrences of a specified element in an array
'''

# from array import *
#
# array_i = array('i', [7, 2, 7, 4, 7, 6, 7])
#
# print("Num of occourance of 7 in a array: " + str(array_i.count(7)))

'''
Append items from inerrable to the end of the array
'''

# from  array import *
#
# array_1 = array('i', [1, 3, 5, 7, 9])
#
# print("Original array: "+ str(array_1))
#
# array_1.extend(array_1)
# array_1.extend(array_1)
#
# print("Extended array: "+str(array_1))

'''
Convert an array to an array of machine values and return the bytes representation
'''

# from array import *
#
# print("Bytes to string: ")
# x = array('b', [119, 51, 114, 101,  115, 111, 117, 114, 99, 101])
# s = x.tobytes()
# print(s)

'''
Append items from a specified list
'''

# from array import *
#
# num_list = [1, 2, 6, -8]
# array_num = array('i', [])
#
# print("Items in the list: " + str(num_list))
# print("Append items to list: ")
# array_num.fromlist(num_list)
#
# print("Items in the array: " + str(array_num))

'''
Inset a new item before the second element in a existing array
'''

# from array import *
#
# array_i = array('i', [1, 2, 3, 4, 5])
#
# array_i.insert(2, 555)
#
# print(array_i)

'''
Remove a specific item using the index from an array
'''

# from array import *
#
# array_1 = array('i', [1, 2, 3, 4, 5, 6 , 7])
#
# array_1.pop(4)
# print("popped 5th element", array_1)

'''
Remove the 1st occurrence of specified element from an array
'''
#
# from array import *
#
# array_nu = array('i', [1, 2, 3, 5, 3, 7, 1, 9, 3])
#
# print("Remove the 1st occurance of 3 in an array.")
#
# array_nu.remove(3)
# print("New Array "+str(array_nu))

'''
Convert an array to an ordinary list with the same items
'''

# from array import *
#
# array_m = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
#
# num_list = array_m.tolist()
# print(num_list)