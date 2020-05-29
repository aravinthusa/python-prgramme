program:

string_name=input("enter the string:")
def most_frequent(string_name):
    string_dict={}
    
    for element in string_name:
        if element in string_dict:
            a=string_dict.get(element)
            a=int(a)+1
            b="0"+str(a)
            string_dict[element]=b
        else:
            b='01'
            string_dict[element]=b
    for j in sorted(string_dict,key=string_dict.get, reverse=True):
        print (j+ "=" + str(string_dict[j]))
        
most_frequent(string_name)

output:

enter the string:mississippi
i=04
s=04
p=02
m=01
