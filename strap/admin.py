from django.contrib import admin

from .models import *


admin.site.register(Karyawan)
admin.site.register(Jenis)
admin.site.register(TempClientSatu)
admin.site.register(TempClientDua)
admin.site.register(TempAkta)
admin.site.register(TempKaryawan)
admin.site.register(DetailClientSatu)
admin.site.register(DetailClientDua)
admin.site.register(DetailKaryawan)

from import_export.admin import ImportExportModelAdmin
@admin.register(Akta)
class AktaAdmin(ImportExportModelAdmin):
    list_display = ("nomor_akta", "tgl_akta", "jenis", "nomor_hak", "desa_tanah","luas_tanah", "luas_bgn","harga_pengalihan", "nop","njop","tgl_ssp","harga_ssp","tgl_sbb","harga_sbb","keterangan")
    pass
    
    
    # Register your models here.
