

from django.urls import path
from .views import convert, index

urlpatterns = [
    path('convert/', convert, name='convert'),
    path('', index, name='index'),  # لعرض صفحة index.html عند الوصول إلى الجذر
]
