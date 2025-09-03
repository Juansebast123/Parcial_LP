Este programa implementa una calculadora que procesa expresiones aritméticas desde un archivo de texto (operaciones.txt) utilizando Flex (analisis lexico) y Bison (analisis sintactico).

La calculadora soporta las siguientes operaciones:
- Suma: +
- Resta: -
- Multiplicacion: *
- Division: /
- Valor absoluto: abs()
- Raiz cuadrada: sqrt()

lex (.l)
- Se encarga de reconocer los tokens (numeros, operadores y funciones como abs y sqrt) y pasarlos al parser.
- Debe incluir calculadora.tab.h para conocer los tokens generados por Bison.

Bison (.y)
- Define la gramatica de las expresiones y como evaluarlas.
- Implementa reglas para manejar operaciones aritmeticas, valores absolutos y raices cuadradas.
- El main abre el archivo pasado como argumento (operaciones.txt) y llama al parser.

Archivo de entrada (operaciones.txt)
- Contiene una operacion por línea.

