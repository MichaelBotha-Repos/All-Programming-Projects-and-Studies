"""This progam will implement the Expert Judgment methodology of project estimation"""

class Task:
    """Represents a task"""
    def __init__(self, description, estimations):
        self.task_description = description
        self.task_estimations = estimations

    


class Project:
    """Represents a project with all allocated tasks and assigned efforts"""
    def __init__(self):
        self.project_id = ""
        self.tasks = []


    def add_task(self):
        '''Method for adding a task '''
        print('Please enter a task description:\n')
        description = input()
        task = [description]
        for i in range(5):
            estimate = input(f"Please enter the {i + 1} effort estimation for task in man.hours:\n")
            task.append(estimate)
        self.tasks.append(task)


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
                print("3 - Exit")
                choice2 = input()
                if choice2 == '1':
                    pass
                elif choice2 == '2':
                    pass
                elif choice2 == '3':
                    break

        elif choice == '3':
            exit()

