#!/bin/bash
for fn in $(ls)
do
echo $fn
if [ -d $fn ]
then
    if [[ $fn == *"raman"* ]]
    then
    (cd $fn ; pwd ;  mpirun -np 48 vasp_vtst_std)
    fi
fi
done
