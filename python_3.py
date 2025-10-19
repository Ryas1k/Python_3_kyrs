
name_files_1 = {}
name_files_2 = {}
size_exp = {'B': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3}

def calcul(x,r):
  if r in size_exp:
    return int(x) * size_exp[r]
  

def determine(count):
  if count > 1024:
    count = round(count/1024)
    c = 'KB'
    if count > 1024:
      count = round(count/1024)
      c = 'MB'  
      if count > 1024:
        count = round(count/1024)
        c = 'GB'  
  return f'{count} {c}'

with open('files.txt','r',encoding='utf-8') as files:
  for line in files:
    name, size, ragmer = line.split()
    name_first, name_second = name.split('.')
    name_files_1.setdefault(name_second,[]).append(name)
    name_files_2.setdefault(name_second,[]).append(calcul(size,ragmer))
s =  {k: sum(v) for k, v in name_files_2.items()} #нашли сумму 

sort_name_files_1 = {k : sorted(v)  for k, v in sorted(name_files_1.items())}

last_index = len(sort_name_files_1)
for i, (k,v) in enumerate(sort_name_files_1.items()):
  print(*v,sep='\n')
  print('----------')
  print(f'Summary: {determine(s[k])}') 
  if i < last_index-1:
    print() 

    
         