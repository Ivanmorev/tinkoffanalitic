class Error(Exception):
    pass

class ValueTooLargeError(Error):
    pass

def inputnumber(message):
  while True:
    try:
       userInput = int(input(message))
       if userInput > 30:
           raise ValueTooLargeError
    except ValueError:
       print("Not an integer! Try again.")
       continue
    except ValueTooLargeError:
       print("Input must be <=30")
       continue
    else:
       return userInput 
       break

     
n = inputnumber("Input n ")
m = inputnumber("Input m ")
id = 0

prime = [[0 for j in range(m)] for i in range(n)]

for x in range(len(prime)):
    for y in range(len(prime[x])):
        if x % 2 == 0:
            prime[x][y] = ('  '+str(id))
            print(prime[x][y][-3:], end=' ')
        else:
            prime[x][y] = ('  ' + str((x+1) * m-(y+1)))
            print(prime[x][y][-3:], end=' ')
        id = id + 1
    print()


