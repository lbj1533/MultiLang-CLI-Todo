from tasks import Task, List
from input_handling import *


def main():
   list = List()
   save_file = "saved_list_py.txt"
   open_save(save_file, list)
   #apply_debug_list_init(list)
   while True:
      save_to_file(save_file, list)
      input_handling(list)
      
        


def apply_debug_list_init(list):
   task1 = Task("task1", "desc for task1", "4/26")
   task2 = Task("proj1", "do the rel proj instead of studying lol", "4/28")
   task3 = Task("proj1", "", "2/20")
   task4 = Task("proj2", "bruh burh bruhu", "4/26")
   list.add_task(task1)
   list.add_task(task2)
   list.add_task(task3)
   list.add_task(task4)
   list.get_info("width")
   return list


def input_handling(list):
   print(list)
   key_pressed = get_input()
   parse_input(key_pressed, list)


if __name__ == "__main__":
   main()
