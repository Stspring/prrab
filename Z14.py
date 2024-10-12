#Требуется написать программу, определяющую наименьшее общее кратное (НОК) чисел a и b.

#В единственной строке входного файла INPUT.TXT записаны два натуральных числа А и В через пробел, не превышающих 46340.

#В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — НОК чисел А и В.


data_input = open('input.txt','r')
data = data_input.read()
data = data.split()

a = int(data[0])
b = int(data[1])
a1=a
b1=b

# Алгоритм Евклида(ищнм НОД)
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
LCM =(a1*b1)/(a+b) 
#Для получения результата достаточно просто перемножить эти числа и разделить полученное произведение на НОД. 
data_output = open('output.txt','w')
data_output.write(str(int(LCM)))
data_input.close()
data_output.close()
