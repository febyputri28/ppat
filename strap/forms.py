from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Karyawan, Akta, TempClientSatu,TempClientDua, TempKaryawan


class KaryawanForm(ModelForm):
    class Meta:
        model = Karyawan
        fields= '__all__'
        exclude = ['user', 'profile_pic']

        widgets = {
            'nik_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'nama_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'tempat_lahir_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'tanggal_lahir_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'uraian_tl_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'status_kewarganegaraan_karyawan': forms.Select(attrs={'class': 'form-control'}),
            'prov_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'kab_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'almt_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'rt_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'rw_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'desa_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'kec_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'telp_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'jenkel_karyawan': forms.Select(attrs={'class': 'form-control'}),
            'jabatan': forms.Select(attrs={'class': 'form-control'}),
            
        }
        labels = {
            'nik_karyawan' : 'NIK',
            'nama_karyawan': 'Nama',
            'tempat_lahir_karyawan' : 'Tempat Lahir',
            'tanggal_lahir_karyawan' : 'Tanggal Lahir',
            'uraian_tl_karyawan' : 'Uraian Tanggal Lahir',
            'status_kewarganegaraan_karyawan' : 'Status Kewarganegaraan',
            'prov_karyawan' : 'Provinsi',
            'kab_karyawan' : 'Kabupaten/Kota',
            'almt_karyawan': 'Alamat',
            'rt_karyawan' : 'RT',
            'rw_karyawan' : 'RW',
            'desa_karyawan' : 'Desa/Kelurahan',
            'kec_karyawan' : 'Kecamatan',
            'tlp_karyawan': 'Telepon',
            'jenkel_karyawan': 'Jenis Kelamin',
            'jabatan': 'Jabatan',
        }


class ProfilForm(ModelForm):
    class Meta:
        model = Karyawan
        fields= '__all__'
        exclude = ['user', 'uraian_tl_karyawan']

        widgets = {

            'nik_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'nama_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'tempat_lahir_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'tanggal_lahir_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'status_kewarganegaraan_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'prov_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'kab_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'almt_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'rt_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'rw_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'desa_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'kec_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'telp_karyawan': forms.TextInput(attrs={'class': 'form-control'}),
            'jenkel_karyawan': forms.Select(attrs={'class': 'form-control'}),
            'jabatan': forms.Select(attrs={'class': 'form-control'}),
            
        }
        labels = {
            'nik_karyawan' : 'NIK ',
            'nama_karyawan': 'Nama',
            'tempat_lahir_karyawan' : 'Tempat Lahir',
            'tanggal_lahir_karyawan' : 'Tanggal Lahir',
            'status_kewarganegaraan_karyawan' : 'Status Kewarganegaraan',
            'prov_karyawan' : 'Provinsi',
            'kab_karyawan' : 'Kabupaten/Kota',
            'almt_karyawan': 'Alamat',
            'rt_karyawan' : 'RT',
            'rw_karyawan' : 'RW',
            'desa_karyawan' : 'Desa/Kelurahan',
            'kec_karyawan' : 'Kecamatan',
            'tlp_karyawan': 'Telepon',
            'jenkel_karyawan': 'Jenis Kelamin',
            'jabatan': 'Jabatan',
        }


