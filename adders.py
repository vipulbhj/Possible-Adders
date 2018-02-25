# A global array used to store all the possible pattern in the form of tuple.
p = []

"""
The use of this function is to check whether a given tuple exists in a set 
of tuples or not.
If it exists, then return true else false.
It takes two argument, first is tuple you want to verify in an orderless manner.
Second is the list of tuples to be checked.
"""
def verify(n,p):
    # n is going to be a tuple.
    # So to check whether there exists something , we  need to check all its 
    # elements and we will do that by checking whether 
    # 1 - Size of both is same or not.
    # 2 - if size is same , then there elements are same or not.


    # make n a list from a tuple.
    n = list(n)
    # p is a list of tuples.
    for i in p:

        if len(n) != len(i):
            continue
        else:
            # i is a tuple.
            # make it a list.
            j = list(i)
            for k in n:
                if k in j:
                    j.remove(k)

            if len(j) == 0:
                return True

    return False

"""
This function produces all the possible ways to repersent the adder of a number.

"""
def possibleAdders(num):
    poss = []
    # Just to handle crazy users
    if num == 1:
        return (1,)
    # This is going to be the base case.
    elif num == 2:
        return [(1,1)]
    else:
        c = possibleAdders(num-1)
        for i in c:
            j = list(i)
            addOne = tuple( [1]+j)
            check = verify(addOne,poss)
            if check == False:
                poss.append(addOne)
            for k in range(len(j)):
                copyJ = j[:]
                copyJ[k] += 1
                checkIn = verify(tuple(copyJ),poss)
                if checkIn == False:
                    poss.append(tuple(copyJ))


        return poss
                



def main():
    """one = (1,2)
    two = (9,9)
    three = (3,3)
    print(verify(one))
    print(verify(two))
    print(verify(three))"""

    # To be replaced by user input later.
    N = int(input("Enter a number you want to find the adders for:- ")) 
    p = possibleAdders(N)
    #print(p)

    #Lets make the code print the output in a preety manner.
    for i in p:
        i = list(i)
        i = list(map(str,i))
        s = "+".join(i)
        print(s)
    




if __name__ == "__main__":
    main()
