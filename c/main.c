#include <stdio.h>
#include "utils.h"

int main(void){
   struct List list = {NULL, NULL};
   struct Task task1 = {
      .name = "task1",
      .dueDate = "4/20",
      .description = "bruh uhhhh",
      .nextTask = NULL
   };
   addTask(&list, &task1);
   printList(&list);
   todoMessage("implement input");
   return 0;
}

