def get_jaccard_sim(str1, str2):

    str1=str1.replace('/',' ')
    str2=str2.replace('/', ' ')
    a = set(str1.split())
    b = set(str2.split())

    print(a)
    print(b)
    c = a.intersection(b)
    print(str(float(len(c)) / (len(a) + len(b) - len(c))))
    return float(len(c)) / (len(a) + len(b) - len(c))

def get_jaccard_sim_advanced(alertlist):

    uniquealert=[]
    cleanlist=[]
    for alert in alertlist:
        cleanlist.append(''.join([i for i in alert if not i.isdigit()]))
    print(cleanlist)
    print('cleanlist length:' + str(len(cleanlist)))
    uniquealert.append(cleanlist[0])
    for alert1 in cleanlist:
        if alert1 in uniquealert:
            continue
        else:
            for alert2 in cleanlist:
                if alert2 in uniquealert:
                    continue
                else:
                    print("jacard sim:")
                    #print(get_jaccard_sim(alert1,alert2))
                    if get_jaccard_sim(alert1,alert2) ==1.0:
                        continue
                    else:
                        if alert2 not in uniquealert:
                            uniquealert.append(alert2)
                            print("printing uniquealert: "+str(uniquealert))

    print('uniquelist')
    print(uniquealert)
'''
    a = set(newstr.split('/'))
    b = set(newstr2.split('/'))
    if not len(b)>1:
        b=set(str2.split())
    else:
        print("length is less than 1")
    print(a)
    print(b)
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))
'''

def main():
    string1='mrtprod/gigabus/abc/pqr failed for 2018/10/3'
    string2='mrtprod/gigabus/abc/pqr failed for 2018/11/3'
    listofalert = []
    listofalert.append('mrtprod/gigabus/abc/pqr failed for 2018/10/3')
    listofalert.append('mrtprod/gigabus/abc failed for 2018/10/3')
    listofalert.append('mrtprod/gigabus/abc/pqr failed for 2018/12/3')
    listofalert.append('mrtprod/gigabus/ failed for 2018/10/3')
    listofalert.append('mrtprod/gigabus/abc/pqr failed for 2018/13/3')
    listofalert.append('mrtprod/gigabus/abc/pqr/lmn/pqr failed for 2018/10/3')
    listofalert.append('mrtprod/gigabus/abc/pqr failed for 2018/14/3')
    listofalert.append('mrtprod/gigabus/abc/pqr/lmn failed for 2018/1/3')
    listofalert.append('mrtprod/gigabus/abc/pqr/obj failed for 2018/10/3')
    listofalert.append('mrtprod/gigabus/abc/pqr failed for 2018/10/3')
    listofalert.append('mrtprod/gigabus/abc/pqr failed for 2018/09/3')
    print('list of alert length:'+str(len(listofalert)))
    get_jaccard_sim_advanced(listofalert)

   #print(get_jaccard_sim(string1,string2))

main()