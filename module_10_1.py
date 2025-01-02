import threading
import time

#создаем обертку для функций с целью подсчета времени работы функции
def run_time_func(func):
    def wrapper(word_count, file_name):
        start_time = time.time()
        func(word_count, file_name)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Завершилась запись в файл {file_name} за {run_time:.4f} секунд")
    return wrapper
#применим декоратор
@run_time_func
def wite_words(word_count, file_name):
    with open(file_name,'w',encoding='utf-8') as file:
        for i in range(1,word_count+1):
            time.sleep(0.1 )
            file.write(f'Какое-то слово № {i}' + '\n')

list_potokov = [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example9.txt')]
def run_potok(spisok:list):
    ''' Функция для подсчета времени работы потока'''
    start_time = time.time()
    for i in range(len(spisok)):
          word_count, file_name=list_potokov[i]
          potok = threading.Thread(target=wite_words(word_count, file_name))
          potok.start()
          potok.join()
    end_time = time.time()
    run_time = end_time - start_time
    return print(f'Работа потока {run_time}')

# wite_words(10, 'example1.txt')
# wite_words(30, 'example2.txt')
# wite_words(200, 'example3.txt')
# wite_words(100, 'example4.txt')
run_potok(list_potokov)
