# TODO Найдите количество книг, которое можно разместить на дискете

v = 1.44*1024*1024  # Объем в байтах
count = 100         # Кол-во страниц
count_str = 50      # Кол-во строк
count_simv = 25     # Кол-во символов
v_simv = 4          # Объем одного символа

V1 = v_simv * count_simv * count_str #Объем 1 страницы
count_books = int(v // (V1*count))
print("Количество книг, помещающихся на дискету:", count_books)
