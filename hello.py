def count_substring(string, sub_string):
    noof=0 
    for i in range(len(string)):
        new_string=string[i:len(string)]
        if(new_string.startswith(sub_string)):
            noof+=1
    return noof

if __name__ == '__main__':
    string = input('enter string:').strip()
    sub_string = input('enter sub string:').strip()
    
    count = count_substring(string, sub_string)
    print(count)