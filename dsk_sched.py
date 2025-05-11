"""
Autor: Oscar Vargas Pabon
Implementamos FCFS, SSTF, SCAN y C-SCAN
First Come First Serve (FCFS)
Shortest Seek Time First (SSTF)
"""
def calc_time( work:list[int] ) -> int:
	res:int = 0;
	for i in range(1,len(work)): res += abs( work[i] - work[i-1] );
	return res;
def FCFS( work:list[int], strt:int, limit:int=5000 ) -> tuple[int,list[int]]:
	# First Come First Serve
	reord = work.copy();
	reord.insert(0,strt);
	tm = calc_time( reord );
	return tm, reord;
def SSTF( work:list[int], strt:int, limit:int=5000 ) -> tuple[int,list[int]]:
	## Nota: Los 'ties' los resuelvo llendo al de más abajo
	am:int = len(work);
	reord = [strt]; us = [False for _ in range(am)];
	for _ in range(am):
		nxt = 0; nxt_val = float("inf");
		for i in range(am):
			if ( not us[i] and nxt_val > abs(strt-work[i]) ):
				nxt,nxt_val=i,abs(strt-work[i]);
		us[nxt] = True; reord.append( work[nxt] );
		strt = reord[-1]
	tm = calc_time( reord );
	return tm, reord;
def SCAN( work:list[int],strt:int,limit:int=5000 ) -> tuple[int,list[int]]:
	reord = [strt];
	disco = [0 for _ in range(limit)]
	for ld in work: disco[ld] += 1;
	for i in range(strt,limit):
		while ( disco[i] > 0 ):
			reord.append( i );
			disco[i] -= 1;
	reord.append( limit-1 );
	for i in range(limit-1,-1,-1):
		while ( disco[i] > 0 ):
			reord.append( i );
			disco[i] -= 1;
	tm = calc_time( reord )
	return tm, reord;
def C_SCAN( work:list[int],strt:int,limit:int=5000 ) -> tuple[int,list[int]]:
	reord = [strt];
	disco = [0 for _ in range(limit)];
	for ld in work: disco[ld] += 1;
	am:int = 0;
	for i in range(strt,limit):
		while ( disco[i] > 0  ):
			reord.append( i ); disco[i] -= 1; am += 1;
	reord.append( limit-1 );
	if ( am < len(work) ):
		reord.append( 0 );
		for i in range(limit):
			while ( disco[i] > 0 ):
				reord.append( i ); disco[i] -= 1;
	tm = calc_time( reord )
	return tm, reord;

if __name__ == '__main__':
	cr_1 = [10, 22,20, 2, 40, 6, 38]
	elevator_1 = [20,22,38,40,10,6,2]
	tm1,_ = FCFS(cr_1,20)
	tm2,_ = SSTF( cr_1,20 )
	tm3 = calc_time(elevator_1)
	print( "fcfs",tm1,"; sstf",tm2,"; elevator",tm3 )

	cr_2=[2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965]
	strt_2 = 2150
	tm4,_ = FCFS(cr_2,strt_2)
	tm5,_ = SCAN(cr_2,strt_2)
	tm6,_ = C_SCAN(cr_2,strt_2)
	print( "fcfs",tm4,"; scan",tm5,"; c-scan",tm6 )
	