
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # TODO 空欄にすると、URLを何も指定しない場合、todoアプリを開く
    path('', include('todo.urls'))
]
