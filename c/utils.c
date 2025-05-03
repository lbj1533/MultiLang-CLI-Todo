#include "utils.h"
#include <stdio.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

char *generateListWidthLine(void)
{
   todoMessage("make this line list width");
   // get terminal width
   struct winsize w;
   ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);
   int terminalWidth = w.ws_col;

   if (terminalWidth <= 0)
   {
      return "";
   }

   char *terminalWidthLine;
   terminalWidthLine = (char *)malloc(terminalWidth + 1);
   if (!terminalWidthLine)
   {
      return "="; /* default has length 10 */
   }

   memset(terminalWidthLine, '=', terminalWidth);
   terminalWidthLine[terminalWidth] = '\0';

   return terminalWidthLine;
}

void printList(const struct List *list)
{
   char *terminalWidthLine = generateListWidthLine();
   printf("%s\n", terminalWidthLine);
   struct Task *curr;
   curr = list->firstTask;
   while (curr)
   {
      printf("%s due %s\n    - %s\n", curr->name, curr->dueDate, curr->description);
      curr = curr->nextTask;
   }
   printf("%s\n", terminalWidthLine);
   free(terminalWidthLine);
   const char userActions[MAX_USER_ACTIONS][MAX_USER_ACTION_LEN] = {"[A] to Add Task", "[D] to Delete Task", "[E] to Exit"};
   for (int i = 0; i < MAX_USER_ACTIONS; i++)
   {
      printf("%s\n", userActions[i]);
   }
   return;
}

void addTask(struct List *list, struct Task *task)
{
   /* assume adding to the end, will sort later */
   if (!list->firstTask)
   {
      /* length is 0, will be 1 */
      list->firstTask = task;
      list->lastTask = task;
   }
   else if (list->firstTask == list->lastTask)
   {
      /* length is 1, will be >1 */
      list->lastTask->nextTask = task;
      list->lastTask = task;
   }
   todoMessage("implement sorting list on add");
   return;
}

void todoMessage(char *message)
{
   printf("\033[1;31mTodo: %s\033[1;0m\n", message);
   return;
}

void todo(void)
{
   printf("\033[1;31mTodo\033[1;0m\n");
   return;
}
