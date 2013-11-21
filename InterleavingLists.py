## Author: Jose F. Martinez Rivera
## Student Number: 802-10-4088
## Course: ICOM4036 - 040
## Professor: Dr. Wilson Rivera
## Hand-In Date: March 12, 2013

#2. Write a program that implements two functions: 
#   AllInter(a,b) and ParallelInter(a,b) where a and b
#   are two lists and the function AllInter returns a list
#   containing all the interleaving, while ParallelInter returns
#   the parallel interleaving. The two input lists may or may not
#    be of equal length. For example:


#Interleaves two lists in a parallel manner
#>> ParallelInter( [1, 2], [3, 4]) 
#[1, 3, 2, 4]
def ParallelInter(a,b):
        if not a:
                return b
        if not b:
                return a
        else:
                return [a[0], b[0]] + ParallelInter(a[1:len(a)],b[1:len(b)])


#All possible interleavings of two lists
# >>AllImter([1, 2], [3, 4])
#[[1,2,3,4], [1,3,2,4], [1,3,4,2], [3,1,2,4], [3,1,4,2], [3,4,1,2]]
def AllInter(a,b):
        if not a:
                return [b]
        if not b:
                return [a]
        else:

                xList = AllInter(a[1::], b[0::])
                xList = prepend(a[0], xList)

                yList = AllInter(a[0::], b[1::])
                yList = prepend(b[0], yList)
               
                return xList + yList

#Used for AllInter, it prepends an element to a list
def prepend(a, aList):

        for i in range(0,len(aList)):
                aList[i].insert(0,a)
        return aList


