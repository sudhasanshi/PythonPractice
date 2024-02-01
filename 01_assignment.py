Assignment : Write a script to read the notice, license file and add the content of each file to the file notice_license.txt. The notice or license file may be started with notice or license
before appending the content to notice_license.txt file add the relative path --> This can also be said as the automation script. Add this to the automation scripts question

To fetch notice and license file from project directory (notice.txt, license.txt, notice.md etc) and the add the contents of this file along with relative path to the single file.
Purpose of writing this script ->  For internal usage

Required output as below
Notice 
Noticefile1path
Noticefile1content
Noticefile2path
Noticefile2content

License
Licensefile1path
Licensefile1content
Licensefile2path
Licensefile2content
1) method
import os, sys
filename="notice_licence.txt"
pwd_path=os.getcwd()
with open(filename, "a") as f:
  f.write("NOTICE\n")
  for paths, dirs, files in os.walk(pwd_path):
    for file in files:
        if file.lower().startswith("notice") or file.lower().startswith("licence"):
           filepath=os.path.basename(file)
           content=open(filepath, "r")
           value=content.read()
           f.write(f"{filepath}\n")
           f.write(f"{value}\n")

with open(filename, "a") as f:
  f.write("LICENCE\n")
  for paths, dirs, files in os.walk(pwd_path):
    for file in files:
        if file.lower().startswith("licence"):
           filepath=os.path.basename(file)
           content=open(filepath, "r")
           value=content.read()
           f.write(f"{filepath}\n")
           f.write(f"{value}\n")
    sys.exit(0)

2)method
import os
pattren=["notice", "license"]
filename="notice_license.txt"
cur_dir=os.getcwd()
for pat in pattren:
    with open(filename, "a") as fh:
        fh.write(f"\n{pat}\n")
    for root, dir, files in os.walk(cur_dir):
        for file in files:
            if file.lower().startswith(pat):
                file_path=os.path.join(root, file)
                with open(file_path, 'r') as ti:
                    content = ti.read()
                with open(filename, 'a') as f:
                    f.write(f"{root}\n{content}")
    with open(filename, 'a') as fh:
        fh.write('*' * 30)
        fh.write("\n")
