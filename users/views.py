from rest_framework.viewsets import ModelViewSet

from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from users.models import Payment

from users.serialize import PaymentSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    # фильтруемые поля
    filterset_fields = {
        'paid_course': ['exact'],
        'paid_lesson': ['exact'],
        'payment_method': ['exact'],
    }

    # Определяем поля для сортировки
    ordering_fields = ['payment_date']
    ordering = ['-payment_date']  # сортировка по умолчанию

    def get_queryset(self):
        queryset = super().get_queryset()

        # Дополнительная фильтрация по курсу (альтернативный вариант)
        course_id = self.request.query_params.get('course_id')
        if course_id:
            queryset = queryset.filter(paid_course__id=course_id)

        # Дополнительная фильтрация по уроку (альтернативный вариант)
        lesson_id = self.request.query_params.get('lesson_id')
        if lesson_id:
            queryset = queryset.filter(paid_lesson__id=lesson_id)

        return queryset
