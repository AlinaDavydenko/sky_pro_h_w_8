from rest_framework import serializers
from users.models import Payment
from materials.models import Course, Lesson


class CoursePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name')


class LessonPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'name')


class PaymentSerializer(serializers.ModelSerializer):
    paid_course = CoursePaymentSerializer(read_only=True)
    paid_lesson = LessonPaymentSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'
