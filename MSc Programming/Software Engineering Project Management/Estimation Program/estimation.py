"""This progam will implement the Expert Judgment methodology of project estimation"""

class Task:
    """Represents a task"""
    def __init__(self):
        self.task_description = ''
        self.task_estimations = []
        self.task_dependencies = []
        self.chosen_estimation = 0
        self.add_description()
        self.add_estimations()

    def add_description(self):
        print('Please enter a task description:\n')
        self.task_description = input()

    def add_estimations(self):
        for i in range(5):
            estimate = input(f"Please enter the {i + 1} effort estimation for task in man.hours:\n")
            self.task_estimations.append(estimate)

    def add_dependency(self):
        print('Please enter the ID of the task dependency')
        dependency = input()
        self.task_dependencies.append(dependency)
        

class Project:
    """Represents a project with all allocated tasks and assigned efforts"""
    def __init__(self):
        self.project_id = ""
        self.tasks = []

    def add_task(self):
        '''Method for adding a task '''
        self.tasks.append(Task())

    def display_tasks(self):
        print("\nTask Description\tTask Estimation 1\tTask Estimation 2\tTask Estimation 3\tTask Estimation 4\tTask Estimation 5")
        for task in self.tasks:
            print(f"{task.task_description}\t\t\t{task.task_estimations[0]}\t\t\t{task.task_estimations[1]}\t\t\t{task.task_estimations[2]}\t\t\t{task.task_estimations[3]}\t\t\t{task.task_estimations[4]}")
            
        print('\n\n')
       
        


if __name__ == '__main__':
    # Main control flow of code
    while True:
        print("Welcome")
        print("Please select and option:")
        print("1 - Create a new project")
        print("2 - Edit an existing project")
        print("3 - Exit")
        choice = input()

        if choice == '1':
            new_project = Project()
            while True:
                print("Please select and option:")
                print("1 - Create a new task")
                print("2 - Edit an existing task")
                print("3 - Display all tasks")
                print("4 - Exit")
                choice2 = input()
                if choice2 == '1':
                    new_project.add_task()
                elif choice2 == '2':
                    pass
                elif choice2 == '3':
                    new_project.display_tasks()
                elif choice2 == '4':
                    break

        elif choice == '3':
            exit()

