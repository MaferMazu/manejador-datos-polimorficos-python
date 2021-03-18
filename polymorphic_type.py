import json
from my_type import read_type, MyType, to_str

class PolymorphicType:
    def __init__(self):
        self.memory=Memory()

    def __str__(self):
        return str(self.memory)

    def assign_type(self,my_input:list) -> int:
        var=my_input[0]
        index,elem=self.search_var(var)
        my_type,error=read_type(my_input[1:])
        if isinstance(my_type,MyType):
            self.memory.add(var,my_type,index)
            print("Se definio '"+var+"' con tipo "+str(my_type))
            return 0
        else:
            print("ERROR, "+error)
            return 1

    def print_type(self,array):
        my_types=[]
        for var in array:
            index,elem=self.search_var(var)
            if index<0:
                print("ERROR,el nombre '"+var+"' no ha sido definido")
                return 1
            else:
                my_types.append(elem[1])

        external_f=my_types[0]
        if len(my_types)>1:
            for i in range(1,len(my_types)):
                if external_f[0]=="funcion":
                    if external_f[1][0][0]=="variable" and my_types[i][0]=="constante":
                        var=external_f[1][0][1][0]
                        const=my_types[i][1][0]
                        self.memory.change_var(var,const,my_types[0])

        arr=my_types[0]
        string=to_str("",arr)
        print(str(array[0])+": "+string)
        return string

    def search_var(self,name):
        memory=self.memory.raw()
        for i in range(len(memory)):
            elem=memory[i]
            if elem[0]==name:
                return i,elem
        return -1,None


class Memory:
    def __init__(self):
        self.mem=[]

    def add(self,var:str,my_type:MyType,index=-1):
        raw_type=my_type.raw()
        if 0<index<len(self.mem):
            self.mem[index]=[var,raw_type]
        else:
            self.mem.append([var,raw_type])

    def __str__(self):
        return json.dumps(self.mem)

    def raw(self):
        return self.mem

    def change_var(self,var,const,array):
        extern_type=array[0]
        my_var=array[1]
        if extern_type=="variable" and my_var[0]==var:
            array[0]="constante"
            array[1]=[const]
            
            return 0

        elif extern_type=="funcion":
            str_dominio=array[1][0]
            str_imagen=array[1][1]
            self.change_var(var,const,str_dominio)
            self.change_var(var,const,str_imagen)

            return 0

init=PolymorphicType()
response=init.assign_type(["1","Int"])
response=init.assign_type(["eq","a","->","Bool","->","Int"])
response=init.assign_type(["eq","a","->","a","->","Bool"])
init.print_type(["eq","1"])
# init.print_type(["1"])
