n = int(input())
mail_get = [input().split('@')[0] for i in range(n)]
print(mail_get)
list2 = []
new_mail_get = list()
m = int(input())
for i in range(m):
    new_name = input()
    count = 0
    #print(new_name)
    while new_name in mail_get:
        count += 1
        new_name = new_name+str(count)
        
    else:
        print(new_name+'@beegeek.bzz')