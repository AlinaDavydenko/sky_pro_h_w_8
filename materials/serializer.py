from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    lesson = LessonSerializer()
    lessons = SerializerMethodField()

    def get_lessons(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    lesson_count_course = SerializerMethodField()
    lesson = LessonSerializer()

    def get_lesson_count_course(self, lesson):
        return Lesson.object.filter(course=lesson.course).count()

    class Meta:
        model = Course
        fields = ('name', 'description', 'picture', 'lesson_count_course')

