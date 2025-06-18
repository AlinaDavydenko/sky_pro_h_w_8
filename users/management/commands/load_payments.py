from django.core.management.base import BaseCommand
from users.models import Payment
from django.contrib.auth import get_user_model
from materials.models import Course, Lesson  # предполагается, что эти модели существуют

User = get_user_model()


class Command(BaseCommand):
    help = 'Load payments data into the database'

    def handle(self, *args, **options):
        payments_data = [
            {
                'user': User.objects.get(pk=1),
                'paid_course': Course.objects.get(pk=1),
                'paid_lesson': None,
                'amount': 10000.00,
                'payment_method': 'transfer'
            },
            {
                'user': User.objects.get(pk=2),
                'paid_course': None,
                'paid_lesson': Lesson.objects.get(pk=5),
                'amount': 3000.00,
                'payment_method': 'cash'
            }
        ]

        for payment_data in payments_data:
            Payment.objects.create(**payment_data)

        self.stdout.write(self.style.SUCCESS('Successfully loaded payments data'))
