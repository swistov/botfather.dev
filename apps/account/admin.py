from django.contrib import admin

from apps.account.models import User, Referral


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["user_id", "name", "username"]
    search_fields = ["user_id", "name", "username"]

    readonly_fields = ["created", "modified"]
    save_on_top = True


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ["user", "referrer"]
