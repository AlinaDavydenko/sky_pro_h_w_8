from django.contrib import admin

from users.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'payment_method', 'payment_date')
    list_filter = ('payment_method',)
    search_fields = ('user__email', 'amount')
