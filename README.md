# :sunny: Manejador de datos polimórficos

Este es un simulador de un manejador de datos polimórficos.

> Este manejador quedó incompleto sin embargo se logró:
> - Crear una estructura para almacenar los tipos y manipularlos
> - Cambiar los datos variables por los constantes (Ej: si eq : a -> a -> Bool y me preguntan tipo eq 1, eso me va a retornar Int -> Int -> Bool si 1 es Int)

> - La función DEF funciona
> - La función TIPO solo funciona si se le mete un argumento o varios (y que estos últimos sean constante).

## :computer: Requerimientos

Python3 and pip3.

Crear tu entorno virtual:

```shell
python3 -m venv env
```

Activar el entorno:

- Unix/macOS

```shell
source env/bin/activate
```

- Windows

```shell
./env\Script\activate
```

### Instalar requerimientos:

```shell
pip3 install -r requirements.txt
```

## :fire: Para correr

```shell
python3 main.py
```

## :bulb: Cómo usarlo

- DEF <nombre> <tipo>

Representa una definición del nombre en <nombre>, como un átomo que tiene
asociado el tipo en <tipo>.

Por ejemplo:

• DEF x T define x teniendo tipo T.

• DEF f t -> T define f teniendo tipo t -> T.

• DEF g (a -> a) -> a define g teniendo tipo (a -> a) -> a.

- TIPO <expr>

Consulta el tipo de la expresión en <expr>, realizando la unificación necesaria y
construyendo el tipo más general posible.

Por ejemplo, considerando las definiciones en la sección anterior:

• TIPO f imprime t -> T (o usando cualquier otra variable de tipo).

• TIPO f x imprime T.

• TIPO g f imprime T.

- SALIR

Salir del programa.

## :mag: Correr los tests

```shell
cd tests
coverage3 run --source=polymorphic_type -m unittest test_polymorphic.py
```

o


```shell
cd tests
coverage3 run --source=my_type -m unittest test_my_type.py
```

#### :star2: Coverage de los tests

```shell
coverage3 report -m
```

- Para el PolymorphicType:

| Module | Coverage |
|:----:|:--:|
| Memory Manager | 93% |


- Para el MyType:

| Module | Coverage |
|:----:|:--:|
| Memory Manager | 86% |