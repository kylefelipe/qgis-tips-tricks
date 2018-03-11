# -*- coding: utf-8 -*-
'''
Created on 9 de mar de 2018

@author: Jorge Luiz Santos
'''
import sys 
from curses.ascii import isdigit

def uso():
    sys.stderr.write ('Digite apenas numeros\n')
    sys.stderr.write ('''
    Uso:
        gridpoints <x0> <y> <número de colunas> <número de linhas> <distância>
    Onde: origem = canto superior esquerdo
        x0                 => Float para coordenada X inicial;
        y0                 => Float para coordenada Y inicial;
        número de colunas  => Inteiro para o número de colunas;
        número de linhas   => Inteiro para o número de linhas;
        distância          => Float para distância entre os pontos do grid
    ''')
    sys.exit(1)

def verificaArgumentos():
    if len(sys.argv) != 6:
        uso()
    
    for i in range(1, len(sys.argv)): 
        try:
            float(sys.argv[i])
        except ValueError:
            sys.stderr.write('Erro no parâmetro %i: %s\n' %(i, sys.argv[i]))
            return False
    
    return True
    

def gridPoints(coordIni, numCol, numRow, dist):
    x0,y0 = coordIni
    
    sys.stdout.write("X,Y\n")
    for row in range(numRow):
        for col in range(numCol):
            sys.stdout.write('%.3f,%.3f\n'%(x0 + col * dist, y0 - row * dist))
            
            
def main():
    if not verificaArgumentos():
        uso()
        sys.exit(1)
        
    coordIni = (float(sys.argv[1]), float(sys.argv[2]))
    numCol = int(sys.argv[3])
    numRow = int(sys.argv[4])
    dist = float(sys.argv[5])
    
    gridPoints(coordIni, numCol, numRow, dist)
    
    sys.stderr.write('Programa terminado\n')
    sys.exit(0)
    
if __name__ == "__main__":
    main()
