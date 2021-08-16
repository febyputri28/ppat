import django_filters
from django_filters import CharFilter
from .models import *


class AktaFilter(django_filters.FilterSet):

    class Meta:
        model = Akta
        fields = ['nomor_akta']
        # fields ='__all__'
        # exclude = ['no_urut','tgl_akta','jenis', 'nomor_hak', 'almt_aset', 'luas_tanah', 'luas_bgn','harga_pengalihan',
        # 'nop', 'njop', 'tgl_ssp', 'harga_ssp', 'tgl_sbb', 'harga_sbb', 'keterangan']
