queue = []

#Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

#Dequeue
element = queue.pop(0)
print("Dequeue: ", element)

#Peek
frontElement = queue[0]
print("Peek: ", frontElement)

#isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

#Size
print("Size: ", len(queue))