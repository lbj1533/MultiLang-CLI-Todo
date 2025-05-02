#define MAX_USER_ACTION_LEN 21
#define MAX_USER_ACTIONS 3


struct List{
   struct Task *firstTask;
   struct Task *lastTask;
};

struct Task{
   char *name;
   char *dueDate;
   char *description;
   struct Task *nextItem;
};

char* generateTerminalWidthLine(void);

void printList(const struct List *list);

void todo_message(char* message);
void todo(void);
