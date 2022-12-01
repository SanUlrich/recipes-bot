from data import breakfast, lunch, dinner
import random


class BreakfastAnswer:
    @staticmethod
    def get_id():
        return str(breakfast.data[random.randint(0, len(breakfast.data))])


class LunchAnswer:
    @staticmethod
    def get_id():
        return str(lunch.data[random.randint(0, len(lunch.data))])


class DinnerAnswer:
    @staticmethod
    def get_id():
        return str(dinner.data[random.randint(0, len(dinner.data))])

