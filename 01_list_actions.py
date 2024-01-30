#list is ordered sequence of different datatypes

userList=["sudha", "paul", "raju", "sham"] 
print(userList)#['sudha', 'paul', 'raju', 'sham']

print(type(userList))#<class 'list'>
print(userList[0])#sudha
print(userList[1])#paul

userList.append("alex")
print(userList)#['sudha', 'paul', 'raju', 'sham', 'alex']
userList.remove("sudha")
print(userList)#['paul', 'raju', 'sham', 'alex']
userList[0]="babu"
print(userList)#['babu', 'sham', 'raju', 'sham', 'alex']
userList.insert(1, "sham")
print(userList)#['sudha', 'sham', 'paul', 'raju', 'sham']
del userList[1]
print(userList)#['sudha', 'paul', 'raju', 'sham']
del userList[-1]
print(userList)#['sudha', 'paul', 'raju']
#number of items in list
print(len(userList)) #4
#sorting list items
userList.sort()
print(userList)#['paul', 'raju', 'sham', 'sudha']
#reverse sorting
userList.sort(reverse=True)
print(userList)#['sudha', 'sham', 'raju', 'paul']
#reversing list
userList.reverse()#reverse() will return None that why we store it in variable and later will print it
print(userList)#['sham', 'raju', 'paul', 'sudha']
#pop() will remove last index value and pop() will return value that's why we directly print it 
print(userList.pop())#sham
print(userList.pop(1))#with index value paul
