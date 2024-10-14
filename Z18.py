#Требуется вычислить факториал целого числа N. Факториал обозначают как N! и вычисляют по формуле:
#N! = 1 * 2 * 3 * … * (N-1) * N, причем 0! = 1.
#Так же допустимо рекуррентное соотношение: N! = (N-1)! * N

#В единственной строке входного файла INPUT.TXT записано одно целое неотрицательное число N (N < 1000).

#В выходной файл OUTPUT.TXT нужно вывести одно целое число — значение N!.

data_input = open('input.txt','r')
data = data_input.read()
a = int(data)
factorial = 1
for i in range(2,a + 1):
    factorial *=i
data_output = open('output.txt','w')
data_output.write(str(factorial))
data_input.close()
data_output.close()