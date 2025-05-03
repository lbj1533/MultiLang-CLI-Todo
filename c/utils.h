#define MAX_USER_ACTION_LEN 21
#define MAX_USER_ACTIONS 3

struct List
{
   struct Task *firstTask;
   struct Task *lastTask;
};

struct Task
{
   char *name;
   char *dueDate;
   char *description;
   struct Task *nextTask;
};

char *generateListWidthLine(void);

void printList(const struct List *list);
void addTask(struct List *list, struct Task *task);

void todoMessage(char *message);
void todo(void);