class AktaForm(ModelForm):
    class Meta:
        model = Akta
        fields= '__all__'
        exclude = ['user','no_transaksi']

        widgets = {
            'nomor_akta': forms.TextInput(attrs={'class': 'form-control'}),
            'tgl_akta': forms.TextInput(attrs={'class': 'form-control'}),
            'jenis': forms.Select(attrs={'class': 'form-control'}),
            'nomor_hak': forms.TextInput(attrs={'class': 'form-control'}),
            'prov_tanah' : forms.TextInput(attrs={'class': 'form-control'}),
            'kab_tanah': forms.TextInput(attrs={'class': 'form-control'}),
            'kec_tanah': forms.TextInput(attrs={'class': 'form-control'}),
            'desa_tanah': forms.TextInput(attrs={'class': 'form-control'}),
            'luas_tanah': forms.TextInput(attrs={'class': 'form-control'}),
            'luas_bgn': forms.TextInput(attrs={'class': 'form-control'}),
            'harga_pengalihan': forms.TextInput(attrs={'class': 'form-control'}),
            'nop': forms.TextInput(attrs={'class': 'form-control'}),
            'njop': forms.TextInput(attrs={'class': 'form-control'}),
            'nib': forms.TextInput(attrs={'class': 'form-control'}),
            'tgl_ssp': forms.TextInput(attrs={'class': 'form-control'}),
            'harga_ssp': forms.TextInput(attrs={'class': 'form-control'}),
            'tgl_sbb': forms.TextInput(attrs={'class': 'form-control'}),
            'harga_sbb': forms.TextInput(attrs={'class': 'form-control'}),
            'keterangan': forms.TextInput(attrs={'class': 'form-control'}),
            'pt': forms.TextInput(attrs={'class': 'form-control'}),
            'jabatan_pt': forms.TextInput(attrs={'class': 'form-control'}),
            'jenis_kuasa': forms.TextInput(attrs={'class': 'form-control'}),
            'keterangan_kuasa': forms.TextInput(attrs={'class': 'form-control'}),
            'jenis_bukti_perjanjian': forms.TextInput(attrs={'class': 'form-control'}),
            'no_bukti_ppat': forms.TextInput(attrs={'class': 'form-control'}),
            'jumlah_perjanjian': forms.TextInput(attrs={'class': 'form-control'}),
            'tanggal_perjanjian': forms.TextInput(attrs={'class': 'form-control'}),
            'no_perjanjian': forms.TextInput(attrs={'class': 'form-control'}),
            'nik_saksi': forms.TextInput(attrs={'class': 'form-control'}),
            'nama_saksi': forms.TextInput(attrs={'class': 'form-control'}),
            'tempat_lahir_saksi': forms.TextInput(attrs={'class': 'form-control'}),
            'tanggal_lahir_saksi': forms.TextInput(attrs={'class': 'form-control'}),
            'uraian_tl_saksi': forms.TextInput(attrs={'class': 'form-control'}),
            'pekerjaan_saksi': forms.TextInput(attrs={'class': 'form-control'}),
            'status_kewarganegaraan_saksi': forms.Select(attrs={'class': 'form-control'}),
            'prov_saksi': forms.TextInput(attrs={'class': 'form-control'}),
            'kab_saksi': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat_saksi': forms.TextInput(attrs={'class': 'form-control'}),
            'rt_saksi': forms.TextInput(attrs={'class': 'form-control'}),
            'rw_saksi': forms.TextInput(attrs={'class': 'form-control'}),
            'desa_saksi': forms.TextInput(attrs={'class': 'form-control'}),
            'kec_saksi': forms.TextInput(attrs={'class': 'form-control'}),
            'status_saksi': forms.TextInput(attrs={'class': 'form-control'}),

            
        }
        labels = {
            'nomor_akta': 'Nomor Akta',
            'tgl_akta': 'Tanggal Akta',
            'jenis': 'Jenis Akta',
            'nomor_hak': 'Nomor Hak',
            'prov_tanah' : 'Provinsi (Letak Aset)',
            'kab_tanah': 'Kabupaten (Letak Aset)',
            'kec_tanah': 'Kecamatan (Letak Aset)',
            'desa_tanah': 'Desa (Letak Aset)',
            'luas_tanah': 'Luas Tanah',
            'luas_bgn': 'Luas Bangunan',
            'harga_pengalihan': 'Harga Pengalihan',
            'nop': 'NOP',
            'njop': 'NJOP',
            'nib': 'NIB',
            'tgl_ssp': 'Tanggal SSP',
            'harga_ssp': 'Harga SSP',
            'tgl_sbb': 'Tanggal SBB',
            'harga_sbb': 'Harga SBB',
            'keterangan': 'Keterangan',
            'pt': 'PT / CV',
            'jabatan_pt': 'Jabatan',
            'jenis_kuasa': 'Jenis Kuasa',
            'keterangan_kuasa': 'Keterangan Kuasa',
            'jenis_bukti_perjanjian': 'Jenis Bukti Perjanjian',
            'no_bukti_ppat': 'Nomor Bukti Perjanjian PPAT',
            'jumlah_perjanjian': 'Jumlah Perjanjian',
            'tanggal_perjanjian': 'Tanggal Perjanjian',
            'no_perjanjian': 'Nomor Perjanjian',
            'nik_saksi': 'NIK Saksi',
            'nama_saksi': 'Nama Saksi',
            'tempat_lahir_saksi': 'Tempat Lahir Saksi',
            'tanggal_lahir_saksi': 'Tanggal Lahir Saksi',
            'uraian_tl_saksi': 'Uraian Tanggal Lahir Saksi',
            'pekerjaan_saksi': 'Pekerjaan Saksi',
            'status_kewarganegaraan_saksi': 'Status Kewarganegaraan Saksi',
            'prov_saksi': 'Provinsi Saksi',
            'kab_saksi': 'Kabupaten Saksi',
            'alamat_saksi': 'Alamat Saksi',
            'rt_saksi': 'RT Saksi',
            'rw_saksi': 'RW Saksi',
            'desa_saksi': 'Desa Saksi',
            'kec_saksi': 'Kecamatan Saksi',
            'status_saksi': 'Status Saksi',
        }


