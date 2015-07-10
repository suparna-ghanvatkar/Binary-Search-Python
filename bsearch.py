def bsearch(alist,item):
        if len(alist)==0:
            return -1
        else:
            mid=len(alist)/2
            if alist[mid]==item:
                return mid
            elif alist[mid]>item:
                pt=bsearch(alist[:mid],item)
                return pt
            elif alist[mid]<item:
                pt=bsearch(alist[mid:],item)
                if pt==-1:
                    return -1
                return mid+pt

no=0
a=[]
no=int(raw_input("Enter number of elements to search:"))
a=(raw_input("Enter the list:(separated by ',')").split(','))
alist=map(int,a)
num=int(raw_input("Enter the number to search:"))
res=bsearch(alist,num)
if res==-1:
    print "Element not found!"
else:
    print "Element found at pos ", res
