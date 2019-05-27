# -*- coding: utf-8 -*-
"""
Created on Wed May  1 12:27:17 2019

@author: HP
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data={}
if rank == 0:
   for x in range(size):
       data[x]=(x+1)**x
   print ('we will be scattering:',data)
else:
   data = None
   
data = comm.scatter(data, root=0)

print ('rank',rank,'has data:',data)

newData = comm.gather(data,root=0)

if rank == 0:
   print ('master:',newData)
		