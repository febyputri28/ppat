from django.db import models
from django.contrib.auth.models import User
from PIL import Image 
# Create your models here.

class Karyawan(models.Model):
    Pilihan=(
        ('PPAT', 'PPAT'),
        ('karyawan PPAT' , 'karyawan PPAT'),
        ('karyawan Notaris' , 'karyawan Notaris'),
    )
    Jenkel=(
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan' , 'Perempuan'),
    )
    Pilih=(
        ('Warga Negara Indonesia', 'Warga Negara Indonesia'),
        ('Warga Negara Asing' , 'Warga Negara Asing'),        
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) 
    nik_karyawan = models.CharField(max_length=50, blank=True, null=True)
    nama_karyawan = models.CharField(max_length=200, blank=True, null=True)
    tempat_lahir_karyawan = models.CharField(max_length=200, blank=True, null=True)
    tanggal_lahir_karyawan = models.CharField(max_length=200, blank=True, null=True)
    uraian_tl_karyawan = models.CharField(max_length=200, blank=True, null=True)
    status_kewarganegaraan_karyawan  = models.CharField(max_length=200, blank=True, null=True, choices=Pilih)
    prov_karyawan = models.CharField(max_length=200, blank=True, null=True)
    kab_karyawan = models.CharField(max_length=200, blank=True, null=True)
    almt_karyawan =  models.CharField(max_length=100, blank=True, null=True)
    rt_karyawan = models.CharField(max_length=50, blank=True, null=True)
    rw_karyawan = models.CharField(max_length=50, blank=True, null=True)
    desa_karyawan = models.CharField(max_length=200, blank=True, null=True)
    kec_karyawan = models.CharField(max_length=200, blank=True, null=True)
    telp_karyawan =  models.CharField(max_length=100, blank=True, null=True)
    jenkel_karyawan =  models.CharField(max_length=100, blank=True, null=True, choices=Jenkel)
    jabatan = models.CharField(max_length=150, blank=True, null=True, choices=Pilihan)
    profile_pic = models.ImageField(default='fotokosong.png', blank=True)
    def __str__(self):
        return '%s' % (self.nama_karyawan)
    class Meta:
        verbose_name_plural ="Karyawan"

    def save(self, *args, **kwargs):
        super(Karyawan, self).save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)


