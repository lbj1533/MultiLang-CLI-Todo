COMPILER = gcc
CFLAGS = -ansi -pedantic -Wall -g -std=c99
TARGET = CTODO
OBJS = main.o utils.o

# default target
all: $(TARGET)

# linking stage
$(TARGET): $(OBJS)
	$(COMPILER) $(CFLAGS) -o $(TARGET) $(OBJS)

# compilation rules
main.o: main.c utils.h
	$(COMPILER) $(CFLAGS) -c main.c -o main.o

utils.o: utils.c utils.h
	$(COMPILER) $(CFLAGS) -c utils.c -o utils.o

clean:
	rm -f $(OBJS) $(TARGET)