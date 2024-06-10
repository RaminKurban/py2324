# сделать приложение, которое спрашивает у пользователя его фамилию,
# если такой пользователь есть в таблице читателей, то вывести его ID,
# сколько книг брал и сколько не вернул
# предусмотреть возможность того, что будут разные пользователи с одинаковой фамилией или не найдена фамилия

import psycopg2

def connect_to_biblio():
    print("начинаем соединение")
    try:
        conn = psycopg2.connect(dbname='biblio', user='postgres', password='123', host='10.10.101.200', port='5550')
        print('есть контакт')
    except:
        print('нет подключения')
    return  conn
def ask_user_fio()->str:
    return input('введите фио').strip()

def check_reader(conn,fio):
    q = f'select nchit from reader where fio = %s '
    with conn.cursor() as cur:  # with - дает авто закрывание
        cur.execute(q,(fio,))
        list_of_nchit= cur.fetchall()
        k = len(list_of_nchit)
        print(f'запрос вернул {k} строк')
        print(list_of_nchit)
        if k==0:
            print('нет такого читателя')
        else:
            if k > 1:
                print('выберите nchit из списка')
                nchit = input()
            else :
                nchit = list_of_nchit[0] [0] # берем единственный столбец из единств. строки рез-та
            print(f'выбран читатель {nchit} по фамилии {fio}')
            q = 'select count(*) as "сколько взял" , count(*)-count(date_in) as "сколько не вернул" ' \
                'from vydacha where nchit = %s '
            cur.execute(q,(nchit,))
            result = cur.fetchone()
            x,y = result
            print(f'читатель {nchit} взял {x} книг не вернул {y} на данный момент')


conn = connect_to_biblio()
reader_fio=ask_user_fio()
check_reader(conn,reader_fio)




