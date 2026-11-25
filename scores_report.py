try:
    with open('C:\\Users\\MEPI\\OneDrive\\Desktop\\Courses\\S1\\Intro to OOP Lab\\Lab 12\\scores.txt', 'r') as file:
          c = 0
          line = file.readline()
          while line != '':
              line = line.rstrip().split(',')
              if line[1].isdecimal():
                  line[1] = int(line[1])
                  c+=1
              if line[0] == 'Karim':
                 print(line[1])
              
              line = file.readline()
          print(c)
except FileNotFoundError:
    print('File not found')
    
try:
    with open('C:\\Users\\MEPI\\OneDrive\\Desktop\\Courses\\S1\\Intro to OOP Lab\\Lab 12\\scores.txt', 'r') as file:

          res = ''
          for line in file:
              line = line.rstrip().split(',')
              if line[0] == 'Maya':
                  line[1] = 88
                  
              if line[0] != 'Nour' and  isinstance(line[1], (int, str)) :
                  if isinstance(line[1], str) and not line[1].isdecimal():
                     break
                  else:

                      res += line[0] + ',' + str(line[1]) + '\n'



except FileNotFoundError:
    print('File not found') 


try:
    with open('C:\\Users\\MEPI\\OneDrive\\Desktop\\Courses\\S1\\Intro to OOP Lab\\Lab 12\\scores.txt', 'w') as file:
          file.write(res)
          file.close()

except FileNotFoundError:
    print('File not found')          
    
  
try:
    with open('C:\\Users\\MEPI\\OneDrive\\Desktop\\Courses\\S1\\Intro to OOP Lab\\Lab 12\\pass.txt', 'w') as file2:
          file = open('C:\\Users\\MEPI\\OneDrive\\Desktop\\Courses\\S1\\Intro to OOP Lab\\Lab 12\\scores.txt', 'r')
          for line in file:
              line = line.rstrip().split(',')
              if int(line[1]) >= 60:
                 file2.write(line[0] + '\n')
          file.close()
          file2.close()

except FileNotFoundError:
    print('File not found') 
    
    
"""
Other method:
    try:
        with open('C:\\Users\\MEPI\\OneDrive\\Desktop\\Courses\\S1\\Intro to OOP Lab\\Lab 12\\scores.txt', 'r') as file:
              c = 0

              for line in file:
                  line = line.rstrip().split(',')
                  if line[1].isdecimal():
                      line[1] = int(line[1])
                      c+=1
                  if line[0] == 'Karim':
                     print(line[1])
                  
              print(c)
    except FileNotFoundError:
        print('File not found')
"""