import psycopg2



def connect_to_biblio():
    print("начинаем соединение")
    try:
        conn = psycopg2.connect(dbname='biblio', user='postgres', password='123', host='10.10.101.200', port='5550')
        print('есть контакт')
    except:
        print('нет подключения')
    return  conn

def ask_user_fio():
    print("новая книга:")
    isbn = int(input('isbn:').strip())
    title = input('название:').strip()
    year = int(input('год:').strip())
    author = input('автор:').strip()
    return isbn,title,year,author
def chekc_reader(conn,fio):

conn = connect_to_biblio()
isbn,title,year,author = ask_book_info()
def
