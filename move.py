import os
import shutil
directory = './Music'
destDir = './Sorted'

for filename in os.listdir(directory):
    newDir = filename.split('-')[0].strip()
    print(filename)
    print('To: %s' % newDir)
    src = os.path.join(directory, filename)
    dest = os.path.join(destDir, newDir, filename)
    if not os.path.exists(os.path.join(destDir, newDir)):
        os.makedirs(os.path.join(destDir, newDir))
    shutil.copy2(src, dest)
