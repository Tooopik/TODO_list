from datetime import datetime
import pickle


class Task:
    taskList = []
    taskStatus = ('todo', 'during', 'done')

    def __init__(self, taskName, addDate, deadLine, taskStatus=taskStatus[0]):
        self.task = taskName
        self.deadLine = deadLine
        self.addDate = addDate
        self.status = taskStatus
        self.taskList.append(self)

    # def addTask(self):
     #   self.task = 'test'
     #   self.deadLine = datetime(input('Deadline (y,m,d) >>> '))
     #   self.addDate = datetime.now()
     #   self.status = self.taskStatus[0]
     #   self.taskList.append({self.task: [self.status, self.addDate, self.deadLine]})

    @ staticmethod
    def numberOfTask():
        return len(Task.taskList)

    @ staticmethod
    def showAllTask():
        for id, task in enumerate(Task.taskList):
            print(
                f'Task ID: {id + 1} | Task: {task.task} | Status: {task.status}')
        print('\n')

    @staticmethod
    def saveTasklist():
        with open("test.pkl", "wb") as out:
            pickle.dump(Task.taskList, out)

    @staticmethod
    def loadTasklist():
        try:
            with open("test.pkl", "rb") as inp:
                Task.taskList = pickle.load(inp)

        except:
            print("ERROR")


def menu():
    while True:
        print('what do you want to do?')
        print('1 - show all TODO postions\n2 - Add new TODO position\n3 - delete position\n4 - Exit')
        try:
            userChoice = int(input('>>> '))
        except ValueError:
            userChoice = 0
            print('Error - select from numbers!')

        if userChoice in [1, 2, 3, 4]:
            break
    return userChoice


print('Welcome to your TODO list')
Task.loadTasklist()
while True:
    userChoice = menu()
    if userChoice == 1:
        tasksAmounth = Task.numberOfTask()
        print(f'You have {tasksAmounth} tasks'+'\n')
        if tasksAmounth > 0:
            Task.showAllTask()

    elif userChoice == 2:
        print('Enter task name:')
        task = input('>>> ')
        deadLine = datetime(2020, 7, 1)
        date = datetime.now()
        Task(task, date, deadLine)
        print('New task added')

    elif userChoice == 3:
        print('Possition deleted')

    elif userChoice == 4:
        break

Task.saveTasklist()
print('\n'+'Bye bye')
