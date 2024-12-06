from django.contrib import admin
from .models import BotUser, Driver, OrderTaxi, GroupChatId

# BotUser modelini ro'yxatga olish
@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'chat_id', 'created_at')  # Qo'shimcha chat_id va created_at ustunlari
    search_fields = ('full_name', 'phone_number', 'chat_id')  # Qidiruv maydonlariga chat_id ham qo'shildi
    list_filter = ('created_at',)  # Qidiruvni vaqt bo'yicha filtrlash

# Driver modelini ro'yxatga olish
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'car_info', 'created_at')  # Mashina ma'lumotlari va vaqtni qo'shish
    search_fields = ('full_name', 'phone_number', 'car_info')  # Mashina ma'lumotlarini qidirish
    list_filter = ('created_at',)  # Vaqt bo'yicha filtrlash

# OrderTaxi modelini ro'yxatga olish
@admin.register(OrderTaxi)
class OrderTaxiAdmin(admin.ModelAdmin):
    list_display = ('user', 'driver', 'from_location', 'person_count', 'direction', 'leave_time', 'driver_status', 'created_at')
    search_fields = ('user__full_name', 'driver__full_name', 'from_location', 'direction')
    list_filter = ('driver_status', 'created_at')  # Holat va vaqt bo'yicha filtrlar

# GroupChatId modelini ro'yxatga olish
@admin.register(GroupChatId)
class GroupChatIdAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'chat_id')  # Guruh nomi va chat_id
    search_fields = ('group_name', 'chat_id')  # Guruh nomi va chat_id bo'yicha qidirish

