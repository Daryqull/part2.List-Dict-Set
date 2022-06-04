#список
#Преимущества: упорядоченная последовательнось элементов с различными типами данных.
cars = ['Lada', 'Audi', 'Chery', 'Infiniti', 'Ferrari']
for x in cars:
   if x == 'Lada':
    print('I buy')
    
    
#словарь
#Преимущества: удобное хранени информации: ключ-значение, значение ключа уникально.

cars = {'Lada':'Russia', 'Audi':'Германия', 'Chery':'Китай', 'Infiniti':'Япония', 'Ferrari':'Италия'}
for x in cars:
   if x == 'Audi':
    print('Германия')
    
    
#множество
#Преимущества:уникальность элементов, поддержка хеширования

cars = {'Lada', 'Audi', 'Chery', 'Infiniti', 'Ferrari'}
for x in cars:
   if x == 'Infiniti':
    print('How much?')
    
    

