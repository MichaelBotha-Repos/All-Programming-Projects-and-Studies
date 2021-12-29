'''
Code from https://scipython.com/book/chapter-2-the-core-python-language-i/examples/the-tower-of-hanoi/

def hanoi(n, P1, P2, P3):
    """ Move n discs from pole P1 to pole P3. """
    if n == 0:
        # No more discs to move in this step
        return

    global count
    count += 1

    # move n-1 discs from P1 to P2
    hanoi(n-1, P1, P3, P2)

    if P1:
        # move disc from P1 to P3
        P3.append(P1.pop())
        print(A, B, C)

    # move n-1 discs from P2 to P3
    hanoi(n-1, P2, P1, P3)

# Initialize the poles: all n discs are on pole A.
n = 3
A = list(range(n,0,-1))
B, C = [], []

print(A, B, C)
count = 0
hanoi(n, A, B, C)
print(count)
'''


''' My code, modifying the above, but keeping the same logic '''

def tower(num_disks, stack_a, stack_b, stack_c):
    """ Using double nested recursion to fulfill the algorithm  """

    # Condition to end recursion
    if num_disks == 0:
        return

    global moves
    moves += 1

    # move n-1 discs from stack_a to stack_b
    tower(num_disks -1, stack_a, stack_c, stack_b)

    if stack_a:
        stack_c.append(stack_a.pop())
        print(stack_a, stack_b, stack_c)

    # move n-1 discs from stack_b to stack_c
    tower(num_disks -1, stack_b, stack_a, stack_c)


while True:
    try:
        num_disks = int(input('please enter the number of disks:\n'))
        break

    except:
        continue

stack_a = [i + 1 for i in reversed(range(num_disks))]
stack_b = []
stack_c = []

print(stack_a, stack_b, stack_c)
moves = 0
tower(num_disks, stack_a, stack_b, stack_c)
print(moves)












