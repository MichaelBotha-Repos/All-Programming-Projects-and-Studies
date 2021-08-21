  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###


one = [['#'],
       ['#'],
       ['#'],
       ['#'],
       ['#']]

two = [['###'],
       ['  #'],
       ['###'],
       ['#  '],
       ['###']]

three = [['###'],
         ['  #'],
         ['###'],
         ['  #'],
         ['###']]

four = [['# #'],
        ['# #'],
        ['###'],
        ['  #'],
        ['  #']]

value = list(input('Please insert a value using positive integers:\n'))

Print = []
for elem in value:
    if elem == '1':
        Print.append(one)
    if elem == '2':
        Print.append(two)
    if elem == '3':
        Print.append(three)
    if elem == '4':
        Print.append(four)
    if elem == '5':
        Print.append(one)
    if elem == '6':
        Print.append(two)
    if elem == '7':
        Print.append(three)
    if elem == '8':
        Print.append(four)

def prnt_row(List,row=0):
    length = len(List)
    cnt = length
    while cnt != 0:
        print(List[length- cnt][row][0], end=' ')
        cnt-= 1
    print('\n',end='')

prnt_row(Print)
prnt_row(Print,1)
prnt_row(Print,2)
prnt_row(Print,3)
prnt_row(Print,4)

