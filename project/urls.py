from django.urls import path
from .import views

urlpatterns = [
    path('', views.first),
    path('second', views.second,name="second"),
    path('third', views.third,name="third"),
    path('fourth', views.fourth,name="fourth"),
    path('fifth', views.fifth,name="fifth"),
    path('sixth', views.sixth,name="sixth"),
    path('seventh', views.seventh,name="seventh"),
    path('eight', views.eight,name="eight"),
    path('nineth', views.nineth,name="nineth"),
    path('tenth', views.tenth,name="tenth"),
    path('eleventh', views.eleventh,name="eleventh"),
    path('twovelth', views.twovelth,name="twovelth"),
    path('thirteenth',views.thirteenth,name="thirteenth"),
    path('fourteenth', views.fourteenth,name="fourteenth"),
    path('fifteenth', views.fifteenth,name="fifteenth"), 
    path('sixteenth', views.sixteenth,name="sixteenth"),
    path('seventeenth', views.seventeenth,name="seventeenth"),
    path('eighteenth', views.eighteenth,name="eighteenth"),
    path('nineteenth', views.nineteenth,name="nineteenth"),
    path('twentieth', views.twentieth,name="twentieth"),
    path('twentifirst', views.twentifirst,name="twentifirst"),
    path('payment', views.payment, name="payment"),
    path('success', views.success, name="success")
]