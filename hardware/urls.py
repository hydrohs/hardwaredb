from django.urls import path

from .views import *

app_name = 'hardware'
urlpatterns = [
    path('', index, name = "index"),
    path('cpus/all', CPUList.as_view(), name="cpus_all"),
    path('cpus/<int:pk>', CPUDetail.as_view(), name="cpu_detail"),
    path('ram/all', RAMList.as_view(), name="ram_all"),
    path('gpus/all', GPUList.as_view(), name="gpus_all"),
    path('gpus/<int:pk>', GPUDetail.as_view(), name="gpu_detail"),
    path('sound_cards/all', SoundCardList.as_view(), name="soundcards_all"),
    path('sound_cards/<int:pk>', SoundCardDetail.as_view(), name="soundcard_detail"),
    path('expansion_cards/all', ExpansionCardList.as_view(), name="expansioncards_all"),
    path('expansion_cards/<int:pk>', ExpansionCardDetail.as_view(), name="expansioncard_detail"),
    path('nics/all', NICList.as_view(), name="nics_all"),
    path('nics/<int:pk>', NICDetail.as_view(), name="nic_detail"),
    path('motherboards/all', MotherboardList.as_view(), name="motherboards_all"),
    path('motherboards/<int:pk>', MotherboardDetail.as_view(), name="motherboard_detail"),
    path('psus/all', PSUList.as_view(), name="psus_all"),
    path('psus/<int:pk>', PSUDetail.as_view(), name="psu_detail"),
    path('drives/all', DriveList.as_view(), name="drives_all"),
    path('drives/<int:pk>', DriveDetail.as_view(), name="drive_detail"),
    path('cases/all', CaseList.as_view(), name="cases_all"),
    path('cases/<int:pk>', CaseDetail.as_view(), name="case_detail"),
    path('systems/<int:pk>', SystemDetail.as_view(), name="system_detail"),
    path('peripherals/all', PeripheralList.as_view(), name="peripherals_all"),
    path('peripherals/<int:pk>', PeripheralDetail.as_view(), name="peripheral_detail"),
    path('cables/all', CableList.as_view(), name="cables_all"),
    path('cables/<int:pk>', CableDetail.as_view(), name="cable_detail")
]