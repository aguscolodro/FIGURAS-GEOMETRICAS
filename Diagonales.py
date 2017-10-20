class Diagonales:

        def determinarFigura(self, cantidad):

            ND = (cantidad*(cantidad - 3)) / 2

            if ND == 0:
                figura='TRIANGULO'
            elif ND == 2:
                figura='CUADRILATERO'
            elif ND == 5:
                figura='PENTAGONO'
            elif ND == 9:
                figura='HEXAGONO'
            elif ND == 14:
                figura='HEPTAGONO'
            elif ND == 20:
                figura='OCTAGONO'
            elif ND == 27:
                figura='ENEAGONO'
            elif ND == 35:
                figura='DECAGONO'
            elif ND == 44:
                figura= 'UNDECAGONO'
            elif ND == 54:
                figura ='DODECAGONO'
            elif ND == 65:
                figura=' TRIDECAGONO'
            elif ND == 77:
                figura='TETRADECAGONO'
            elif ND == 90:
                figura='PENTADECAGONO'
            elif ND == 104:
                figura='HEXADECAGONO'
            elif ND == 119:
                figura=' HEPTADECAGONO'
            elif ND == 135:
                figura='OCTADECAGONO'
            elif ND == 152:
                figura = 'ENEADECAGONO'
            elif ND == 170:
                figura=' ISODECAGONO'
            else:
                figura='FIGURA MAYOR A 20 PUNTOS: Ingrese menor cantidad'

            return figura