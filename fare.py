class Fare:
    """
    Класс тарифа
    """

    def __init__(self, destination: str, price: int, note: str):
        """
        Конструктор класса
        :param destination: пункт назначения
        :param price: цена билета по этому тарифу
        :param note: примечание тарифа
        """
        self.destination = destination
        self.price = price
        self.note = note
        self.passengers = []  # список всех пассажиров, купивших билет по этому тарифу

    def get_price(self) -> int:
        """
        Получить цену билета по этому тарифу
        :return: цена билета
        """
        return self.price

    def get_fare_destination(self) -> str:
        """
        Получить пункт назначения этого тарифа
        :return: пункт назначения
        """
        return self.destination

    def get_fare_description(self) -> str:
        """
        Получить описание этого тарифа
        :return: описание тарифа
        """
        if self.note.lower() != "нет":
            return f"Тариф «Ульяновск-{self.destination}» (Цена билета: {self.price} руб; Примечание: {self.note})"
        else:
            return f"Тариф «Ульяновск-{self.destination}» (Цена билета: {self.price} руб.)"

    def add_passenger(self, passenger):
        """
        Зарегистрировать пассажира на направление по этому тарифу
        :param passenger: регистрируемый пассажир
        """
        self.passengers.append(passenger)

    def get_passengers(self) -> []:
        """
        Получить список всех пассажиров, купивших билеты по этому тарифу
        :return: список пассажиров
        """
        return self.passengers
