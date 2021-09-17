#!/bin/bash
export VASP_RAMAN_RUN='mpirun -np 48 vasp_vtst_std'
export VASP_RAMAN_PARAMS='04_72_2_0.01'

python vasp_raman.py 
