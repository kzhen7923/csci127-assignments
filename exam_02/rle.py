def encode(string):
    l = list(string)
    whole_list = []
    i = 0
    while i in range(len(l)-1):
        sub_list = []
        sub_list.append(l[i])
        count = 1
        while l[i] == l[i+1]:
                i = i + 1
                count += 1
        sub_list.append(count)        
        whole_list.append(sub_list)
        i = i + 1
        
    return whole_list


print(encode("aacccddaa"))       
        
