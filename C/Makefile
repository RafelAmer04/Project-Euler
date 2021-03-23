CFLAGS = -O3 -I.
CC = gcc
TARGET = P011
OBJECTS = readnumbers.o P011.o

$TARGET): $(OBJECTS)
	$(CC) -o $(TARGET) $(OBJECTS)

clean:
	rm -f $(OBJECTS) $(TARGET)