class ClienSatuForm(ModelForm):
    class Meta:
        model = TempClientSatu
        fields= '__all__'

        widgets = {
            'nik_pertama': forms.TextInput(attrs={'class': 'form-control'}),
            'nama_pertama': forms.TextInput(attrs={'class': 'form-control'}),
            'tempat_lahir_pertama': forms.TextInput(attrs={'class': 'form-control'}),
            'tanggal_lahir_pertama': forms.TextInput(attrs={'class': 'form-control'}),
            'pekerjaan_pertama': forms.TextInput(attrs={'class': 'form-control'}),
            'status_kewarganegaraan_pertama': forms.Select(attrs={'class': 'form-control'}),
            'prov_pertama': forms.TextInput(attrs={'class': 'form-control'}),
            'kab_pertama': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat_pertama': forms.TextInput(attrs={'class': 'form-control'}),
            'rt_pertama': forms.TextInput(attrs={'class': 'form-control'}),
            'rw_pertama': forms.TextInput(attrs={'class': 'form-control'}),
            'desa_pertama': forms.TextInput(attrs={'class': 'form-control'}),
            'kec_pertama': forms.TextInput(attrs={'class': 'form-control'}),            
        }
        labels = {
            'nik_pertama': 'NIK',
            'nama_pertama': 'Nama',
            'tempat_lahir_pertama': 'Tempat Lahir',
            'tanggal_lahir_pertama': 'Tanggal Lahir',
            'pekerjaan_pertama': 'Pekerjaan',
            'status_kewarganegaraan_pertama': 'Status Kewarganegaraan',
            'prov_pertama': 'Provinsi',
            'kab_pertama': 'Kabupaten / Kota',
            'alamat_pertama': 'Alamat',
            'rt_pertama': 'RT',
            'rw_pertama': 'RW',
            'desa_pertama': 'Desa / Kelurahan',
            'kec_pertama': 'Kecamatan ',
        }



class ClienDuaForm(ModelForm):
    class Meta:
        model = TempClientDua
        fields= ['nik_kedua', 'nama_kedua', 'tempat_lahir_kedua','tanggal_lahir_kedua','pekerjaan_kedua','status_kewarganegaraan_kedua','prov_kedua','kab_kedua','alamat_kedua','rt_kedua','desa_kedua','kec_kedua']

        widgets = {
            'nik_kedua': forms.TextInput(attrs={'class': 'form-control'}),
            'nama_kedua': forms.TextInput(attrs={'class': 'form-control'}),
            'tempat_lahir_kedua': forms.TextInput(attrs={'class': 'form-control'}),
            'tanggal_lahir_kedua': forms.TextInput(attrs={'class': 'form-control'}),
            'pekerjaan_kedua': forms.TextInput(attrs={'class': 'form-control'}),
            'status_kewarganegaraan_kedua': forms.Select(attrs={'class': 'form-control'}),
            'prov_kedua': forms.TextInput(attrs={'class': 'form-control'}),
            'kab_kedua': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat_kedua': forms.TextInput(attrs={'class': 'form-control'}),
            'rt_kedua': forms.TextInput(attrs={'class': 'form-control'}),
            'rw_kedua': forms.TextInput(attrs={'class': 'form-control'}),
            'desa_kedua': forms.TextInput(attrs={'class': 'form-control'}),
            'kec_kedua': forms.TextInput(attrs={'class': 'form-control'}),            
        }
        labels = {
            'nik_kedua': 'NIK',
            'nama_kedua': 'Nama',
            'tempat_lahir_kedua': 'Tempat Lahir',
            'tanggal_lahir_kedua': 'Tanggal Lahir',
            'pekerjaan_kedua': 'Pekerjaan',
            'status_kewarganegaraan_kedua': 'Status Kewarganegaraan',
            'prov_kedua': 'Provinsi',
            'kab_kedua': 'Kabupaten / Kota',
            'alamat_kedua': 'Alamat',
            'rt_kedua': 'RT',
            'rw_kedua': 'RW',
            'desa_kedua': 'Desa / Kelurahan',
            'kec_kedua': 'Kecamatan ',
        }


class SaksiForm(ModelForm):
    class Meta:
        model = TempKaryawan
        fields= '__all__'
        exclude = ['user']
        widgets = {
            'nik_karyawan': forms.Select(attrs={'class': 'form-control'}),
        }
        labels={
            'nik_karyawan': 'Nama Karyawan',

        }