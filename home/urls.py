from django.urls import path
from .views import (
    sumka_list,
    sumka_detail,
    sumka_create,
    sumka_update,
    sumka_delete,
    SumkaApiView,
    SumkaView
)

urlpatterns = [
    # path('', sumka_list, name='sumka-list'),               
    # path('sumkalar/<int:pk>/', sumka_detail, name='sumka-detail'),   
    # path('create/', sumka_create, name='sumka-create'),     
    # path('update/<int:pk>', sumka_update, name='sumka-update'),  
    # path('delete/<int:pk>', sumka_delete, name='sumka-delete'),  

    # path('', SumkaApiView.as_view()),
    # path('sumkalar/<int:pk>/', SumkaApiView.as_view()),
    # path('', SumkaView.as_view()),
    # path('sumkalar/<int:pk>/', SumkaView.as_view()),
]
