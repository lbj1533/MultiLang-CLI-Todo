from datetime import date, MINYEAR


# define a task
class Task:
   def __init__(self, name, description, due_date):
      self.name = name
      self.description = description
      self.due_date = self.parse_date(due_date)

   def __str__(self):
      if self.due_date:
            due_date_str = f" due {self.due_date}"
      else:
            due_date_str = ""
      if self.description:
            description_str = f"\n\t{self.description}"
      else:
            description_str = ""
      return f"- {self.name}{due_date_str}{description_str}\n"
   
   def __len__(self):
      return len(str(self.name)) + len(str(self.description)) + len(str(self.due_date))

   def parse_date(self, due_date):
      if not(due_date):
         return None
      # format is assumed to be MM/DD
      due_date = due_date.split("/")
      due_date = date(date.today().year, int(due_date[0]), int(due_date[1]))
      return due_date

    # tests for equality, only considers date and name
   def __eq__(self, other_task):
      if other_task == None:
         return False
      return self.name == other_task.name and self.due_date == other_task.due_date

   def __lt__(self, other_task):
      if self.due_date < other_task.due_date:
         return True
      elif self.due_date > other_task.due_date:
         return False
      else:
         if self.name < other_task.name:
               return True
         else:
               return False

class List:
   def __init__(self):
      self.tasks = []

   def __len__(self):
      self.get_info("width")
             
          

   def __str__(self) -> str:
      return_string = ""
      num_cols = List.get_info(self, "width")
      terminal_width_line = "=" * num_cols
      top_bar = "=" * ((num_cols//2) - 3) + "|TODO|" + "=" * ((num_cols//2) - 3)
      if len(self.tasks) == 0:
         return_string = f"{top_bar}\nThere are no items in the list.\n{terminal_width_line}\n"
         return return_string
      # important: the following line only works if "Todo" is the first line added to return_string
      # return_string += "TODO"
      # return_string += "-" * (len(top_bar) - len(return_string))
      for task in self.tasks:
         return_string += str(task)
      return top_bar + "\n" + return_string + terminal_width_line + "\n"

   def add_task(self, task):
      self.tasks.append(task)

   def remove_task_at_index(self, index):
      self.tasks.pop(index)

   def sort(self):
      def by_date(task):
         if task.due_date is None:
            # should always be less than a given date
            return date(MINYEAR, 1, 1)
         return task.due_date

      self.tasks.sort(key=by_date)

   def search(self, task):
      return self.tasks.index(task)
   
   def get_info(self, command) -> str:
      def calculate_width(self) -> int:
         max = 0
         for task in self.tasks:
            if max < len(task):
               max = len(task)
         return max
      
      if command.lower() == "width":
         return calculate_width(self)
      
