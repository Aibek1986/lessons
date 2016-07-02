# coding=utf-8
# Есть здание из 2 комнат
# Нужно угадать номер комнаты, в которую нужно войти, чтобы выйти из здания
# В первой комнате, есть на выбор еще 2 комнаты и одна из этих комнат
# является выходом из игры а другая перекидывает нас на уровень  выше



# import random
# rooms = [1, 2]
# room_number = input('Vyberite cislo(1 i 2): ')
#
# if room_number in rooms:
#     play = True
#     if room_number == 1:
#         print 'Vy vidite 2 komnaty'
#         exit = random.randint(1, 2)
#         while play:
#             select_room = input('Vyberite komnatu(1 i 2): ')
#             if select_room == exit:
#                 print 'Vy vywli iz igry'
#                 play = False
#             else:
#                 print 'Vy snova v komnate'
#
#     else:
#         print 'Vy vidite 5 komnat'
#         exit = random.randint(1, 5)
#         while play:
#             select_room = input('Vyberite komnatu(ot 1 do 5): ')
#             if select_room == exit:
#                 print 'Vy vywli iz igry'
#                 play = False
#             else:
#              print 'Vy snova v ko'

odd = []
even = []
i = 0
while i < 100:
    if i % 2 == 0:
        even.append(i)

    else:

        odd.append(i)
    i += 1
print odd
print even

#print sum(odd[1::2])

odd_sum = 0
even_sum = 0

for sum in odd:
        if odd.index(sum) % 2 != 0:
            odd_sum += sum
            print sum
#
# for sum in even:
#         if even.index(sum) % 2 == 0:
#             even_sum += sum
#             # print sum

print odd_sum
print even_sum
