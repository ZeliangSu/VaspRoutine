import os
import subprocess
import shutil

#subprocess.run('phonopy -d --dim="1 2 1"', shell=True, check=True)
#subprocess.run('phonopy --dim="1 2 1" --readfc --hdf5 --fc-symmetry --mesh="1 1 1" --eigenvectors"', shell=True, check=True)
#subprocess.run('phonopy --dim="1 2 1" --readfc --hdf5 --fc-symmetry --irreps="0 0 0"', shell=True, check=True)

# preparation
current_dir = os.path.dirname(os.path.abspath(__file__))
i = 0
j = 0
for fn in os.listdir(current_dir):
    # create sub-folder
    if 'POSCAR-0' in fn:
        new_dir =  os.path.join(current_dir, 'dis-%05d' % i)
        os.mkdir(new_dir)
        shutil.move(fn, os.path.join(new_dir,'POSCAR'))
        # copy INCAR POTCAR KPOINTS
        shutil.copy(os.path.join(current_dir, 'INCAR-step2'), os.path.join(new_dir, 'INCAR'))
        shutil.copy(os.path.join(current_dir, 'POTCAR'), os.path.join(new_dir, 'POTCAR'))
        shutil.copy(os.path.join(current_dir, 'KPOINTS'), os.path.join(new_dir, 'KPOINTS'))
        # shutil.copy(os.path.join(current_dir, 'vasp.slurm'), os.path.join(new_dir, 'vasp.slurm'))
        # shutil.copy(os.path.join(current_dir, 'vasp_raman.py'), os.path.join(new_dir, 'vasp_raman.py'))
        i += 1

    elif 'POSCAR_FC2' in fn:
        new_dir =  os.path.join(current_dir, 'dis_fc2-%05d' % j)
        os.mkdir(new_dir)
        shutil.move(fn, os.path.join(new_dir,'POSCAR'))
        # copy INCAR POTCAR KPOINTS
        shutil.copy(os.path.join(current_dir, 'INCAR-step2'), os.path.join(new_dir, 'INCAR'))
        shutil.copy(os.path.join(current_dir, 'POTCAR'), os.path.join(new_dir, 'POTCAR'))
        shutil.copy(os.path.join(current_dir, 'KPOINTS'), os.path.join(new_dir, 'KPOINTS'))
        # shutil.copy(os.path.join(current_dir, 'vasp.slurm'), os.path.join(new_dir, 'vasp.slurm'))
        # shutil.copy(os.path.join(current_dir, 'vasp_raman.py'), os.path.join(new_dir, 'vasp_raman.py'))
        j += 1
