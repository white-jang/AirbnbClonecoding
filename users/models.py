from django.db import models
from django.contrib.auth.models import AbstractUser

# AbstractUser이기 때문에 코드에서만 쓰이고 DB에 저장 X
# => 'Abstract' Model


class User(AbstractUser):
    """ Custom user model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )
    # gender를 선택권을 주는 CharField로 수정하기 위한 튜플 => choices 파라미터에 이용
    # GENDER_MALE 값이 DB에 저장되고, "Male"은 (admin)form에서 보여지는 값

    LANGAUGE_ENGLISH = "english"
    LANGAUGE_KOREAN = "korean"

    LANGAUGE_CHOICES = (
        (LANGAUGE_ENGLISH, "en"),
        (LANGAUGE_KOREAN, "ko"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )
    # currency(환율) 선택권

    avatar = models.ImageField(blank=True)
    # blank=True의 경우 form에도 적용되어 값을 필수로 채우지 않아도 됨
    # null=True는 DB에서만 사용됨
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    langauge = models.CharField(choices=LANGAUGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
