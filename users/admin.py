from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)  # decorater
class UserAdmin(UserAdmin):
    """ Custom user admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "langauge",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    # django에서 기본으로 제공하는 admin User 패널의 fieldset과 Custom fieldset을 합침
