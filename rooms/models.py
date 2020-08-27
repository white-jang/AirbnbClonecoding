from django.db import models
from django_countries.fields import CountryField
from core import models as cores_models
from users import models as user_models


class AbstractItem(cores_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ Roomtype Model Definition """

    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]  # 알파벳순으로 값들 정렬


class Amenity(AbstractItem):
    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "Amenities"
        # admin 페이지에서 확인할 수 있는 모델명 설정
        # 이 변수를 이용하지 않을 경우 클래스 이름 + "s"로 자동 설정됨


class Facility(AbstractItem):
    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "House Rule"
        # admin 페이지에서 확인할 수 있는 모델명 설정
        # 모델명을 덮어쓰기 하듯 새롭게 지정 (이름+"s"는 없어지지 않음)
        # House rules => House Rules


class Room(cores_models.TimeStampedModel):
    """ Room Model definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()  # 0~24시간의 "시간"만 표시
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilites = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)

    def __str__(self):
        return self.name


class Photo(cores_models.TimeStampedModel):
    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
