name=str(input())
age=int(input())
if age<7:
    print('entrepreneur')
elif 7<=age<=14:
    print('Hello, ',name,'! You are in',(age%7)+1,'klass')
elif 7<=age<=17:
     print('Hello, ',name,'! You are in',(age%7)+1,'klass and you have',(age%15)+1,'years of programing experience. Sounds cool!')
elif 18<=age<=21:
    print('Hello, ',name,'! You are at',(age%18)+1,'course and you have',(age%15)+1,'years of programing experience. Sounds cool!')
else:
     print('Hello, ',name,'! You are entrepreneur and you have',(age%15)+1,' years of programing experience. Sounds cool!')