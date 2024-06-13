fruits = ["apple", "banana", "cherry"]
print(fruits)
print("apple" in fruits)
print("kiwi" in fruits)

my_list = list([])
print(my_list)

print(len(fruits))

other_list = ["apple", 2, 5.9, True, [1, 2, 5]]  #лучше в списке хранить однотипные данные
print(other_list)
print(len(other_list))

new_list1 = [1, 2, 3]
new_list2 = [1, 4, 3]
new_list3 = [1, 2, 3]

print(new_list1 == new_list2)
print(new_list1 == new_list3)

print(bool([]))
print(bool([1]))

element1 = "apple"  #альтернативная инициация списка
element2 = "kiwi"
element3 = "banana"
list_fruits = [element1, element2, element3]
print(list_fruits)

word = "hello!"
my_newlist = list(word)
print(my_newlist)