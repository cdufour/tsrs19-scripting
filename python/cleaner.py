# cleaner.py
import os

source_dir = './files'
destination_dir = './danger'

files = os.listdir(source_dir)

for f in files:
    if f[-3:] == "exe":
        os.rename(source_dir + '/' + f, destination_dir + '/' + f)
        print('Exécutable trouvé et déplacé')