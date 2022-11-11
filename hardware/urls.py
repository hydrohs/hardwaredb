from django.urls import path

from .views import *

app_name = 'hardware'
urlpatterns = [
    path('', index, name = "index"),
    path('cpus/<int:pk>', CPUDetailView.as_view(), name="cpu_detail"),
    path('cpus/all', CPUList.as_view(), name="cpus_all"),
    path('ram/all', RAMList.as_view(), name="ram_all"),
    path('gpus/all', GPUList.as_view(), name="gpus_all"),
    path('gpus/<int:pk>', GPUDetailView.as_view(), name="gpu_detail"),
    path('sound_cards/all', SoundCardList.as_view(), name="soundcards_all"),
    path('sound_cards/<int:pk>', SoundCardDetailView.as_view(), name="soundcard_detail"),
    path('expansion_cards/all', ExpansionCardList.as_view(), name="expansioncards_all"),
    path('expansion_cards/<int:pk>', ExpansionCardDetailView.as_view(), name="expansioncards_detail"),
    path('nics/all', NICList.as_view(), name="nics_all"),
    path('nics/<int:pk>', NICDetailView.as_view(), name="nic_detail"),
    path('motherboards/all', MotherboardList.as_view(), name="motherboards_all"),
    path('cases/all', CaseList.as_view(), name="cases_all"),
    path('peripherals/all', PeripheralList.as_view(), name="peripherals_all"),
    path('psus/all', PSUList.as_view(), name="psus_all"),
    path('cables/all', CableList.as_view(), name="cables_all"),
]