import os
import subprocess
import shutil

# preparation
current_dir = os.path.dirname(os.path.abspath(__file__))
i = 0
for fn in os.listdir(current_dir):
    # create sub-folder
    if 'Raman-POSCAR' in fn:
        new_dir =  os.path.join(current_dir, 'raman-%05d' % i)
        os.mkdir(new_dir)
        shutil.move(fn, os.path.join(new_dir,'POSCAR'))
        # copy INCAR POTCAR KPOINTS
        shutil.copy(os.path.join(current_dir, 'INCAR-step3'), os.path.join(new_dir, 'INCAR'))
        shutil.copy(os.path.join(current_dir, 'POTCAR'), os.path.join(new_dir, 'POTCAR'))
        shutil.copy(os.path.join(current_dir, 'KPOINTS'), os.path.join(new_dir, 'KPOINTS'))
        # shutil.copy(os.path.join(current_dir, 'vasp.slurm'), os.path.join(new_dir, 'vasp.slurm'))
        # shutil.copy(os.path.join(current_dir, 'vasp_raman.py'), os.path.join(new_dir, 'vasp_raman.py'))
        i += 1

