# Routing - 특정 주소를 들어갔을 때, view 를 돌려줘야 한다
# 특정 주소를 만들어주는 작업 = urls.py
# 제일 먼저 요청을 받는 파일 !!!

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accountapp.urls'))  # accountapps.urls.py 의 파일을 참조하여 안에서 다시 분기를 하는
]