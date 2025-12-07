text = input('Введите строку: ').lower() #мы же не доверяем вводу пользователя, верно? :)
start_index = text.rindex('h')
end_index = text.index('h')
result = text[start_index-1:end_index:-1]
print('Развёрнутая последовательность между первым и последним h:', result)