# coding=utf-8
menu = [{''
         'name' : 'Lagman',
         'price' : 160,
         'weight' : 200},
        {'name' : 'Kofe',
         'price' : 40,
         'weight' : 100
        }]

quantity = input('Количество порций: ')
select = raw_input('Блюдо: ')
service = 15
balance = 1000
discount = 20

for m in menu:
    if select == m['name']:
        subtotal = quantity * m['price']
        total = subtotal + subtotal * service/100
        print 'Итого: %s' %(total)
        if discount:
            totalDiscount = total-total*discount/100
            print 'Ваш счет со скидкой : %s' % (totalDiscount)

if balance >= total:
        print 'Приходите еще!'
else:
        print 'Вам стоит пройти с нами!'