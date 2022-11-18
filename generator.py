from random import choice
print("Hello this is password generator.")
#Cái này là mày nhập tài khoản mày muốn tạo là gì, tài khoản facebook hay gmail gì đó
application = input('Which application do you want to create an account? ')
account_name = input('Enter your account name: ')   
#Cái này là tạo 1 cái list chứa tất cả kí tự,chữ cái,số trong bảng mã ASCII        
arr = [ chr(i) for i in range(32,127)]
s=''
#Cái này dùng để hỏi độ dài của cái password mày mong muốn nhưng tối thiểu là 8 kí tự
while True:
    n = int(input('How many character in your password do you want to create? (At least 8 characters) '))
    if n<8:
        print('Please enter at least 8 characters')
    else:
        break
#Cái này là tạo mật khẩu ngẫu nhiên bằng cách dùng vòng lặp for và hàm choice chọn ngẫu nhiên kí tự trong bảng
#mã ASCII tao vừa tạo trong cái list arr
for i in range(n+1):
    s+=choice(arr)
#Đoạn này để thông báo chương trình nó tự động lưu kết quả ở địa chỉ nào 
print('Your password is : {}\nI will store it in C:\\linh ta linh tinh\\secret\\password.txt \nPlease check it out'.format(s))
#Cái này là mở file password.txt để chương trình lưu cái mật khẩu cho mày
with open('password.txt','a') as file:
     file.write(application.title()+': '+account_name+'\npassword: '+s+'\n')