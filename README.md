# Этот репозиторий содержит набор различных Python-скриптов для обработки и анализа данных. Ниже приведено краткое описание каждого файла:

## python_1.py

Скрипт выполняет базовую обработку строк, делит строки по разделителю и выводит отдельные элементы. Предназначен для демонстрации работы с функциями split и rsplit на примере строковых переменных.

<img width="1221" height="602" alt="image" src="https://github.com/user-attachments/assets/8d2603f2-1836-4762-9bec-609f7c2304e8" />

Sample Input 1:  
  
13  
Sample Output 1:  
  
2  
Sample Input 2:  

2  
Sample Output 2:  

1  
Sample Input 3:  

20  
Sample Output 3:  
3  

## python_2.py

Программа реализует подсчет количества различных элементов во входных данных с помощью словаря. Используются методы setdefault и get для агрегации информации о частоте встречаемости элементов.

<img width="979" height="904" alt="image" src="https://github.com/user-attachments/assets/18187782-89a0-4956-89f7-44bc88d59f58" />

https://stepik.org/lesson/569749/step/8?unit=564263 cсылка на задачу.
 
Sample Input 1:

6  
ivan-petrov@beegeek.bzz  
petr-ivanov@beegeek.bzz  
ivan-petrov1@beegeek.bzz  
ivan-ivanov@beegeek.bzz  
ivan-ivanov1@beegeek.bzz  
ivan-ivanov2@beegeek.bzz  
3  
ivan-ivanov  
petr-petrov  
petr-ivanov  
Sample Output 1:  

ivan-ivanov3@beegeek.bzz  
petr-petrov@beegeek.bzz  
petr-ivanov1@beegeek.bzz  
Sample Input 2:  

2  
timyr-guev2@beegeek.bzz  
anri-tabuev@beegeek.bzz  
3  
timyr-guev  
timyr-guev  
anri-tabuev  
Sample Output 2:  

timyr-guev@beegeek.bzz  
timyr-guev1@beegeek.bzz  
anri-tabuev1@beegeek.bzz  
## python_3.py  

Скрипт содержит функции сортировки списка на основе пользовательских правил, включая сортировку по длине элементов и лексикографическое сравнение. Возможно использование lambda-функций для создания сложных ключей сортировки.

<img width="829" height="872" alt="image" src="https://github.com/user-attachments/assets/03d46dc4-a41e-4bcb-b077-08816e39ff83" />


## python_4.py

Скрипт предназначен для поиска и подсчета дубликатов в массиве или списке чисел. Используются структуры данных dict и set для выявления повторяющихся значений и организации удобной агрегации.

<img width="1077" height="538" alt="image" src="https://github.com/user-attachments/assets/56f376f9-fc3a-4096-b010-47b4b3eb1602" />

Примечание 2. Начальная часть ответа выглядит так:  
  
2010-Q3  
2017-Q1  
...  
  
## python_5.py

Программа работает с числовыми массивами, группируя числа по их сумме цифр и выводя результаты группировки в виде словарей. Полезна для задач группировки данных по определённому признаку.

<img width="1108" height="756" alt="image" src="https://github.com/user-attachments/assets/b380ab63-9af6-4822-8b9c-f854e77ce37b" />

Sample Input 1:  
  
dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]  

print(get_min_max(dates))  
Sample Output 1:  
  
(datetime.date(1992, 6, 10), datetime.date(2021, 10, 5))  
Sample Input 2:  
  
print(get_min_max([]))  
Sample Output 2:  
  
()  
  
## python_6.py

Скрипт анализирует входные данные, реализует фильтрацию элементов по условиям, связанным с обработкой данных списками и множествами. Реализует выборку уникальных значений и формирование результирующих коллекций.

<img width="882" height="190" alt="image" src="https://github.com/user-attachments/assets/73b94c05-cbd0-49f9-8599-10b21d4226e9" />

Sample Input 1:  
  
date1 = date(2021, 11, 1)  
date2 = date(2021, 11, 22)  
  
print(saturdays_between_two_dates(date1, date2))  
Sample Output 1:  
  
3  
Sample Input 2:  
  
date1 = date(2020, 7, 26)  
date2 = date(2020, 7, 2)  
  
print(saturdays_between_two_dates(date1, date2))  
Sample Output 2:  
  
4    

## files.txt

Этот файл содержит перечень всех файлов, доступных в репозитории: медиафайлы, скрипты, документы и вспомогательные данные.

## Требования

- Python 3.7+
    

## Использование

Каждый скрипт запускается отдельным файлом:

text

`python имя_файла.py`
