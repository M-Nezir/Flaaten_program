""""
İç içe geçmiş veri yapılarını düzleştiren Flatten Programı

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
