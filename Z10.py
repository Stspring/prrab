#В единственной строке входного файла INPUT.TXT записаны 4 числа: 
# A, B, C и D – целые коэффициенты кубического уравнения. Каждый коэффициент по модулю меньше 32768, A ≠ 0.

#В единственную строку выходного файла OUTPUT.TXT нужно вывести через пробел в порядке возрастания 
# все корни заданного кубического уравнения. Кратные корни следует выводить только один раз.

data_input = open('input.txt','r')
data = data_input.read()
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
d = int(data[3])
x3 = " "
x1 = " "
x2 = " "
for i in range(-100,100+1):
    if (a*i**3+b*i**2+c*i+d)==0:
        x1=i
        for v in range(i+1,100+1):
            if (a*v**3+b*v**2+c*v+d)==0:
                    x2=v
                    for w in range(v+1,100+1):
                         if (a*w**3+b*w**2+c*w+d)==0:
                              x3=w
                              break  
                    break
        break
data_output = open('output.txt','w')
if x3 != ' ': # если х не равен 0, выводим 3 хса
    data_output.write(str(x1)+' '+str(x2)+' '+str(x3))
elif x2 !=' ':
     data_output.write(str(x1)+' '+str(x2))
else: 
     data_output.write(str(x1))
data_input.close()
data_output.close()


    
 