class TempKaryawan(models.Model):
    user =  models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    nik_karyawan = models.ForeignKey(Karyawan, null=True, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"{self.id_karyawan}-{self.id}"
    class Meta:
        verbose_name_plural ="TempKaryawan"

        
class TempClientSatu(models.Model):
    user =  models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    nik_pertama = models.CharField(max_length=50,blank=True, null=True)    
    nama_pertama  = models.CharField(max_length=200, blank=True, null=True)
    tempat_lahir_pertama  = models.CharField(max_length=200, blank=True, null=True)
    tanggal_lahir_pertama  = models.CharField(max_length=200, blank=True, null=True)
    uraian_tl_pertama = models.CharField(max_length=200, blank=True, null=True)
    pekerjaan_pertama  = models.CharField(max_length=200, blank=True, null=True)
    status_kewarganegaraan_pertama  = models.CharField(max_length=200, blank=True, null=True)
    prov_pertama  = models.CharField(max_length=200, blank=True, null=True)
    kab_pertama  = models.CharField(max_length=200, blank=True, null=True)
    alamat_pertama  = models.CharField(max_length=200, blank=True, null=True)
    rt_pertama  = models.CharField(max_length=50, blank=True, null=True)
    rw_pertama  = models.CharField(max_length=50, blank=True, null=True)
    desa_pertama  = models.CharField(max_length=200, blank=True, null=True)
    kec_pertama  = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return f"{self.nama_pertama}-{self.user}-{self.id}"
    class Meta:
        verbose_name_plural ="TempClientSatu"

class TempClientDua(models.Model):   
    user =  models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    nik_kedua = models.CharField(max_length=50,blank=True, null=True)
    nama_kedua  = models.CharField(max_length=200, blank=True, null=True)
    tempat_lahir_kedua  = models.CharField(max_length=200, blank=True, null=True)
    tanggal_lahir_kedua  = models.CharField(max_length=200, blank=True, null=True)
    uraian_tl_kedua = models.CharField(max_length=200, blank=True, null=True)
    pekerjaan_kedua  = models.CharField(max_length=200, blank=True, null=True)
    status_kewarganegaraan_kedua  = models.CharField(max_length=200, blank=True, null=True)
    prov_kedua  = models.CharField(max_length=200, blank=True, null=True)
    kab_kedua  = models.CharField(max_length=200, blank=True, null=True)
    alamat_kedua  = models.CharField(max_length=200, blank=True, null=True)
    rt_kedua = models.CharField(max_length=50, blank=True, null=True)
    rw_kedua  = models.CharField(max_length=50, blank=True, null=True)
    desa_kedua  = models.CharField(max_length=200, blank=True, null=True)
    kec_kedua  = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return f"{self.nama_kedua}-{self.user}-{self.id}"
    class Meta:
        verbose_name_plural ="TempClientDua"


class TempAkta(models.Model):
    Pilihan=(
        ('AJB', 'AJB'),
        ('APHT' , 'APHT'),
        ('SKMHT' , 'SKMHT'),
        ('AH' , 'AH'),
        ('APHB' , 'APHB'),
    )
    user =  models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    nomor_akta = models.CharField(max_length=50, blank=True, null=True)
    tgl_akta =  models.CharField(max_length=50, blank=True, null=True)
    jenis =  models.CharField(max_length=100, blank=True, null=True, choices=Pilihan)
    nomor_hak =  models.CharField(max_length=200, blank=True, null=True)
    prov_tanah =  models.CharField(max_length=200, blank=True, null=True)
    kab_tanah =  models.CharField(max_length=200, blank=True, null=True)
    kec_tanah =  models.CharField(max_length=200, blank=True, null=True)
    desa_tanah =  models.CharField(max_length=200, blank=True, null=True)
    luas_tanah =  models.CharField(max_length=50, blank=True, null=True)
    luas_bgn =  models.CharField(max_length=50, blank=True, null=True)
    harga_pengalihan =  models.CharField(max_length=50, blank=True, null=True)
    nop =  models.CharField(max_length=50, blank=True, null=True)
    njop =  models.CharField(max_length=50, blank=True, null=True)
    nib =  models.CharField(max_length=50, blank=True, null=True)
    tgl_ssp =  models.CharField(max_length=50, blank=True, null=True)
    harga_ssp =  models.CharField(max_length=50, blank=True, null=True)
    tgl_sbb =  models.CharField(max_length=50, blank=True, null=True)
    harga_sbb =  models.CharField(max_length=50, blank=True, null=True)
    keterangan =  models.CharField(max_length=200, blank=True, null=True)
    pt =  models.CharField(max_length=200, blank=True, null=True)
    jabatan_pt =  models.CharField(max_length=200, blank=True, null=True)
    jenis_kuasa =  models.CharField(max_length=200, blank=True, null=True)
    keterangan_kuasa =  models.CharField(max_length=500, blank=True, null=True)
    jenis_bukti_perjanjian =  models.CharField(max_length=200, blank=True, null=True)
    no_bukti_ppat =  models.CharField(max_length=200, blank=True, null=True)
    jumlah_perjanjian =  models.CharField(max_length=200, blank=True, null=True)
    tanggal_perjanjian =  models.CharField(max_length=50, blank=True, null=True)
    no_perjanjian =  models.CharField(max_length=50, blank=True, null=True)
    nik_saksi = models.CharField(max_length=50,blank=True, null=True)    
    nama_saksi  = models.CharField(max_length=200, blank=True, null=True)
    tempat_lahir_saksi  = models.CharField(max_length=200, blank=True, null=True)
    tanggal_lahir_saksi  = models.CharField(max_length=200, blank=True, null=True)
    uraian_tl_saksi = models.CharField(max_length=200, blank=True, null=True)
    pekerjaan_saksi  = models.CharField(max_length=200, blank=True, null=True)
    status_kewarganegaraan_saksi  = models.CharField(max_length=200, blank=True, null=True)
    prov_saksi  = models.CharField(max_length=200, blank=True, null=True)
    kab_saksi  = models.CharField(max_length=200, blank=True, null=True)
    alamat_saksi  = models.CharField(max_length=200, blank=True, null=True)
    rt_saksi  = models.CharField(max_length=50, blank=True, null=True)
    rw_saksi  = models.CharField(max_length=50, blank=True, null=True)
    desa_saksi  = models.CharField(max_length=200, blank=True, null=True)
    kec_saksi  = models.CharField(max_length=200, blank=True, null=True)
    status_saksi  = models.CharField(max_length=200, blank=True, null=True)
   

    def __str__(self):
        return f"{self.nomor_akta}-{self.user}-{self.id}"
    class Meta:
        verbose_name_plural ="TempAkta"





class Akta(models.Model):
    Pilihan=(
        ('AJB', 'AJB'),
        ('APHT' , 'APHT'),
        ('SKMHT' , 'SKMHT'),
        ('AH' , 'AH'),
        ('APHB' , 'APHB'),
    )
    Pilih=(
        ('Warga Negara Indonesia', 'Warga Negara Indonesia'),
        ('Warga Negara Asing' , 'Warga Negara Asing'),        
    )
    user =  models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    no_transaksi = models.BigIntegerField(blank=True, null=True)
    nomor_akta = models.CharField(max_length=50, blank=True, null=True)
    tgl_akta =  models.CharField(max_length=50, blank=True, null=True)
    jenis =  models.CharField(max_length=100, blank=True, null=True, choices=Pilihan)
    nomor_hak =  models.CharField(max_length=200, blank=True, null=True)
    prov_tanah =  models.CharField(max_length=200, blank=True, null=True)
    kab_tanah =  models.CharField(max_length=200, blank=True, null=True)
    kec_tanah =  models.CharField(max_length=200, blank=True, null=True)
    desa_tanah =  models.CharField(max_length=200, blank=True, null=True)
    luas_tanah =  models.CharField(max_length=50, blank=True, null=True)
    luas_bgn =  models.CharField(max_length=50, blank=True, null=True)
    harga_pengalihan =  models.CharField(max_length=50, blank=True, null=True)
    nop =  models.CharField(max_length=50, blank=True, null=True)
    njop =  models.CharField(max_length=50, blank=True, null=True)
    nib =  models.CharField(max_length=50, blank=True, null=True)
    tgl_ssp =  models.CharField(max_length=50, blank=True, null=True)
    harga_ssp =  models.CharField(max_length=50, blank=True, null=True)
    tgl_sbb =  models.CharField(max_length=50, blank=True, null=True)
    harga_sbb =  models.CharField(max_length=50, blank=True, null=True)
    keterangan =  models.CharField(max_length=200, blank=True, null=True)
    pt =  models.CharField(max_length=200, blank=True, null=True)
    jabatan_pt =  models.CharField(max_length=200, blank=True, null=True)
    jenis_kuasa =  models.CharField(max_length=200, blank=True, null=True)
    keterangan_kuasa =  models.CharField(max_length=500, blank=True, null=True)
    jenis_bukti_perjanjian =  models.CharField(max_length=200, blank=True, null=True)
    no_bukti_ppat =  models.CharField(max_length=200, blank=True, null=True)
    jumlah_perjanjian =  models.CharField(max_length=200, blank=True, null=True)
    tanggal_perjanjian =  models.CharField(max_length=50, blank=True, null=True)
    no_perjanjian =  models.CharField(max_length=50, blank=True, null=True)
    nik_saksi = models.CharField(max_length=50,blank=True, null=True)    
    nama_saksi  = models.CharField(max_length=200, blank=True, null=True)
    tempat_lahir_saksi  = models.CharField(max_length=200, blank=True, null=True)
    tanggal_lahir_saksi  = models.CharField(max_length=200, blank=True, null=True)
    uraian_tl_saksi = models.CharField(max_length=200, blank=True, null=True)
    pekerjaan_saksi  = models.CharField(max_length=200, blank=True, null=True)
    status_kewarganegaraan_saksi  = models.CharField(max_length=200, blank=True, null=True,choices=Pilih)
    prov_saksi  = models.CharField(max_length=200, blank=True, null=True)
    kab_saksi  = models.CharField(max_length=200, blank=True, null=True)
    alamat_saksi  = models.CharField(max_length=200, blank=True, null=True)
    rt_saksi  = models.CharField(max_length=50, blank=True, null=True)
    rw_saksi  = models.CharField(max_length=50, blank=True, null=True)
    desa_saksi  = models.CharField(max_length=200, blank=True, null=True)
    kec_saksi  = models.CharField(max_length=200, blank=True, null=True)
    status_saksi  = models.CharField(max_length=200, blank=True, null=True)

    def get_akta(self):
        return DetailClientSatu.objects.filter(no_transaksi=self.no_transaksi)
    
    def get_akta2(self):
        return DetailClientDua.objects.filter(no_transaksi=self.no_transaksi)

    def get_akta3(self):
        return DetailKaryawan.objects.filter(no_transaksi=self.no_transaksi)

    def __str__(self):
        return f"{self.nomor_akta}-{self.user}-{self.no_transaksi}"
    class Meta:
        verbose_name_plural ="Data Akta"

class DetailClientSatu(models.Model):
    Pilih=(
        ('Warga Negara Indonesia', 'Warga Negara Indonesia'),
        ('Warga Negara Asing' , 'Warga Negara Asing'),        
    )
    user =  models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    no_transaksi = models.BigIntegerField(blank=True, null=True)
    nik_pertama = models.CharField(max_length=50,blank=True, null=True) 
    nama_pertama  = models.CharField(max_length=200, blank=True, null=True)
    tempat_lahir_pertama  = models.CharField(max_length=200, blank=True, null=True)
    tanggal_lahir_pertama  = models.CharField(max_length=200, blank=True, null=True)
    uraian_tl_pertama = models.CharField(max_length=200, blank=True, null=True)
    pekerjaan_pertama  = models.CharField(max_length=200, blank=True, null=True)
    status_kewarganegaraan_pertama  = models.CharField(max_length=200, blank=True, null=True, choices=Pilih)
    prov_pertama  = models.CharField(max_length=200, blank=True, null=True)
    kab_pertama  = models.CharField(max_length=200, blank=True, null=True)
    alamat_pertama  = models.CharField(max_length=200, blank=True, null=True)
    rt_pertama  = models.CharField(max_length=200, blank=True, null=True)
    rw_pertama  = models.CharField(max_length=200, blank=True, null=True)
    desa_pertama  = models.CharField(max_length=200, blank=True, null=True)
    kec_pertama  = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return f"{self.nama_pertama}-{self.user}-{self.no_transaksi}"
    class Meta:
        verbose_name_plural ="DetailClientSatu"



class DetailClientDua(models.Model):
    Pilih=(
        ('Warga Negara Indonesia', 'Warga Negara Indonesia'),
        ('Warga Negara Asing' , 'Warga Negara Asing'),        
    )
    user =  models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    no_transaksi = models.BigIntegerField(blank=True, null=True)
    nik_kedua = models.CharField(max_length=50,blank=True, null=True)
    nama_kedua  = models.CharField(max_length=200, blank=True, null=True)
    tempat_lahir_kedua  = models.CharField(max_length=200, blank=True, null=True)
    tanggal_lahir_kedua  = models.CharField(max_length=200, blank=True, null=True)
    uraian_tl_kedua = models.CharField(max_length=200, blank=True, null=True)
    pekerjaan_kedua  = models.CharField(max_length=200, blank=True, null=True)
    status_kewarganegaraan_kedua  = models.CharField(max_length=200, blank=True, null=True, choices=Pilih)
    prov_kedua  = models.CharField(max_length=200, blank=True, null=True)
    kab_kedua  = models.CharField(max_length=200, blank=True, null=True)
    alamat_kedua  = models.CharField(max_length=200, blank=True, null=True)
    rt_kedua = models.CharField(max_length=50, blank=True, null=True)
    rw_kedua  = models.CharField(max_length=50, blank=True, null=True)
    desa_kedua  = models.CharField(max_length=200, blank=True, null=True)
    kec_kedua  = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return f"{self.nama_kedua}-{self.user}-{self.no_transaksi}"
    class Meta:
        verbose_name_plural ="DetailClientDua"


class DetailKaryawan(models.Model):
    
    no_transaksi = models.BigIntegerField(blank=True, null=True)
    user =  models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    nik_karyawan = models.ForeignKey(Karyawan, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nik_karyawan}-{self.user}-{self.no_transaksi}"
    class Meta:
        verbose_name_plural ="DetailKaryawan"



class Jenis(models.Model):
    id_jenis = models.CharField(max_length=50)
    jenis = models.CharField(max_length=100)
    keterangan_jenis =  models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.jenis)
    class Meta:
        verbose_name_plural ="Jenis Akta"


