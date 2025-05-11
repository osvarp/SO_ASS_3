"""
Autor: Oscar Vargas Pabon
Genero casos aleatorios xd
"""
import random

def generator( n:int, limit:int=5000 )->list[int]:
	cas = []
	for _ in range(n): cas.append( random.randint(0,limit-1) );
	return cas;

if __name__=="__main__":
	gen = generator(10,limit=2);
	print(gen)