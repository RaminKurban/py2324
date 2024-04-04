import psycopg2

def how_many_books(active_connection):
    #нужно составить запрос
    q = 'select count(*) from book'
    #выполнить запрос при помощи Курсора
    cur = active_connection.cursor()
    cur.execute(q)
    result = cur.fetchone() # извлекаем 1 строку из результатов  последнего запроса
    #обработать результаты
    print(f' в библиотеке информация о {result[0]} книгах')

def how_many_exemplar(active_connection):
    e = 'select count(*) from exemplar '
    cur = active_connection.cursor()
    cur.execute(e)
    result = cur.fetchone()
    print(f' в библиотеке информация о {result[0]} экземплярах')

def get_genre_amount(active_connection)->int:
    g = 'select count(*) from genre '
    with active_connection.cursor() as cur:  # with - дает авто закрывание
        cur.execute(g)
        result = cur.fetchone()
        return  result[0]
def print_books(active_connection):
    g = 'select * from book '
    with active_connection.cursor() as cur:  # with - дает авто закрывание
        cur.execute(g)
        print('_____список книг_____')
        for line in cur:
            i , t, y  = line
            print(f'{i}  {t}  {y}')
        print('----------------')







# точка входа
try:
    conn = psycopg2.connect(dbname='biblio', user='postgres', password='123', host='10.10.101.200', port='5550')
    print ('есть контакт')
    how_many_books(conn)
    how_many_exemplar(conn)
    g_amount = get_genre_amount(conn)
    print(f' в библиотеке насчитывается {g_amount} жанров')
    print_books(conn)
    conn.close()
except:
    print('нет подключения')



