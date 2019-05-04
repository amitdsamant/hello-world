def bubblesort(theseq):
    n = len(theseq)
    print('length of the string',n)
    for i in range(n-1):
        print('i:',i)
        for j in range(n -1 -i):
            print(i+n-1)
            print('j:',j)
            if theseq[j] > theseq[j+1]:
                tmp = theseq[j]
                print('theseq[j]',theseq[j])
                print('theseq[j+1]',theseq[j+1])
                print('tmp:',tmp)
                theseq[j]=theseq[j+1]
                theseq[j+1]=tmp
    return theseq
if __name__ == '__main__':
    newlist = bubblesort([7,4,1,3,3])
    print(newlist)
