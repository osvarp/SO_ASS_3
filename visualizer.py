"""
Autor: Oscar Vargas Pabon
Visualizando esa cosa
"""

import matplotlib.pyplot as plt

def see_work( work:list[int],name:str="-_-", limit:int=5000 ) -> None:
	plt.plot( [i for i in range(len(work))],work );
	plt.gca().set_ylim([0,limit])
	plt.ylabel( "Cilindros" ); plt.xlabel( "Requests" );
	plt.title( name )
	plt.show();

def printTable( metaData:list[tuple], data:list[tuple], numerated:bool=False, title:str="", fun=lambda c:c.__str__() ) -> None:
	"""
	Imprime una tabla ascii que muestra ciertos datos.

	Parameters
	----------
	metaData : Informacion sobre los encabezados de la tabla. Vienen en el formato (cad,len) donde 
				cad es el titulo del encabezado y len es la cantidad de caracteres que tiene la columna.
	data : los datos organizados en [f1,f2,...,fk] donde fi son los datos referentes a una fila de la
				tabla.
	numerated : toma valor 'True' si se quiere tener una columna que enumere las filas
	title : El titulo de la tabla
	fun : La funcion con la que se va a convertir a cadena los datos en 'data'
	"""
	assert(len(data) >0 )
	assert( len(metaData) == len(data[0]) ) # esta condicion se debe cumplir para todo i valido
	myPad = lambda cad,width: ' '*((width-len(cad))//2)+cad+' '*((width-len(cad)+1)//2)
	# construyo la linea separadora
	line = ['+']
	if ( numerated ):
		line.append( '-'*5 );
		if ( title != '' ):
			print(line[-1],end='-');
		line.append('+');
	for name,length in metaData:
		line.append( '-'*length );
		if ( title!='' ):
			print(line[-1],end='-')
		line.append('+');
	line = "".join(line);
	# imprimo el titulo
	if ( title ):
		print('-')
		print("|%s|" % ( myPad(title,len(line)-2) ));
	print( line );

	# imprimo los encabezados
	print('|',end='');
	if ( numerated ):
		print( "%s" %(myPad('#',5)),end='|' )
	for name,length in metaData:
		print( "%s" %(myPad(name,length)) ,end= '|' );
	print()
	print(line);
	
	# imprimo los datos
	for row in range(len(data)):
		print('|',end='');
		if ( numerated ):
			print( "%s"%(myPad(str(row+1),5)),end='|' );
		for ind in range(len(data[row])):
			pnt = fun(data[row][ind]);
			print("%s"%(myPad(pnt,metaData[ind][1])),end='|');
		print()
		print(line);