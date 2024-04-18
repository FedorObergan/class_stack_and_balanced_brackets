from stack_class import Stack




stack = Stack()
assert stack.is_empty() == True
stack.push(1)
assert stack.is_empty() == False
stack.push(2)
assert stack.__str__() == '[1, 2]'
assert stack.pop() == 2
assert stack.pop() == 1
assert stack.__str__() == '[]'
stack.push(4)
stack.push(2)
stack.push(8)
assert stack.peek() == 8
assert stack.size() == 3
stack.pop()
stack.pop()
stack.pop()
assert stack.is_empty() == True
