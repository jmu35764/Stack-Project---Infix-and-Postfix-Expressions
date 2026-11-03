class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

if __name__ == "__main__":

    import unittest

    s1 = Stack()
    
    #Test if the stack is empty upon creation
    print(s1.is_empty())

    #Test if the stack size increases
    s1.push(1)
    print(s1.size())

    #Test that pushing several items preverves LIFO order
    # and that peek returns but doesn't remove the top item
    s1.push(2)
    print(s1.peek())
    s1.push(3)
    print(s1.peek())
    s1.push(4)
    print(s1.peek())

    #Show items in list to prove data is not lost using peek
    print(s1._data)

    #Show pop returns items in reverse order of insertion
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())

    #Stack returns to empty after all items are removed
    print(s1.is_empty())

    print(s1.peek())
    print(s1.pop())

  







    




