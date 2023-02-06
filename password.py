my_password = 'a123456'
x = 1
while x <= 3:
    password = input('請輸入密碼： ')
    if password == my_password:
        print('登入成功!')
        break
    else:
        print(f'密碼錯誤! 還有{3-x}次機會')
        x += 1