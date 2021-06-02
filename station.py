from fare import Fare
from passenger import Passenger


class Station:
    """
    Класс вокзала
    """

    def __init__(self):
        """
        Конструктор класса
        """
        self.fares = []  # список доступных тарифов вокзала
        self.passengers = []  # список людей, купивших билеты по тарифам вокзала

    def add_new_fare(self, fare_destination: str, fare_price: int, note="нет"):
        """
        Пополнить тарифы этого вокзала новым тарифом
        :param fare_destination: пункт назначения
        :param fare_price: цена билета по тарифу
        :param note: примечание к тарифу (опционально)
        """
        new_fare = Fare(fare_destination, fare_price, note)
        self.fares.append(new_fare)

    def register_ticket_purchase(self, fare_destination: str, first_name: str, last_name: str,
                                 passport_series: int, passport_number: int):
        """
        Зарегистрировать покупку билета для данного человека по данному направлению
        :param fare_destination: выбранное направление
        :param first_name: имя
        :param last_name: фамилия
        :param passport_series: серия паспорта
        :param passport_number: номер паспорта
        """
        the_fare = self.get_fare_by_destination(fare_destination)
        # Если человек ещё ни разу не покупал билеты, то вносим его в базу, иначе - получаем из базы
        if not self.is_passenger_exist(passport_series, passport_number):
            the_passenger = Passenger(first_name, last_name, passport_series, passport_number)
            self.passengers.append(the_passenger)
        else:
            the_passenger = self.get_passenger_by_series_and_number(passport_series, passport_number)
        the_passenger.buy_ticket(the_fare)
        the_fare.add_passenger(the_passenger)

    def display_information_about_passenger(self, passport_series: int, passport_number: int):
        """
        Отобразить информацию о пассажире и купленных им билетах по серии и номеру паспорта
        :param passport_series: серия паспорта
        :param passport_number: номер паспорта
        """
        for passenger in self.passengers:
            if passenger.get_passport_series() == passport_series and \
                    passenger.get_passport_number() == passport_number:
                print(f"Пассажир: {passenger.get_personal_data()}\n"
                      f"Стоимость купленных пассажиром билетов: {passenger.get_total_cost_of_tickets()} руб.")
                return
        print(f"Пассажир с серией пасспорта {passport_series} и номером паспорта {passport_number} ещё не покупал"
              f" билетов!")

    def display_information_about_fare(self, fare_destination: str):
        """
        Отобразить информацию о данном тарифе
        :param fare_destination: пункт назначения
        """
        for fare in self.fares:
            if fare.get_fare_destination().lower() == fare_destination.lower():
                print(fare.get_fare_description())
                return
        print(f"Тарифа «Ульяновск-{fare_destination}» не существует...")

    def display_passengers_by_fare(self, fare_destination: str):
        """
        Отобразить всех пассажиров, купивших билеты на данное направление
        :param fare_destination: название пункта назначения
        """
        for fare in self.fares:
            if fare.get_fare_destination().lower() == fare_destination.lower():
                fare_passengers = fare.get_passengers()
                if len(fare_passengers) > 0:
                    print(f"Список пассажиров, купивших билеты по тарифу «Ульяновск-{fare_destination}»:")
                    for passenger in self.passengers:
                        print(passenger.get_personal_data())
                else:
                    print(f"Пассажиров, купивших билеты по тарифу «Ульяновск-{fare_destination}», пока нет.")
                return
        print(f"Тарифа «Ульяновск-{fare_destination}» не существует...")

    def display_fares(self):
        """
        Отобразить список доступных тарифов
        """
        if len(self.fares) > 0:
            print(f"Список доступных тарифов:")
            for fare in self.fares:
                print(fare.get_fare_description())
        else:
            print(f"Тарифов пока нет...")

    def get_fare_by_destination(self, fare_destination: str) -> Fare:
        """
        Получить тариф по пункту назначения (Предварительно проверить на существование методом is_fare_exist())
        :param fare_destination: название пункта назначения
        :return: искомый тариф (объёкт Fare)
        """
        for fare in self.fares:
            if fare.get_fare_destination().lower() == fare_destination.lower():
                return fare

    def is_fare_exist(self, fare_destination: str) -> bool:
        """
        Проверить, существует ли тариф по данному пункту назначения
        :param fare_destination: название пункта назначения
        :return: True, если существует; иначе - False
        """
        for fare in self.fares:
            if fare.get_fare_destination().lower() == fare_destination.lower():
                return True
        return False

    def get_passenger_by_series_and_number(self, passenger_passport_series: int,
                                           passenger_passport_number: int) -> Passenger:
        """
        Получить человека по серии и номеру паспорта (Предварительно проверить человека на наличие в базе методом
         is_passenger_exist())
        :param passenger_passport_series: серия паспорта
        :param passenger_passport_number: номер паспорта
        :return: искомый человек (объёкт Passenger)
        """
        for passenger in self.passengers:
            if passenger.get_passport_series() == passenger_passport_series and \
                    passenger.get_passport_number() == passenger_passport_number:
                return passenger

    def is_passenger_exist(self, passenger_passport_series: int, passenger_passport_number: int) -> bool:
        """
        Проверить, существует ли человек в базе
        :param passenger_passport_series: серия паспорта человека
        :param passenger_passport_number: номер паспорта человека
        :return: True, если существует; иначе - False
        """
        for passenger in self.passengers:
            if passenger.get_passport_series() == passenger_passport_series and \
                    passenger.get_passport_number() == passenger_passport_number:
                return True
        return False
