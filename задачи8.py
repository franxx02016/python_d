word = "телефон"
reversed_word = word[::-1] # TODO Разверните слово с помощью слайсирования
print("Слово", word, "задам наперед:", reversed_word)

str_ = "sdkfjsdkjfnksjdnfkjsdnfkjsndfkjsndfkjsndfkjsnd"
str_1 = set('sdkfjsdkjfnksjdnfkjsdnfkjsndfkjsndfkjsndfkjsnd'
# TODO найдите и распечатайте количество уникальных символов в строке
print(len(str_1))

list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл"]
last_player = list_players[-1]
reestr = {"Первый участник": list_players[0]}

print("Последний участник:", last_player)
print("Первый участник:", reestr["Первый участник"])

fruits = ["яблоко", "банан", "опельсин", "виноград"]  # список фруктов

incorrect_word = fruits[2]  # получаем из списка слово с опечаткой
correct_word = "а" + incorrect_word[1:]  # исправляем слово с опечаткой, путем создания нового слова

fruits[2] = correct_word  # заменяем слово в списке
print(fruits)

1 вар # TODO исправьте опечатку в слове
fruits = ["яблоко","банан","опельсин","виноград"]
fruits[2] = "апельсин"
print (fruits)

fruits = ["яблоко", "панан", "апельсин", "виноград"]  # список фруктов

incorrect_word = fruits[1]  # получаем из списка слово с опечаткой
correct_word = "б" + incorrect_word[1:]  # исправляем слово с опечаткой, путем создания нового слова

fruits[1] = correct_word  # заменяем слово в списке
print(fruits)
