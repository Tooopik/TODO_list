from asyncio.windows_events import NULL
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

    @staticmethod
    def editTask():
        print('Enter task ID to edit:')
        taskId = int(input('>>> '))
        print(
            f'\nTask: {Task.taskList[taskId-1].task} | Status: {Task.taskList[taskId-1].status} | Deadline: {Task.taskList[taskId-1].deadLine}\n')

        if taskId <= len(Task.taskList):
            print('What do you want to edit?')
            print('1 - name\n2 - status\n3 - deadline')
            userChoice = int(input('>>> '))
            if userChoice in [1, 2, 3]:
                if userChoice == 1:
                    print(f'Current name: {Task.taskList[taskId-1].task}')
                    print('Enter new name:')
                    newName = input('>>> ')
                    if len(newName) >= 1:
                        Task.taskList[taskId-1].task = newName
                        print(
                            f'Task name changed to: {Task.taskList[taskId-1].task}\n')
                    else:
                        print(f'New name "{newName}" is not correct')

                elif userChoice == 2:
                    print(f'Current status: {Task.taskList[taskId-1].status}')
                    print('Select status:')
                    for idx, status in enumerate(Task.taskStatus, start=1):
                        print(f'{idx} - {status}')
                    userChoice = int(input('>>> '))
                    if userChoice in range(0, len(Task.taskStatus)+1):
                        Task.taskList[taskId -
                                      1].status = Task.taskStatus[userChoice-1]
                        print(
                            f'Status changed to: {Task.taskList[taskId -1].status}\n')
                    else:
                        print(f'Number {userChoice} is wrong')

                elif userChoice == 3:
                    pass
            else:
                print('Use number from range')
        else:
            print(f'Task with ID {taskid} not exist')

    @staticmethod
    def deleteTask():
        print('Enter task ID to delete:')
        taskId = int(input('>>> '))
        try:
            del Task.taskList[taskId - 1]
            print('Task deleted\n')
        except:
            print('error')

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
        print('1 - show all TODO postions\n2 - Add new TODO position\n3 - edit position\n4 - delete position\n5 - Exit')
        try:
            userChoice = int(input('>>> '))
        except ValueError:
            userChoice = 0
            print('Error - select from numbers!')

        if userChoice in [1, 2, 3, 4, 5]:
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
        Task.editTask()

    elif userChoice == 4:
        Task.deleteTask()

    elif userChoice == 5:
        break

Task.saveTasklist()
print('\n'+'Bye bye')
