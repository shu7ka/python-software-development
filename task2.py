# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator = ","):
    new_first_group = first_group.split(separator)
    new_second_group = second_group.split(separator)
    general = set(new_first_group).intersection(set(new_second_group))
    return sorted(general)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
