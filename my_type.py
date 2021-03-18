def read_type(my_input:list):
    """ Super important function that creates objects MyType for use
    input: list
        Array like ["a","->","Bool"]
    output: MyType
        Structure like ["funcion", [["variable", ["a"]], ["constante", ["Bool"]]]"""
    
    if len(my_input)<1:
        return None,"no se encontró un tipo"

    # For parenting
    count=0
    with_parenting=False
    ini=0
    fin=0
    for i in range(len(my_input)):
        if my_input[i]=="(":
            count=count+1
            if not with_parenting:
                with_parenting=True
                ini=i
        elif my_input[i]==")":
            count=count-1
        if count==0 and with_parenting:
            fin=i
            break

    # If i have parenting
    if with_parenting:
        try:
            if my_input[fin+1]=="->":
                try:
                    dominio,error1=read_type(my_input[ini:fin])
                    imagen,error2=read_type(my_input[fin+2:])
                    if error1 or error2:
                        return None,error1+" "+error2
                    return MyType("funcion",[dominio.raw(),imagen.raw()]),""
                except:
                    return None,"no definio la imagen de la funcion"
        except:
            try:
                dominio,error=read_type(my_input[ini:fin])
                if error:
                    return None,error
            except:
                return None,"error"

    # If i dont have parenting but i have a function
    for i in range(len(my_input)):
        if my_input[i]=="->":
            try:
                dominio,error1=read_type(my_input[:i])
                imagen,error2=read_type(my_input[i+1:])
                if error1 or error2:
                    return None,error1+" "+error2
                return MyType("funcion",[dominio.raw(),imagen.raw()]),""
            except:
                return None,"no definio la imagen de la funcion"

    # If my type is a variable or constante
    for i in range(len(my_input)):
        if my_input[i][0].islower():
            return MyType("variable",[my_input[i]]),""
        elif my_input[i][0].isupper():
            return MyType("constante",[my_input[i]]),""


class MyType:
    def __init__(self,my_type,args):
        """ Function that init MyType
        Example: ["constante",["Int"]]
            Represents Int
        Example 2: ["funcion", [["funcion", [["variable", ["a"]], ["constante", ["Bool"]]]], ["constante", ["Int"]]]]]
            Represets (a -> Bool) -> Int"""
        self.my_type=[my_type,args]

    def __str__(self):
        """ Function to print my type for humans """
        string=to_str("",self.my_type)
        if self.my_type[0]=="funcion":
            string=string[1:-1]
        return string

    def raw(self):
        """ Return a array with info about my type """
        return self.my_type

def to_str(string,array):
        """ Create recursive string to print in str """
        extern_type=array[0]
        if extern_type=="constante" or extern_type=="variable":
            str_type=array[1][0]
            string=string+str_type
            return string

        elif extern_type=="funcion":
            str_dominio=array[1][0]
            str_imagen=array[1][1]
            str_type = "("+to_str("",str_dominio)+" -> " + to_str("",str_imagen)+")"
            string=string+str_type
            return string
# response,error=read_type(["(","a","->","a",")","->","Bool"])
# print(response)
# response.change_var("a","Int",response.raw())
# print(response)