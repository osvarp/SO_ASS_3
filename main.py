"""
Autor: Oscar Vargas Pabon

"""
import sys

from generate_cases import generator
from dsk_sched import FCFS,SSTF,SCAN,C_SCAN
from visualizer import printTable,see_work
algo = [FCFS,SSTF,SCAN,C_SCAN]
alg_nm = ["FCFS","SSTF","SCAN","C_SCAN"]


def main():
	strt = int(sys.argv[1]) if len(sys.argv)>1 else 0
	sz = int(sys.argv[2]) if len(sys.argv)>2 else 1000
	limit = int(sys.argv[3]) if (len(sys.argv)>3) else 5000
	work = generator(sz,limit=limit)
	alg_tm = []; alg_reord = [];
	for alg in algo:
		tm,reord = alg(work,strt,limit=limit)
		alg_tm.append(tm); alg_reord.append(reord);

	meta = [(nm,20) for nm in alg_nm]
	printTable(meta,[alg_tm],title="Tiempos de los algoritmos (medido en cilindros)")

	for i in range(len(algo)):
		see_work(alg_reord[i],alg_nm[i],limit=limit)


if __name__=="__main__":
	main()