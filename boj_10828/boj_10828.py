from collections import deque
import sys

N = int(input())
# print('N :', N)
# stack = []
stack = deque()

input = lambda: sys.stdin.readline().strip()
print = lambda x: sys.stdout.write(str(x) + '\n')

for _ in range(N):
    command = input()
    # print('command :', command)
    commands = command.split()
    if commands[0] == 'push':
        stack.append(commands[1])
    elif commands[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif commands[0] == 'size':
        print(len(stack))
    elif commands[0] == 'empty':
        print(0 if stack else 1)
    elif commands[0] == 'top':
        print(stack[-1] if stack else -1)
    # print(stack)
