# -*- coding: utf-8 -*-
"""
Created on Wed May  1 12:46:20 2019

@author: HP
"""

from mpi4py import MPI

def increm(b,n):
    data=[]
    for x in range(b,n):
      data.append((x+1)**x)
    return data

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data=[]
var=100/size

data_loc=increm(int(rank*var),int((rank+1)*var))
data =comm.allreduce(data_loc,op=MPI.SUM)

print(len(data))

if rank == 0:
   print ('master:')
		