st_to_in={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10}
in_to_st={1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J"}
targets=[]
map1=[]
map2=[]
ships1=[]
ships2=[]


def input_convert(st):
    try:
        if len(st)==2:
            i=int(st[1])
            j=st[0]
        elif len(st)==3:
            i=int(st[1:3])
            j=st[0]
        else: raise Exception()
        if i not in range(1,11) or ord(j) not in range(ord('A'),ord('K')): raise Exception()
        return (j,i)
    except:
        return False