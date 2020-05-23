# Programa simples para auxiliar na conversão de rumo em azimute e vice-versa, fazendo operações entre graus

# Funções que realizam as operações:

# Função que soma os graus:

def soma(g1, m1, s1, g2, m2, s2):
    g3 = g1 + g2
    m3 = m1 + m2
    s3 = s1 + s2

    if s3 > 60:
        s3 -= 60
        m3 += 1
    if m3 > 60:
        m3 -= 60
        g3 += 1
    print(f"A soma  é: {g3}º {m3}' {s3}\"")


# Função que subtrai os graus:

def menos(g1, m1, s1, g2, m2, s2):
    if s2 > s1:
        m1 -= 1
        s1 += 60
    if m2 > m1:
        g1 -= 1
        m1 += 60
    s3 = s1 - s2
    m3 = m1 - m2
    g3 = g1 - g2

    if s3 > 60:
        s3 -= 60
        m3 += 1
    if m3 > 60:
        m3 -= 60
        g3 += 1

    print(f"A subtração  é: {g3}º {m3}' {s3}\"")


# Função que multiplica os graus por um número inteiro:

def mult(g1, m1, s1):
    multiplicador = int(input("Digite o multiplicador: "))
    soma = 0
    soma1 = 0

    s3 = s1 * multiplicador
    if s3 >= 60:
        soma = s3 // 60
        s3 = s3 % 60

    m3 = (m1 * multiplicador) + soma
    if m3 >= 60:
        soma1 = m3 // 60
        m3 = m3 % 60
    g3 = (g1 * multiplicador) + soma1

    print(f"O resultado  é: {g3}º {m3}' {s3}\"")

# Função principal em que o programa chamará as funções para realizar as operações:

def main():
    ope = str(input('''Digite:
         + para adição;
         - para subtração;
         x para multiplicação ou;
         Digite "sair" para sair.
             '''))

    while ope != "sair":

        if ope == '+':
            g1 = int(input("Graus: "))
            m1 = int(input("Minutos : "))
            s1 = int(input("Segundos: "))

            print("E:")

            g2 = int(input("Graus: "))
            m2 = int(input("Minutos : "))
            s2 = int(input("Segundos: "))

            soma(g1, m1, s1, g2, m2, s2)

            ope = str(input('''Digite:
                    + para adição;
                    - para subtração;
                    x para multiplicação ou;
                    Digite "sair" para sair.
                                    '''))
        if ope == '-':
            g1 = int(input("Graus: "))
            m1 = int(input("Minutos : "))
            s1 = int(input("Segundos: "))

            print("E:")

            g2 = int(input("Graus: "))
            m2 = int(input("Minutos : "))
            s2 = int(input("Segundos: "))

            menos(g1, m1, s1, g2, m2, s2)

            ope = str(input('''Digite:
                    + para adição;
                    - para subtrção;
                    x para multiplicação ou;
                    Digite "sair" para sair.
                                    '''))
        if ope == 'x':

            g1 = int(input("Graus: "))
            m1 = int(input("Minutos : "))
            s1 = int(input("Segundos: "))

            mult(g1, m1, s1)

            ope = str(input('''Digite:
                    + para adição;
                    - para subtração;
                    x para multiplicação ou;
                    Digite "sair" para sair.
                                    '''))

main()
