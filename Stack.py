stack = []

#push
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

#pop
element = stack.pop()
print("Pop:", element)

#peek
topElement = stack[-2]
print("Peek: ", topElement)

#isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

#size
print("Size: ", len(stack))
