from django.contrib import admin
from .models import *

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = "id", "nom", "davlat", 'logo', 'president', "murabbiy", "yil",  "eng_katta_tr", "eng_katta_sotuv"
    list_display_links = 'id', 'nom'
    list_editable = 'president', 'murabbiy', 'eng_katta_tr', 'eng_katta_sotuv'
    list_filter = 'nom', 'davlat',
    list_per_page = 35
    search_fields = 'id', 'nom', 'davlat'

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = "id", "ism", "pozitsiya", 'millat', 'tr_narx', "tug_yil", "club"
    list_display_links = 'id', 'ism'
    list_editable = 'pozitsiya', 'tr_narx'
    list_filter = 'ism', 'tug_yil', 'club'
    list_per_page = 35
    search_fields = 'id', 'ism', 'millat', 'yosh', 'club', 'tr_narx'

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = "id", "player", "eski", 'yangi', 'narx', "tax_narx", "mavsum"
    list_display_links = 'id', 'player'
    # list_editable = ''
    list_filter = ('mavsum',)
    list_per_page = 35
    search_fields = 'id', 'player'

# admin.site.register(Player)
# admin.site.register(Club)
# admin.site.register(Transfer)
admin.site.register(HozirgiMavsum)