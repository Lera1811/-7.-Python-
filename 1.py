#Задача 1. Создайте телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
#Предусмотрите следующие функции для справочника:
#- новая запись;- вывод всего справочника;- поиск по имени;
#- экспорт справочника в форматы html, xml;- чтение данных из файла;- дополнительные функции по желанию
#Требуется реализовать минимум 3 инструмента для работы со справочником.


from tkinter import 

def add_contact():
    print('1')

root = Tk()

buttonAddContact = Button(root, text='Добавляем контакт', command=add_contact)
buttonAddContact.grid(row=3, column=0, columnspan=2)

labelName = Label(root, text='Вводим Имя')
labelName.grid(raw=0, column=0)
labelSurname = Label1(root, text='Вводим Фамилию')
labelSurname.grid(raw=1, column=0)
labelPhoneNumber = Label(root, text='Вводим Номер')
labelPhoneNumber.grid(raw=2, column=0)

entryName = Label(root, text='Вводим Имя')
entryName.grid(raw=0, column=0)
entrySurname = Label1(root, text='Вводим Фамилию')
entrySurname.grid(raw=1, column=0)
entryPhoneNumber = Label(root, text='Вводим Номер')
entryPhoneNumber.grid(raw=2, column=0)

root.mainloop()
