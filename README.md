print formatting
it is the process of combining variables and strings toger to display the formatted output

1).format method:
example:
i need to dispaly statement as : my emplyoee name is aa and employeid is 111
name="aa"
id=111
print("my employee name is {} and employeid is {}".format(name,id))


2)f-method
print(f"my employee name is {name} employeid is {id}")

input method

f-method and format method in input
string-group of characters in python indexing allows the user to grab paratial values from any data
indexing starts from 0 to n-1 

-Why python is required for DevOps even though we have shell scripting 
1.python supports reverse indexing . it will start display from last character. for last character index is -1
  python has advance/adavantage features compare to shell scripting
2.It is independent of OS. where as bash scripting works only on Linux OS
3.For writing more complex logic which we can't do it in shell scripting
4.Python provides better error handling compared with shell scripting
5.number of lines of code will be reduced compared with shell scripting
6.Easy to learn and understand

python modules
Modules:
1) SYS module : This is a module which is used to print the system related 
values. Using this module we can access variables maintained by the 
python interpreter and functions that interact with the interpreter.To 
use this module need to import sys module.
syntax: import sys

 a) sys.argv :(argv-argument vector) It is a list in python which contains the command line 
   arguments passed to the script. The first element is the script name. 
   example: import sys
   print(sys.argv) - It will print the name and argument passed
   print(sys.argv[1]) - It will print the first command line argument passed
   
 b) sys.path : It will print the current system path
   import sys
   print(sys.path) 
 c) sys.exit : It is used to exit from the python interpreter by raising the exception.
    import sys
    sys.exit(0)
    sys.exit(f"Execution stopped")

    
2) OS module : This module provides the way for interacting with the OS.
 
 - os.getcwd() - Display the current working directory
 - os.makedirs() - It is used to create the directory
    os.makedirs("pythondir", exist_ok=True) -
 - os.listdir() - It will list all the files and directories
    print(os.listdir("D:\\Drives\\DRC\\python\\pythonProject"))
 - os.chdir() - It is used to change the directory
    os.chdir("pythondir")
    print(os.getcwd())
 - os.path.isfile() - It will check whether it is a file or not and return true if it exists.
    print(os.path.isfile("1.txt")) - checks file exist
    print(os.path.exists("pythondir")) - checks directory exist
 - os.path.join() - It is used to join the path
 - os.path.basename() - It will return the base name of the file.
 - os.walk() - It is used to walk through all the directory and sub directoy and in each iteration it returns the current path, all the files and 
               directories.
