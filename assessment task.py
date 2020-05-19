#assessment task(counting occurances of char in string)
from collections import Counter

#implement a funtion to count occurances of char in string
def charocur():
    count_list = []
    n = "The new patients were an 18-year-old female student who returned from Britain on Friday, "\
        "and a 61-year-old man whose granddaughter and domestic helper was infected previously, "\
        "according to Dr Chuang Shuk-kwan, head of the Centre for Health Protection’s communicable disease branch."
    
#use built-in container Counter to count
    c = Counter(n)
#store all the ele of c in list 'l'
    l = list(c)

#append all the appeared ele and their occurances in count_list
#l[ele] referring to each ele stored in list 'l'
#c[l[ele]]=c[the picked ele], use to show the count of the picked ele
    for ele in range(len(c)):
        count_list.append([l[ele], c[l[ele]]])

#return result
    return count_list
    
#call & display charocur function
print(charocur())