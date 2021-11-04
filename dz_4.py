greeting = "Привет, {}!"
posts = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for post in posts:
    print(greeting.format(post.split()[-1].title()))
