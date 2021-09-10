#!/bin/bash
for fn in $(ls)
do
echo $fn
if [ -d $fn ]
then
	(cd $fn ; pwd ;  mpirun -np 48 vasp_vtst_std)
fi
done
