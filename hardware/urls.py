from django.urls import path

from . import views

app_name = 'hardware'
urlpatterns = [
    path('', views.index, name = "index"),
    path('cpus/<int:pk>', views.CPUDetailView.as_view(), name="cpu_detail"),
    path('cpus/all', views.CPUList.as_view(), name="cpus_all"),
    path('ram/all', views.RAMList.as_view(), name="ram_all"),
    path('gpus/all', views.GPUList.as_view(), name="gpus_all"),
    path('sound_cards/all', views.SoundCardList.as_view(), name="soundcards_all"),
    path('expansion_cards/all', views.ExpansionCardList.as_view(), name="expansioncards_all"),
    path('nics/all', views.NICList.as_view(), name="nics_all"),
    path('motherboards/all', views.MotherboardList.as_view(), name="motherboards_all"),
    path('cases/all', views.CaseList.as_view(), name="cases_all"),
    path('peripherals/all', views.PeripheralList.as_view(), name="peripherals_all"),
    path('psus/all', views.PSUList.as_view(), name="psus_all"),
    path('cables/all', views.CableList.as_view(), name="cables_all"),
]