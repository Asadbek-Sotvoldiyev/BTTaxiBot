from django.db import models

class BotUser(models.Model):
    chat_id = models.BigIntegerField(unique=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Driver(models.Model):
    chat_id = models.BigIntegerField(unique=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    car_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name



class OrderTaxi(models.Model):
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)
    from_location = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    person_count = models.PositiveIntegerField(null=True, blank=True)
    direction = models.CharField(max_length=100, null=True, blank=True)
    leave_time = models.CharField(max_length=100, null=True, blank=True)
    driver_status=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user}, To_address: {self.direction}"


class GroupChatId(models.Model):
    chat_id = models.CharField(max_length=100)
    group_name = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name
