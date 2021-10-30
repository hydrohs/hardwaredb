from django.urls import path

from . import views

app_name = 'hardware'
urlpatterns = [
    path('', views.index, name = "index"),
    path('cpus', views.CPUList.as_view(), name="cpus"),
    path('ram', views.RAMList.as_view(), name="ram"),
    path('gpus', views.GPUList.as_view(), name="gpus"),
    path('sound_cards', views.SoundCardList.as_view(), name="soundcards"),
    path('expansion_cards', views.ExpansionCardList.as_view(), name="expansioncards"),
    path('nics', views.NICList.as_view(), name="nics"),
    path('motherboards', views.MotherboardList.as_view(), name="motherboards"),
    path('cases', views.CaseList.as_view(), name="cases"),
    path('peripherals', views.PeripheralList.as_view(), name="peripherals"),
    path('psus', views.PSUList.as_view(), name="psus"),
]