from rest_framework.routers import SimpleRouter

from materials.views import (CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView,
                             LessonDestroyAPIView, LessonRetrieveAPIView)

from materials.apps import MaterialsConfig

from django.urls import path

app_name = MaterialsConfig.name

router = SimpleRouter

router.register('', CourseViewSet)

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update')
]

urlpatterns += router.urls
