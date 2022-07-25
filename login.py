def rull():
  def add_user():
      name=input('enter the name :')
      pin=input('enter the pin :')
      fu_s=name+' '+pin+' '+'\n'+' '
      file=open('new.txt','a')
      file.write(fu_s)
  def login():
      file=open('new.txt')
      reading=file.read().split(' ')
      username=input('enter the username :')
      z=3
      while True:
          if username in reading :
              i=reading.index(username)
              i+=1
              pin=input('enter the pin')
              if 1!=z:
                  if pin==reading[i]:
                      print('log in successfully _____')
                      break
                  else:
                      print('you pin is wrong!!')
                      z-=1
                      pass
              else:
                  break
          else:
              print('userName is wrong!!')
              break
  while True:
      print("""        1)Sign up
      2)Login 
      3)Back
      """)

      c=int(input('enter the choice :'))
      if c==1:
          add_user()
      elif c==2:
          login()
      else:
          print('come again')
          break
rull()