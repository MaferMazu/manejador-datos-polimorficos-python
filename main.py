from sys import exit
from polymorphic_type import PolymorphicType

def main():
    my_manager=PolymorphicType()
    print("*"*30)
    print("""Bienvenido al manejador de datos polimorficos :D Happy coding\n""")
    while True:
        my_input=input(">> ")
        elems=my_input.split(" ")
        command=elems[0]
        if command.upper()=="SALIR":
            exit(0)
        elif command.upper()=="DEF" and len(elems)>1:
            my_manager.assign_type(elems[1:])

        elif command.upper()=="TIPO" and len(elems)>1:
            my_manager.print_type(elems[1:])
        else:
            print_help()

def print_help():
    """ Print help for user """

    response="""- DEF <nombre> <tipo>

                Representa una definición del nombre en <nombre>,
                como un átomo que tiene asociado el tipo en <tipo>.

                Por ejemplo:

                • DEF x T define x teniendo tipo T.
                • DEF f t -> T define f teniendo tipo t -> T.
                • DEF g (a -> a) -> a define g teniendo tipo (a -> a) -> a.

                - TIPO <expr>

                Consulta el tipo de la expresión en <expr>, realizando la unificación
                necesaria y construyendo el tipo más general posible.

                Por ejemplo, considerando las definiciones en la sección anterior:
                • TIPO f imprime t -> T (o usando cualquier otra variable de tipo).
                • TIPO f x imprime T.
                • TIPO g f imprime T.

                - SALIR

                Salir del programa.\n"""

    print(response)


if __name__ == "__main__":
    
    main()