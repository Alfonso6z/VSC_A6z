"""
*    Ojetivo:
*        Eliminar espacios entre strings - fila
?    shortcut:
?        Ctrl + Shift + k
&    sepuede eliminar por bloque
"""



def sumar(a,b):
    """
    Nisi mollit culpa ullamco ullamco irure cillum ut culpa anim labore. Aute excepteur non esse fugiat cillum minim est reprehenderit non laboris culpa nulla. Enim commodo magna mollit adipisicing cillum velit cillum non veniam eiusmod. Tempor anim id do laborum adipisicing sint exercitation fugiat. Duis aliquip amet dolore pariatur excepteur esse adipisicing excepteur.

Voluptate enim in aliquip ut aliqua consequat ea cupidatat ex qui. Ea est deserunt officia minim incididunt. Cillum minim commodo dolor reprehenderit.

In incididunt quis eiusmod et excepteur qui. Sunt magna consectetur aliquip id deserunt velit. Duis sint irure ipsum non consequat cupidatat elit minim esse et reprehenderit cillum nostrud elit. Fugiat laborum cillum id sit tempor laborum labore tempor. Adipisicing minim ad reprehenderit sint est quis. Irure amet sunt incididunt consequat duis aliquip sunt ullamco laborum sunt est dolore anim. Ea eiusmod veniam eu ullamco irure veniam.

Eu sit Lorem do anim ut officia. Aliqua do ullamco anim commodo ut. Nisi ad esse nisi do commodo ipsum et nostrud adipisicing esse fugiat irure voluptate. Deserunt fugiat proident quis proident amet veniam velit.

Nulla aliquip esse irure quis elit. Sint nulla laboris quis excepteur adipisicing non anim nulla anim ullamco. Est culpa esse nulla dolor et excepteur labore occaecat duis excepteur ipsum consequat. Est in enim proident dolore elit anim consectetur id aute. Amet mollit minim voluptate amet id velit deserunt laborum velit velit magna ut. Velit nulla est mollit eu minim Lorem aliqua Lorem ullamco adipisicing cillum consectetur.

Aliqua labore aliqua culpa consequat qui excepteur ullamco velit minim tempor tempor officia aute. Aliquip occaecat ut nostrud deserunt minim reprehenderit. Do laboris fugiat duis dolore aliqua excepteur laborum nulla id minim dolor sunt. Cupidatat consequat aliquip velit ea velit laboris.

Excepteur eu est culpa aute. Officia id mollit amet irure esse sunt laborum qui do commodo. Cillum quis officia dolore consectetur eu nostrud irure et nulla irure reprehenderit aliqua. Nostrud ullamco eiusmod reprehenderit sint ad aute eiusmod proident ea enim minim.

Est irure do culpa sunt in do cillum consectetur cillum. Culpa minim nostrud ad eu nulla sint nisi nisi aute magna qui voluptate. Labore est ut esse occaecat excepteur mollit veniam magna proident et. Sit ex elit sint irure cupidatat Lorem magna nulla.

Do fugiat labore aliqua in sint nostrud adipisicing ut aute veniam pariatur exercitation. Magna aliquip labore ea id ex in nulla in nulla magna excepteur ad. Magna consequat reprehenderit est dolor irure exercitation minim aute ipsum nisi ex occaecat exercitation.

Aliqua ullamco nisi ex ea sint consequat deserunt. Proident sint reprehenderit ullamco proident veniam occaecat anim aliquip ad. Aute tempor duis duis et et nostrud eiusmod aute reprehenderit labore. Esse anim magna est sint nulla ea elit in tempor amet do. Reprehenderit irure ex tempor cupidatat reprehenderit irure Lorem duis pariatur duis reprehenderit.
    """
    return a + b

def saludar(nombre):
    return f"Hola {nombre}"

def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n

def area(a,b):
    return a*b

def fib(n):
    # fibonacci
    # fibonnaci
    # definición: la suma de los 2 anteriores
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n>1:
        return fib(n-2) + fib (n-1)
    else:
        print("Ingresa un número positivo")