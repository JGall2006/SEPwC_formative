import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Function: add_task
    
    Input - a task to add to the list
    Return - nothing
    """ 
    with open(TASK_FILE, "a") as file:
        file.write(task + "\n")
        
        
        
        #if i am on my branch this should be here 

    return    
    
      
    
def list_tasks():
    
    with open (TASK_FILE, "r") as file:
        tasks = file.readlines()
        counter = 1
        output_string = ""
        for task in tasks:
            output_string = output_string + str(counter)+". "+task
            counter = counter + 1
            
    return output_string.rstrip('\n')


def remove_task(index):
    
    with open (TASK_FILE, "r") as file:
        lines = file.readlines()
        file = f
    if 0 < index <= len(lines):
        removed = lines.pop(index - 1)
        
        with open(TASK_FILE, "w") as file:
            file.writelines(lines)
        print(f"Removed: {removed.strip()}")
    
    else:
        print("sorry, there is no task to remove")
    
    except FileNotFoundError:
        print("Error, no tasks found. Create one!!")
        
#should delete a task and replaice it with text saying nothing
        
    
    return

def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
