from import_export import resources
from .models import Akta

class AktaResources(resources.ModelResource):
    class Meta:
        model = Akta
        fields= ['nomor_akta', 'tgl_akta', 'jenis', 'nomor_hak', 'desa_tanah','luas_tanah','luas_bgn','harga_pengalihan', 'nop','njop','tgl_ssp','harga_ssp','tgl_sbb','harga_sbb','keterangan']
    
