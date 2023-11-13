print("Сколько будет 2 в 10-ой степени?")
print("Ответ в файле по адресу --> D:\Python Projects\st_theanswerishere.txt")

#Создание и запись в файл
with open("D:\\Python Projects\st_theanswerishere.txt", "w") as answer:
    answer.write("2 ^ 10 = 1024")
