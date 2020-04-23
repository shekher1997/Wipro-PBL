string = 'black-red-green-yellow-crimson-plum-vermilion-burgundy-turquoise-beige-cyan'

def stringSorter (string):
    n = string.count('-') + 1
    stringList = ['']*n
    i = 0
    for letters in string:
        if (letters != '-'):
            stringList[i] = stringList[i] + letters
        else:
            i += 1
    stringList.sort()
    del string
    string = ""
    for  i in range(0,len(stringList),1):
        string = string + stringList[i]
        if(i != len(stringList)-1):
            string = string + "-"
    del stringList
    return(string)
    

print("Input: ",string,end="\n\n")
print("Output: ",stringSorter(string),end="\n\n")