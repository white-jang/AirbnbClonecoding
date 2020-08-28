from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):
    """ Conversation Model Definition """

    # 여러 명이 한 번에 대화 가능 (대화방)

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):
    """ Message Model Definition """

    # 대화방에서 유저가 보내는 메시지

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.text}"
