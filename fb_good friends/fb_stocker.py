import urllib.request, urllib.parse
import re

host = "https://www.facebook.com/"

stockers = input("Enter the stockers' id : ")
stockers_lst = re.findall('"([0-9]*)-',stockers)
print("Total IDs scanned : ",len(stockers_lst))
n = input("How many IDs do you want to see ? - ")
i=0
while i<int(n):
    fhand = urllib.request.urlopen(host+stockers_lst[i])
    j=0
    for line in fhand:
        j+=1
        if j==3:
            #print(line.decode())
            name = re.findall('"name":"([a-z A-Z]*)",',line.decode())
            if(len(name)>0):
                print(name[0])
                i+=1
            break
    
