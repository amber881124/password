my_password = 'a123456'
most = 3
x = 1
while x <= most:
    password = input('請輸入密碼： ')
    if password == my_password:
        print('登入成功!')
        break
    else:
        print('密碼錯誤!')
        if most-x > 0:
            print(f'還有{most-x}次機會')
        x += 1