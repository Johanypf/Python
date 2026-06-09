'''
/*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */
'''


def isValid_2(s: str) -> bool:
    stack = []
    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for caracter in s:

        if caracter in '([{':
            stack.append(caracter)

        elif caracter in ')]}':

            if not stack:
                return False

            if stack[-1] != pares[caracter]:
                return False

            stack.pop()

  
    return len(stack) == 0

print(isValid_2("{ [ a * ( c + d ) ] - 5 }"))