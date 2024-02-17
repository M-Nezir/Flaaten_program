""""
Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi)
oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""

def böl(l):
  li = []
  for i in l:
    if type(i)== list:
       li.extend(böl(i))
    else:
        li.append(i)
  return li

a = böl(list(eval(input())))
print(a)
