def main():
    tasks = []  # Создаем пустой список для хранения задач

    print("Добро пожаловать в консольный To-Do лист!")

    while True:
        # Выводим меню для пользователя
        print("\n--- Меню ---")
        print("1. Показать список задач")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выйти")

        choice = input("\nВыберите действие (введите номер 1-4): ")

        if choice == '1':
            if not tasks:
                print("\nВаш список задач пуст! 🎉")
            else:
                print("\nВаши задачи:")
                # Выводим задачи с их порядковыми номерами
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif choice == '2':
            new_task = input("\nВведите новую задачу: ")
            tasks.append(new_task)
            print(f"Задача '{new_task}' успешно добавлена!")

        elif choice == '3':
            if not tasks:
                print("\nСписок пуст, удалять нечего.")
                continue

            try:
                task_num = int(input("\nВведите номер задачи, которую хотите удалить: "))
                # Проверяем, существует ли такой номер
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)  # index на 1 меньше номера
                    print(f"Задача '{removed_task}' удалена!")
                else:
                    print("Ой! Задачи с таким номером нет.")
            except ValueError:
                print("Ошибка: Пожалуйста, введите число, а не текст.")

        elif choice == '4':
            print("\nДо свидания! Хорошего дня!")
            break  # Выходим из цикла и завершаем программу

        else:
            print("\nНеверный ввод. Пожалуйста, выберите число от 1 до 4.")


if __name__ == "__main__":
    main()