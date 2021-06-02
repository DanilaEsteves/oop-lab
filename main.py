from station import Station


def get_started_with_station_ticket_office():
    """
    Начать работу с кассой вокзала
    """
    the_station = Station()

    # Изначально вокзал имеет 5 тарифов
    the_station.add_new_fare("Тольятти", 400)
    the_station.add_new_fare("Самара", 600, "С пересадкой в г. Тольятти")
    the_station.add_new_fare("Краснодар", 1000)
    the_station.add_new_fare("Саранск", 350, "Через Сурское")
    the_station.add_new_fare("Нижний Новгород", 800)

    print("Начинаем работу с кассой вокзала «Ульяновск Центральный». Напишите:"
          "\n— «1», если Вы хотите вывести список доступных тарифов;"
          "\n— «2», если Вы хотите добавить новый тариф;"
          "\n— «3», если Вы хотите получить подробную информацию о конкретном тарифе;"
          "\n— «4», если Вы хотите получить список пассажиров, купивших билеты по конкретному тарифу;"
          "\n— «5», если Вы хотите зарегистрировать покупку билета;"
          "\n— «6», если Вы хотите рассчитать стоимость купленных пассажиром билетов;"
          "\n— «-1», если Вы хотите завершить работу с ИС.")

    command = input("Введите команду: ")
    while command != "-1":
        if command == "1":
            the_station.display_fares()
        elif command == "2":
            the_fare_destination = input("Введите пункт назначения: ")
            the_fare_price = int(input(f"Введите цену тарифа «Ульяновск-{the_fare_destination}»: "))
            the_fare_note = input(f"Введите примечание к тарифу «Ульяновск-{the_fare_destination}» "
                                  f"(Если примечания нет, то введите «Нет»): ")
            the_station.add_new_fare(the_fare_destination, the_fare_price, the_fare_note)
            print(f"Тариф «Ульяновск-{the_fare_destination}» успешно добавлен!")
        elif command == "3":
            the_fare_destination = input("Введите пункт назначения: ")
            the_station.display_information_about_fare(the_fare_destination)
        elif command == "4":
            the_fare_destination = input("Введите пункт назначения: ")
            the_station.display_passengers_by_fare(the_fare_destination)
        elif command == "5":
            fare_destination = input("Введите пункт назначения: ")
            if the_station.is_fare_exist(fare_destination):
                passenger_first_name = input("Введите имя: ")
                passenger_last_name = input("Введите фамилию: ")
                passenger_passport_series = int(input("Введите серию паспорта: "))
                passenger_passport_number = int(input("Введите номер паспорта: "))
                the_station.register_ticket_purchase(fare_destination, passenger_first_name, passenger_last_name,
                                                     passenger_passport_series, passenger_passport_number)
                print(f"{passenger_first_name} {passenger_last_name} приобрёл билет на поездку по тарифу "
                      f"«Ульяновск-{fare_destination}».")
            else:
                print("Тарифа по такому направлению нет..")
        elif command == "6":
            passenger_passport_series = int(input("Введите серию паспорта: "))
            passenger_passport_number = int(input("Введите номер паспорта: "))
            the_station.display_information_about_passenger(passenger_passport_series, passenger_passport_number)
        elif command == "7":
            print("Напишите:"
                  "\n— «1», если Вы хотите вывести список доступных тарифов;"
                  "\n— «2», если Вы хотите добавить новый тариф;"
                  "\n— «3», если Вы хотите получить подробную информацию о конкретном тарифе;"
                  "\n— «4», если Вы хотите получить список пассажиров, купивших билеты по конкретному тарифу;"
                  "\n— «5», если Вы хотите зарегистрировать покупку билета;"
                  "\n— «6», если Вы хотите рассчитать стоимость купленных пассажиром билетов;"
                  "\n— «-1», если Вы хотите завершить работу с кассой вокзала.")
        else:
            print("Некорректная команда, повторите попытку! (Напишите «7», чтобы узнать список доступных команд)")
        command = input("Введите команду: ")
    print("Работа с кассой вокзала «Ульяновск Центральный» закончена.")


if __name__ == '__main__':
    get_started_with_station_ticket_office()
