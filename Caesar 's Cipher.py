print('Добро пожаловать в Де/Шифратор Цезаря!')
code = int(input('Зашифровать - 1, Расшифровать - 2: '))
lang = input('Введите язык ru - русский, eng - английский: ')
step = int(input('Введите шаг сдвига вправо: '))
text = input('Введите текст: ')
if code == 1:
    cipher = ''
    if lang == 'eng':
        for i in range(len(text)):
            if text[i].islower():
                cipher += chr(((ord(text[i]) -97 + step) % 26) + 97)
            elif text[i].isupper():
                cipher += chr(((ord(text[i]) -65 + step) % 26) + 65)
            else:
                cipher += text[i]
    if lang == 'ru':
        for i in range(len(text)):
            if text[i].islower():
                cipher += chr(((ord(text[i]) - 1072 + step) % 32) + 1072)
            elif text[i].isupper():
                cipher += chr(((ord(text[i]) - 1040 + step) % 32) + 1040)
            else:
                cipher += text[i]
    print(cipher)
if code == 2:
    decipher = ''
    if lang == 'eng':
        for i in range(len(text)):
            if text[i].islower():
                decipher += chr(((ord(text[i]) - 97 + 26 - step) % 26) + 97)
            elif text[i].isupper():
                decipher += chr(((ord(text[i]) - 65 + 26 - step) % 26) + 65)
            else:
                decipher += text[i]
    if lang == 'ru':
        for i in range(len(text)):
            if text[i].islower():
                decipher += chr(((ord(text[i]) - 1072 + 32 - step) % 32) + 1072)
            elif text[i].isupper():
                decipher += chr(((ord(text[i]) - 1040 + 32 - step) % 32) + 1040)
            else:
                decipher += text[i]
    print(decipher)