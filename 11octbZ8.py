#Во входном файле INPUT.TXT записаны три натуральных числа A, B и C через пробел. Числа A и B ≤ 10^2, а C ≤ 10^6.
#В выходной файл нужно вывести YES в том случае, если A*B=C и вывести NO в противном случае.

input_data = open('input.txt','r')
data = input_data.read()
a = int(data[0])
b = int(data[1])
c = int(data[2])
if a <= 10**10 and b <= 10**10
