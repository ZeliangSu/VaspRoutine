import os
import subprocess
import shutil

# preparation
current_dir = os.path.dirname(os.path.abspath(__file__))
i = 0
for fn in os.listdir(current_dir):
    # create sub-folder
    if 'raman-' in fn:
        # copy OUTCAR from these folders back to root
        shutil.copy(os.path.join(fn, 'OUTCAR'), os.path.join(current_dir, 'OUTCAR.%05d' % i))
        i += 1

