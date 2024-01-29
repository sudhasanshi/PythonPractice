import os, sys
print(os.getcwd())
print(os.listdir("C:\\Users\\sudha\\python-files"))
print(os.chdir("C:\\Users\\sudha"))
print(os.makedirs("sudha", exist_ok=True))
print(os.chdir("C:\\Users\\sudha\\python-files"))
print(os.makedirs("manju", exist_ok=True))
print(os.removedirs("manju"))
print(os.path.join("C:\\Users\\sudha\\python-files", "sudha"))
print(os.path.isfile("sudha"))
print(os.path.basename("osmodule.py"))
print(os.path.exists("sudha"))
print(os.walk("C:\\Users\\sudha\\python-files"))

for path, dir, files in os.walk("C:\\Users\\sudha\\python-files\\PythonPractice"):
    print(path, dir, files)
    for file in files:
        if file.lower().endswith(".py"):
            print(file)
    sys.exit(0)
