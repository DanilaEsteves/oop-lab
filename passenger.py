class Passenger:
    """
    Класс пассажира
    """

    def __init__(self, first_name: str, last_name: str, passport_series: int, passport_number: int):
        """
        Конструктор класса
        :param first_name: имя
        :param last_name: фамилия
        :param passport_series: серия паспорта
        :param passport_number: номер паспорта
        """
        self.first_name = first_name
        self.last_name = last_name
        self.passport_series = passport_series
        self.passport_number = passport_number
        self.tickets = []  # купленные пассажиром билеты

    def get_passport_series(self) -> int:
        """
        Получить серию паспорта этого пассажира
        :return: серия паспорта
        """
        return self.passport_series

    def get_passport_number(self) -> int:
        """
        Получить номер паспорта этого пассажира
        :return: номер паспорта
        """
        return self.passport_number

    def get_personal_data(self) -> str:
        """
        Получить персональные данные этого пассажира
        :return: персональные данные
        """
        return f"{self.first_name} {self.last_name} (Серия: {self.passport_series}, номер: {self.passport_number})"

    def buy_ticket(self, ticket):
        """
        Зарегистрировать покупку билета по данному тарифу этим пассажиром
        :param ticket: покупаемый билет
        """
        self.tickets.append(ticket)

    def get_total_cost_of_tickets(self) -> int:
        """
        Получить совокупную стоимость купленных этим пассажиром билетов
        :return: стоимость купленных билетов
        """
        total_cost = 0
        for ticket in self.tickets:
            total_cost += ticket.get_price()
        return total_cost
