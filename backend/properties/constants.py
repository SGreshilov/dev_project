from django.db.models import  TextChoices, IntegerChoices


class PropertyStatus(IntegerChoices):
    """Статус объекта в собственности"""

    ON_SALE = 1, 'В продаже'
    SOLD = 2, 'Продано'
    BOOKED = 3, 'Забронировано'


class PropertyType(TextChoices):
    """Тип объекта в собственности"""

    FLAT = 'flat', 'Квартира'
    APARTMENTS = 'apartments', 'Апартаменты'
    PARKING = 'parking', 'Парковочное место'
    COMMERCIAL = 'commercial', 'Коммерческое помещение'
