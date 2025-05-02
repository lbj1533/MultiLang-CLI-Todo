#include "utils.h"
#include <stdio.h>

const char userActions[MAX_USER_ACTIONS][MAX_USER_ACTION_LEN] = {"[A] to Add Task","[D] to Delete Task","[E] to Exit"};

char* generateTerminalWidthLine(void){
   todo_message("terminal width line not implemented yet");
   char *terminalWidthLine = "=======";
   return terminalWidthLine;
}

void printList(const struct List *list){
   printf("%s\n",generateTerminalWidthLine());
   todo_message("traversing the list not implemented yet");
   printf("%s\n",generateTerminalWidthLine());
}

void todo_message(char* message){
   printf("\033[1;31mTodo: %s\033[1;0m\n", message);
   return;
}

void todo(void){
   printf("\033[1;31mTodo\033[1;0m\n");
   return;
}
