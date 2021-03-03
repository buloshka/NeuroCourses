def Matrix(l1,l2):
  if len(l1[0]) == len(l2):
    ans = [[0 for i in range(len(l2[0]))] for i in range(len(l1))]
    for a in range(len(l1)):
      for b in range(len(l2[0])):
        for c in range(len(l2)):
          ans[a][b] += l1[a][c]*l2[c][b]
  else:
    print("\nКоличество строк второй матрицы не равно количеству столбцов первой.\n")
    return None
  return ans
def X():
  print("\n\nВвод чисел через пробел, следующая строка - enter.\nКогда матрица заполнена, enter и 'end'.\n\nПример:\n    Пример матрицы:\n    0 0 0\n    0 0 0\n    0 0 0\n    end\n\nВведите матрицу:")
  a = []
  while(True):
    p = input()
    if p == "end":
      break
    elif len(p.split(" ")) == 1 and '' in p.split(" "):
      print("Должна быть хотя бы одна цифра. \nДля завершения напишите end.")
    elif '' in p.split(" "):
      print("В строке есть пропуски, введите заново.\nДля завершения напишите end.")
    else:
      a.append(p.split(" "))
  for z in range(len(a)):
    for x in range(len(a[z])):
      a[z][x] = int(a[z][x])
  return a
answer = Matrix(X(),X())
print("\nПроизведение матриц:\n")
if answer != None:
  for a in range(len(answer)):
    for b in range(len(answer[a])):
      print(answer[a][b],end = ' ')
    print()
