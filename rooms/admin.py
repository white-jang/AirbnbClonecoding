from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),  # 접기 기능 추가
                "fields": ("amenities", "facilites", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    # ordering = ("name", "price")
    # 설정한 필드를 기준으로 정렬 (1.name, 2.price)

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilites",
        "house_rules",
        "city",
        "country",
    )

    search_fields = ("city", "^host__username")
    # 해당 field를 기준으로 검색할 수 있게 해줌
    # icontains한 설정으로 대소문자 구별 없이 검색 가능
    # room 모델의 host 필드(User)가 가진 username으로도 검색 가능 "__" 이용

    filter_horizontal = (
        "amenities",
        "facilites",
        "house_rules",
    )
    # ManyToMany 관계에서 사용할 수 있는 필터

    def count_amenities(self, obj):
        # obj는 row
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """

    pass
