# Python Stack Class

This is a simple implementation of a stack data structure in Python. 

## Features

- The `Stack` class supports basic stack operations: push, pop, and peek.
- The size of the stack must be defined upon initialization and cannot be changed afterward.
- If an attempt is made to push an item onto a full stack, an exception will be raised.
- If an attempt is made to pop an item from or peek at an empty stack, an exception will be raised.

## Example

Here's how you can use the `Stack` class:

```python
s = Stack(3)  # Creates a new stack that can hold up to 3 items

s.push('apple')  # Pushes 'apple' onto the stack
s.push('banana')  # Pushes 'banana' onto the stack
print(s.peek())  # Prints 'banana'

print(s.pop())  # Pops and prints 'banana'
print(s.pop())  # Pops and prints 'apple'