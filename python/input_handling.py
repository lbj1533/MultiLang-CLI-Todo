from tasks import Task
from datetime import date
import logging

def log(log, level, message):
   logging.basicConfig(filename="py.log", filemode='w')
   logger = logging.getLogger(log)
   level = level.lower()
   if level == "debug":
      logger.debug(f"{level.upper} - {log} - {message}")
   elif level == "info":
      logger.info(message)
   elif level == "warning":
      logger.warning(message)
   elif level == "error":
      logger.error(message)
   elif level == "critical":
      logger.error(message)
   else:
      logger.info(f"Level is wrong for this debug. Message: {message}")
   

def get_input():
   prompt = "[A] to Add Task\n[D] to Delete Task\n[E] to Exit\n"
   return input(prompt)

def input_new_task() -> None|Task:
   prompt = "Enter a name for the task:\n"
   name = input(prompt)
   prompt = "Enter a due date for the task as MM/DD:\n"
   due_date = input(prompt)
   prompt = "Enter a description for the task (Hit Enter to skip):\n"
   description = input(prompt)
   if not(name) or not(due_date):
      return None
   return Task(name, description, due_date)

def input_task_to_remove(list):
   
   def index_by_name(list, name):
      for i, obj in enumerate(list.tasks):
         if obj.name == name:
            return i
      print(f"{name} not found")
   
   def index_by_date(list, date):
      for i, obj in enumerate(list.tasks):
         if obj.due_date == date:
            return i
      print(f"{date} not found")

   prompt = "Enter the name of the task:\n"
   name = input(prompt)
   name_count = sum(1 for task in list.tasks if task.name == name)

   if name_count == 1:
      index = index_by_name(list, name)
      return index
   
   #if multiple items with same name:
   prompt = "Enter the date of the task(MM/DD):\n"
   due_date = input(prompt)
   if "/" not in due_date:
      print("Tasks need a name and a date.")
      return None
   due_date = due_date.split("/")
   try:
      due_date = date(date.today().year, int(due_date[0]), int(due_date[1]))
   except ValueError:
      print("Malformatted Date.")
      return None
   index = index_by_date(list, due_date)
   if index:
      return index
   else:
      print("No such task exists.")
      return None

def parse_input(key_pressed, list):
   key_pressed = key_pressed.lower()
   if key_pressed == "a":
      task = None
      while not(task):
         task = input_new_task()
         if task == None or type(task.due_date) != date:
            print("A task must include a name and a date.")
            return
      list.add_task(task)
      list.sort()
   elif key_pressed == "d":
      task = input_task_to_remove(list)
      list.remove_task_at_index(task)
      list.sort()
   elif key_pressed == "e":
      quit(0)

def save_to_file(filename, list):
   with open(f"./python/{filename}", 'w') as file:
      for task in list.tasks:
         file.write(f"{task.name}|{task.due_date}|{task.description}\n")

def open_save(filename, list):
   try:
      with open(f"./python/{filename}", 'r') as file:
         for line in file:
            arg_list = line.strip().split("|")
            list.add_task(Task(arg_list[0],arg_list[2], arg_list[1]))
   except FileNotFoundError:
      print("No save found. Creating new list.\n")