from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.core import serializers
from .resources import AktaResources
from django.contrib.auth.decorators import login_required
from .decorators import tolakhalaman_ini
from django.http import HttpResponse, JsonResponse
from django.views import View
from .forms import *
from django.contrib import messages
from .models import *
from .filters import AktaFilter
from django.contrib.auth.models import Group
from xhtml2pdf import pisa
from django.template.loader import get_template

# Create your views here. 
@login_required(login_url='login')
def home(request):  
    akta = Akta.objects.order_by('-id')
    ajb = akta.filter(jenis = 'AJB').count()
    apht = akta.filter(jenis = 'APHT').count()
    skmht = akta.filter(jenis = 'SKMHT').count()
    ah = akta.filter(jenis = 'AH').count()
    aphb = akta.filter(jenis = 'APHB').count()
    context = {
        'menu' : 'Beranda',
        'page' : 'selamat datang di Notaris dan PPAT',
        'data_ajb' : ajb, 
        'data_apht' : apht, 
        'data_skmht' : skmht, 
        'data_ah' : ah, 
        'data_aphb' : aphb,       
    }
    return render(request, 'strap/home.html', context)

@login_required(login_url='login')
def aktamasuk(request):     
    list_akta = Akta.objects.order_by('-id')
    list_clientsatu = DetailClientSatu.objects.filter(no_transaksi='1')
    filter_akta = AktaFilter(request.GET, queryset=list_akta)
    list_akta = filter_akta.qs

    halaman_tampil = Paginator(list_akta, 5)     
    halaman_url = request.GET.get('halaman',1)     
    halaman_akta = halaman_tampil.get_page(halaman_url)

    if halaman_akta.has_previous():         
        url_previous = f'?halaman={halaman_akta.previous_page_number()}'     
    else:         
        url_previous = '' 
 
    if halaman_akta.has_next():         
        url_next = f'?halaman={halaman_akta.next_page_number()}'     
    else:         
        url_next = '' 
    context = {
        'menu' : 'Akta Masuk',
        'page' : 'halaman akta masuk',   
        'aktamasuk' : list_akta,
        'clientsatu' : list_clientsatu,
        'filter_akta' : filter_akta, 
        'page_akta':halaman_akta, 
        'previous' : url_previous,         
        'next' : url_next  
    }
    return render(request, 'strap/aktamasuk.html', context)

@login_required(login_url='login')
def delete_akta(request, pk):
    hapusakta = Akta.objects.get(id=pk)
    if request.method == 'POST':
        hapusakta.delete()
        return redirect('/aktamasuk')
    context = {
        'menu' : 'Hapus Akta',
        'page' : 'Hapus', 
        'dataaktadelete' : hapusakta,
        }
    return render(request, 'strap/delete_akta.html', context)

@login_required(login_url='login')
def updateAkta(request, pk):
    up_akta = Akta.objects.get(id=pk)
    formakta = AktaForm(instance=up_akta)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = AktaForm(request.POST, instance=up_akta)
        if formedit.is_valid:
            formedit.save()
            return redirect('karyawan')
    context = {
        'menu' : 'Update Akta',
        'page' : 'Edit Akta', 
        'formakta' : formakta,
        }
    return render(request, 'strap/update_akta.html', context)

@login_required(login_url='login')
def karyawan(request):
    list_karyawan = Karyawan.objects.all()  
    context = {
        'menu' : 'Karyawan',
        'page' : 'halaman karyawan',
        'karyawan' : list_karyawan    
          
    }
    return render(request, 'strap/karyawan.html', context)

@login_required(login_url='login')
def jenis(request):   
    list_jenis = Jenis.objects.all()  
    context = {
        'menu' : 'Halaman Jenis Akta',
        'page' : 'jenis',  
        'jenis' : list_jenis,      
    }
    return render(request, 'strap/jenis.html', context)

@login_required(login_url='login')
def buatakta(request): 
    no = Akta.objects.all().count()
    
    notransaksi =1 + int(no)
    context = {
        'menu' : 'Halaman Buat Akta',
        'page' : 'buat akta',
        'notransaksi':notransaksi
  
    }
    return render(request, 'strap/buatakta.html', context)

@login_required(login_url='login')
def tampilform(request):
    formk = SaksiForm()
    context = {
        'judul': 'Halaman Beranda',
        'formsaksi':formk
  
    }
    return render (request, 'strap/formsaksi.html', context)

@login_required(login_url='login')
def SimpanFormK(request):
    if request.is_ajax and request.method == "POST":
        formk = SaksiForm(request.POST)
        if formk.is_valid():
            instance = formk.save()
            ser_instance = serializers.serialize('json',[instance,])
            return JsonResponse({"instance":ser_instance}, status=200)
        else:
            return JsonResponse({"error":formk.errors}, status=400)
    return JsonResponse({"error":""}, status=400)


@login_required(login_url='login')
def simpanclientpertama(request):
    if request.method == 'POST':
        user = request.user
        nik_pertama = request.POST.get('nik_pertama')
        nama_pertama = request.POST.get('nama_pertama')
        tempat_lahir_pertama = request.POST.get('tempat_lahir_pertama')
        tanggal_lahir_pertama = request.POST.get('tanggal_lahir_pertama')
        uraian_tl_pertama = request.POST.get('uraian_tl_pertama')
        pekerjaan_pertama = request.POST.get('pekerjaan_pertama')
        status_kewarganegaraan_pertama = request.POST.get('status_kewarganegaraan_pertama')
        prov_pertama = request.POST.get('prov_pertama')
        kab_pertama = request.POST.get('kab_pertama')
        alamat_pertama = request.POST.get('alamat_pertama')
        rt_pertama = request.POST.get('rt_pertama')
        rw_pertama = request.POST.get('rw_pertama')
        desa_pertama = request.POST.get('desa_pertama')
        kec_pertama = request.POST.get('kec_pertama')

        cek_temp = TempClientSatu.objects.filter(user=user, nik_pertama = nik_pertama, nama_pertama=nama_pertama, tempat_lahir_pertama=tempat_lahir_pertama, tanggal_lahir_pertama=tanggal_lahir_pertama,uraian_tl_pertama=uraian_tl_pertama, pekerjaan_pertama=pekerjaan_pertama, status_kewarganegaraan_pertama=status_kewarganegaraan_pertama, prov_pertama=prov_pertama, kab_pertama=kab_pertama, alamat_pertama=alamat_pertama, rt_pertama=rt_pertama, rw_pertama=rw_pertama, desa_pertama=desa_pertama, kec_pertama=kec_pertama).count()
        if cek_temp > 0:
            temp = TempClientSatu.objects.get(user = user, nik_pertama = nik_pertama, nama_pertama=nama_pertama, tempat_lahir_pertama=tempat_lahir_pertama, tanggal_lahir_pertama=tanggal_lahir_pertama,uraian_tl_pertama=uraian_tl_pertama, pekerjaan_pertama=pekerjaan_pertama, status_kewarganegaraan_pertama=status_kewarganegaraan_pertama, prov_pertama=prov_pertama, kab_pertama=kab_pertama, alamat_pertama=alamat_pertama, rt_pertama=rt_pertama, rw_pertama=rw_pertama, desa_pertama=desa_pertama, kec_pertama=kec_pertama)
            temp.save()
            
        else:
            simpan = TempClientSatu.objects.create(user = user, nik_pertama = nik_pertama, nama_pertama=nama_pertama, tempat_lahir_pertama=tempat_lahir_pertama, tanggal_lahir_pertama=tanggal_lahir_pertama,uraian_tl_pertama=uraian_tl_pertama, pekerjaan_pertama=pekerjaan_pertama, status_kewarganegaraan_pertama=status_kewarganegaraan_pertama, prov_pertama=prov_pertama, kab_pertama=kab_pertama, alamat_pertama=alamat_pertama, rt_pertama=rt_pertama, rw_pertama=rw_pertama, desa_pertama=desa_pertama, kec_pertama=kec_pertama)
            simpan.save()
    return JsonResponse({'status': 0 })

@login_required(login_url='login')
def simpanclientkedua(request):
    if request.method == 'POST':
        user = request.user
        nik_kedua = request.POST.get('nik_kedua')
        nama_kedua = request.POST.get('nama_kedua')
        tempat_lahir_kedua = request.POST.get('tempat_lahir_kedua')
        tanggal_lahir_kedua = request.POST.get('tanggal_lahir_kedua')
        uraian_tl_kedua = request.POST.get('uraian_tl_kedua')
        pekerjaan_kedua = request.POST.get('pekerjaan_kedua')
        status_kewarganegaraan_kedua = request.POST.get('status_kewarganegaraan_kedua')
        prov_kedua = request.POST.get('prov_kedua')
        kab_kedua = request.POST.get('kab_kedua')
        alamat_kedua = request.POST.get('alamat_kedua')
        rt_kedua = request.POST.get('rt_kedua')
        rw_kedua = request.POST.get('rw_kedua')
        desa_kedua = request.POST.get('desa_kedua')
        kec_kedua = request.POST.get('kec_kedua')

        cek_temp = TempClientDua.objects.filter(user=user, nik_kedua = nik_kedua, nama_kedua=nama_kedua, tempat_lahir_kedua=tempat_lahir_kedua, tanggal_lahir_kedua=tanggal_lahir_kedua,uraian_tl_kedua=uraian_tl_kedua, pekerjaan_kedua=pekerjaan_kedua, status_kewarganegaraan_kedua=status_kewarganegaraan_kedua, prov_kedua=prov_kedua, kab_kedua=kab_kedua, alamat_kedua=alamat_kedua, rt_kedua=rt_kedua, rw_kedua=rw_kedua, desa_kedua=desa_kedua, kec_kedua=kec_kedua).count()
        if cek_temp > 0:
            temp = TempClientDua.objects.get(user = user, nik_kedua = nik_kedua, nama_kedua=nama_kedua, tempat_lahir_kedua=tempat_lahir_kedua, tanggal_lahir_kedua=tanggal_lahir_kedua,uraian_tl_kedua=uraian_tl_kedua, pekerjaan_kedua=pekerjaan_kedua, status_kewarganegaraan_kedua=status_kewarganegaraan_kedua, prov_kedua=prov_kedua, kab_kedua=kab_kedua, alamat_kedua=alamat_kedua, rt_kedua=rt_kedua, rw_kedua=rw_kedua, desa_kedua=desa_kedua, kec_kedua=kec_kedua)
            temp.save()
            
        else:
            simpan = TempClientDua.objects.create(user = user, nik_kedua = nik_kedua, nama_kedua=nama_kedua, tempat_lahir_kedua=tempat_lahir_kedua, tanggal_lahir_kedua=tanggal_lahir_kedua,uraian_tl_kedua=uraian_tl_kedua, pekerjaan_kedua=pekerjaan_kedua, status_kewarganegaraan_kedua=status_kewarganegaraan_kedua, prov_kedua=prov_kedua, kab_kedua=kab_kedua, alamat_kedua=alamat_kedua, rt_kedua=rt_kedua, rw_kedua=rw_kedua, desa_kedua=desa_kedua, kec_kedua=kec_kedua)
            simpan.save()

    return JsonResponse({'status': 0 })

@login_required(login_url='login')
def simpanketerangan(request):
    if request.method == 'POST':
        user = request.user        
        nomor_akta = request.POST.get('nomor_akta')
        tgl_akta = request.POST.get('tgl_akta')
        jenis = request.POST.get('jenis')
        nomor_hak = request.POST.get('nomor_hak')
        prov_tanah = request.POST.get('prov_tanah')
        kab_tanah = request.POST.get('kab_tanah')
        kec_tanah = request.POST.get('kec_tanah')
        desa_tanah = request.POST.get('desa_tanah')
        luas_tanah = request.POST.get('luas_tanah')
        luas_bgn = request.POST.get('luas_bgn')
        harga_pengalihan = request.POST.get('harga_pengalihan')
        nop = request.POST.get('nop')
        njop = request.POST.get('njop')
        nib = request.POST.get('nib')
        tgl_ssp = request.POST.get('tgl_ssp')
        harga_ssp = request.POST.get('harga_ssp')
        tgl_sbb = request.POST.get('tgl_sbb')
        harga_sbb = request.POST.get('harga_sbb')
        keterangan = request.POST.get('keterangan')
        pt = request.POST.get('pt')
        jabatan_pt = request.POST.get('jabatan_pt')
        jenis_kuasa = request.POST.get('jenis_kuasa')
        keterangan_kuasa = request.POST.get('keterangan_kuasa')
        jenis_bukti_perjanjian = request.POST.get('jenis_bukti_perjanjian')
        no_bukti_ppat = request.POST.get('no_bukti_ppat')       
        jumlah_perjanjian = request.POST.get('jumlah_perjanjian')
        tanggal_perjanjian = request.POST.get('tanggal_perjanjian')
        no_perjanjian = request.POST.get('no_perjanjian')
        nik_saksi = request.POST.get('nik_saksi')
        nama_saksi = request.POST.get('nama_saksi')
        tempat_lahir_saksi = request.POST.get('tempat_lahir_saksi')
        tanggal_lahir_saksi = request.POST.get('tanggal_lahir_saksi')
        uraian_tl_saksi = request.POST.get('uraian_tl_saksi')       
        pekerjaan_saksi = request.POST.get('pekerjaan_saksi')
        status_kewarganegaraan_saksi = request.POST.get('status_kewarganegaraan_saksi')
        prov_saksi = request.POST.get('prov_saksi')
        kab_saksi = request.POST.get('kab_saksi')
        alamat_saksi = request.POST.get('alamat_saksi')
        rt_saksi = request.POST.get('rt_saksi')
        rw_saksi = request.POST.get('rw_saksi')
        desa_saksi = request.POST.get('desa_saksi')
        kec_saksi = request.POST.get('kec_saksi')
        status_saksi = request.POST.get('status_saksi')
        
        simpan = TempAkta.objects.create(
            user=user, 
            nomor_akta=nomor_akta, 
            tgl_akta=tgl_akta, 
            jenis=jenis, 
            nomor_hak=nomor_hak, 
            prov_tanah=prov_tanah, 
            kab_tanah=kab_tanah, 
            kec_tanah=kec_tanah, 
            desa_tanah=desa_tanah, 
            luas_tanah=luas_tanah, 
            luas_bgn=luas_bgn, 
            harga_pengalihan=harga_pengalihan, 
            nop=nop, 
            njop=njop, 
            nib=nib,
            tgl_ssp=tgl_ssp, 
            harga_ssp=harga_ssp,
            tgl_sbb=tgl_sbb,
            harga_sbb=harga_sbb,
            keterangan=keterangan, 
            pt=pt, 
            jabatan_pt=jabatan_pt, 
            jenis_kuasa=jenis_kuasa, 
            keterangan_kuasa=keterangan_kuasa, 
            jenis_bukti_perjanjian=jenis_bukti_perjanjian, 
            no_bukti_ppat = no_bukti_ppat,
            jumlah_perjanjian=jumlah_perjanjian, 
            tanggal_perjanjian=tanggal_perjanjian,
            no_perjanjian=no_perjanjian, 
            nik_saksi=nik_saksi, 
            nama_saksi=nama_saksi, 
            tempat_lahir_saksi=tempat_lahir_saksi, 
            tanggal_lahir_saksi=tanggal_lahir_saksi, 
            uraian_tl_saksi=uraian_tl_saksi,
            pekerjaan_saksi=pekerjaan_saksi, 
            status_kewarganegaraan_saksi=status_kewarganegaraan_saksi, 
            prov_saksi=prov_saksi, 
            kab_saksi=kab_saksi, 
            alamat_saksi=alamat_saksi, 
            rt_saksi=rt_saksi, 
            rw_saksi=rw_saksi, 
            desa_saksi=desa_saksi, 
            kec_saksi=kec_saksi,
            status_saksi=status_saksi)
        simpan.save()

    return JsonResponse({'status': 0 })

@login_required(login_url='login')
def hapusclientsatu(request):
    if request.method == "POST":
        id = request.POST.get('id')       
        nik_pertama = request.POST.get('nik_pertama')
        nama_pertama = request.POST.get('nama_pertama')
        tempat_lahir_pertama = request.POST.get('tempat_lahir_pertama')
        tanggal_lahir_pertama = request.POST.get('tanggal_lahir_pertama')
        pekerjaan_pertama = request.POST.get('pekerjaan_pertama')
        status_kewarganegaraan_pertama = request.POST.get('status_kewarganegaraan_pertama')
        prov_pertama = request.POST.get('prov_pertama')
        kab_pertama = request.POST.get('kab_pertama')
        alamat_pertama = request.POST.get('alamat_pertama')
        rt_pertama = request.POST.get('rt_pertama')
        rw_pertama = request.POST.get('rw_pertama')
        desa_pertama = request.POST.get('desa_pertama')
        kec_pertama = request.POST.get('kec_pertama')
        
        temp = TempClientSatu.objects.get(pk=id)
        temp.delete()

        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


@login_required(login_url='login')
def hapusclientkedua(request):
    if request.method == "POST":
        id = request.POST.get('id')       
        nik_kedua = request.POST.get('nik_kedua')
        nama_kedua = request.POST.get('nama_kedua')
        tempat_lahir_kedua = request.POST.get('tempat_lahir_kedua')
        tanggal_lahir_kedua = request.POST.get('tanggal_lahir_kedua')
        pekerjaan_kedua = request.POST.get('pekerjaan_kedua')
        status_kewarganegaraan_kedua = request.POST.get('status_kewarganegaraan_kedua')
        prov_kedua = request.POST.get('prov_kedua')
        kab_kedua = request.POST.get('kab_kedua')
        alamat_kedua = request.POST.get('alamat_kedua')
        rt_kedua = request.POST.get('rt_kedua')
        rw_kedua = request.POST.get('rw_kedua')
        desa_kedua = request.POST.get('desa_kedua')
        kec_kedua = request.POST.get('kec_kedua')
        
        temp = TempClientDua.objects.get(pk=id)
        temp.delete()

        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


@login_required(login_url='login')
def hapuskaryawan(request):
    if request.method == "POST":
        id = request.POST.get('id')       
        id_karyawan = request.POST.get('id_karyawan')
        
        temp = TempKaryawan.objects.get(pk=id)
        temp.delete()

        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})



@login_required(login_url='login')
def simpantransaksi(request):
    if request.method == 'POST':
        no_transaksi = request.POST.get('no_transaksi')
        user = request.user
        trans = TempAkta.objects.order_by('-id').filter(user=request.user)
        for i in trans:
            instance_trans = Akta(
                no_transaksi = no_transaksi,
                user = user,
                nomor_akta= i.nomor_akta, 
                tgl_akta=i.tgl_akta, 
                jenis=i.jenis, 
                nomor_hak=i.nomor_hak, 
                prov_tanah=i.prov_tanah, 
                kab_tanah=i.kab_tanah, 
                kec_tanah=i.kec_tanah, 
                desa_tanah=i.desa_tanah, 
                luas_tanah=i.luas_tanah, 
                luas_bgn=i.luas_bgn, 
                harga_pengalihan=i.harga_pengalihan, 
                nop=i.nop, 
                njop=i.njop,
                nib=i.nib, 
                tgl_ssp=i.tgl_ssp, 
                harga_ssp=i.harga_ssp,
                tgl_sbb=i.tgl_sbb,
                harga_sbb=i.harga_sbb,
                keterangan=i.keterangan, 
                pt=i.pt, 
                jabatan_pt=i.jabatan_pt, 
                jenis_kuasa=i.jenis_kuasa, 
                keterangan_kuasa=i.keterangan_kuasa, 
                jenis_bukti_perjanjian=i.jenis_bukti_perjanjian, 
                no_bukti_ppat=i.no_bukti_ppat,
                jumlah_perjanjian=i.jumlah_perjanjian, 
                tanggal_perjanjian=i.tanggal_perjanjian,
                no_perjanjian=i.no_perjanjian, 
                nik_saksi=i.nik_saksi, 
                nama_saksi=i.nama_saksi, 
                tempat_lahir_saksi=i.tempat_lahir_saksi, 
                tanggal_lahir_saksi=i.tanggal_lahir_saksi, 
                uraian_tl_saksi=i.uraian_tl_saksi,
                pekerjaan_saksi=i.pekerjaan_saksi, 
                status_kewarganegaraan_saksi=i.status_kewarganegaraan_saksi, 
                prov_saksi=i.prov_saksi, 
                kab_saksi=i.kab_saksi, 
                alamat_saksi=i.alamat_saksi, 
                rt_saksi=i.rt_saksi, 
                rw_saksi=i.rw_saksi, 
                desa_saksi=i.desa_saksi, 
                kec_saksi=i.kec_saksi,
                status_saksi=i.status_saksi
            )
            instance_trans.save()
        trans.delete()

        temp = TempClientSatu.objects.order_by('-id').filter(user=request.user)
        for r in temp:
            instance_detail= DetailClientSatu(
                no_transaksi = no_transaksi,
                user = request.user,
                nik_pertama = r.nik_pertama, 
                nama_pertama= r.nama_pertama, 
                tempat_lahir_pertama= r.tempat_lahir_pertama, 
                tanggal_lahir_pertama= r.tanggal_lahir_pertama, 
                uraian_tl_pertama = r.uraian_tl_pertama,
                pekerjaan_pertama= r.pekerjaan_pertama, 
                status_kewarganegaraan_pertama= r.status_kewarganegaraan_pertama, 
                prov_pertama= r.prov_pertama, 
                kab_pertama= r.kab_pertama, 
                alamat_pertama= r.alamat_pertama, 
                rt_pertama= r.rt_pertama, 
                rw_pertama=r.rw_pertama, 
                desa_pertama=r.desa_pertama, 
                kec_pertama=r.kec_pertama

            )
            instance_detail.save()
        temp.delete()

        tempdua = TempClientDua.objects.order_by('-id').filter(user=request.user)
        for a in tempdua:
            instance_detaildua= DetailClientDua(
                no_transaksi = no_transaksi,
                user = request.user,
                nik_kedua = a.nik_kedua, 
                nama_kedua= a.nama_kedua, 
                tempat_lahir_kedua= a.tempat_lahir_kedua, 
                tanggal_lahir_kedua= a.tanggal_lahir_kedua, 
                uraian_tl_kedua =a.uraian_tl_kedua,
                pekerjaan_kedua= a.pekerjaan_kedua, 
                status_kewarganegaraan_kedua= a.status_kewarganegaraan_kedua, 
                prov_kedua= a.prov_kedua, 
                kab_kedua= a.kab_kedua, 
                alamat_kedua= a.alamat_kedua, 
                rt_kedua= a.rt_kedua, 
                rw_kedua=a.rw_kedua, 
                desa_kedua=a.desa_kedua, 
                kec_kedua=a.kec_kedua

            )
            instance_detaildua.save()
        tempdua.delete()

        tempk = TempKaryawan.objects.order_by('id')
        for b in tempk:
            instance_karyawan = DetailKaryawan(
                no_transaksi = no_transaksi,
                user = request.user,
                nik_karyawan = b.nik_karyawan
            )
            instance_karyawan.save()
        tempk.delete()
       
        return JsonResponse({'status': 0 })
    else:
        return JsonResponse({'status': 0 })



@login_required(login_url='login')
def TampilClientSatu(request):
    temp = TempClientSatu.objects.order_by('-id').filter(user=request.user)
    context = {
        'temp' : temp,
    }
    return render(request, 'strap/tampil_js/tampilclientsatujs.html', context)

@login_required(login_url='login')
def TampilClientDua(request):
    tempdua = TempClientDua.objects.order_by('-id').filter(user=request.user)
    context = {
        'tempdua' : tempdua,
    }
    return render(request, 'strap/tampil_js/tampilclientduajs.html', context)

@login_required(login_url='login')
def TampilKaryawan(request):
    temp = TempKaryawan.objects.order_by('-id')
    context = {
        'temp' : temp,
    }
    return render(request, 'strap/tampil_js/tampilkaryawanjs.html', context)


@login_required(login_url='login')
def Tambahkaryawan(request): 
    form = KaryawanForm()
    formkaryawan = KaryawanForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

    

        if User.objects.filter(username = username).first():
            messages.success(request, 'Username sudah ada.')
            return redirect('formkaryawan')

        if password1 != password2:
            messages.success(request, 'Password Tidak sama')
            return redirect('formkaryawan')
        # user
        user = User.objects.create_user(username=username)
        user.set_password(password1)
        user.is_active = True
        user.save()
        # user


        # Group
        strap_karyawan = Group.objects.get(name='karyawan')
        user.groups.add(strap_karyawan)
        # Group

        # Karyawan
        formsimpankaryawan = formkaryawan.save()
        formsimpankaryawan.user = user
        formsimpankaryawan.save()  
    context = {
        'menu' : 'Form Karyawan',
        'page' : 'form karyawan',  
        'form' : form,      
    }
    return render(request, 'strap/tambah_karyawan.html', context)

@login_required(login_url='login')
def updateKaryawan(request, pk):
    up_karyawan = Karyawan.objects.get(id=pk)
    formkaryawan = KaryawanForm(instance=up_karyawan)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = KaryawanForm(request.POST, instance=up_karyawan)
        if formedit.is_valid:
            formedit.save()
            return redirect('karyawan')
    context = {
        'menu' : 'Update Karyawan',
        'page' : 'Edit karyawan', 
        'form' : formkaryawan,
        }
    return render(request, 'strap/update_karyawan.html', context)


@tolakhalaman_ini
def loginPage(request): 
    formlogin = AuthenticationForm
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        cocokan = authenticate(request, username=username, password=password )
        if cocokan is not None:
            login(request, cocokan)
            return redirect('beranda')    
    context = {
        'menu' : 'Login',
        'page' : 'Halaman login',    
        'tampillogin' : formlogin    
    }
    return render(request, 'strap/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')

def registerPage (request):
    formregister = RegisterForm()
    if request.method == 'POST':
        formregister = RegisterForm(request.POST)
        if formregister.is_valid():
            nilaiusername = formregister.cleaned_data.get('username')
            messages.success(request, f'Username Anda adalah {nilaiusername}')
            group_karyawan = formregister.save()             
            grup = Group.objects.get(name='karyawan')             
            group_karyawan.groups.add(grup)          
            Karyawan.objects.create(                 
                user=group_karyawan,                 
                nama_karyawan=group_karyawan.username) 
            formregister.save() 
            return redirect('login')

    context = {
        'menu': 'Halaman Register',
        'page': 'register',
        'tampilregister' : formregister
    }
    return render(request, 'strap/register.html', context)

@login_required(login_url='login')
def profilsaya(request):
    datakaryawan = request.user.karyawan
    form = ProfilForm(instance = datakaryawan)
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=datakaryawan)
        if form.is_valid:
            form.save() 
    context = {
        'menu': 'Profil',
        'page' : 'Halaman Profil',
        'formkaryawan': form
        
    }
    return render(request, 'strap/profil_saya.html', context)

@login_required(login_url='login')
def render_pdf_akta(request, pk):
    buatakta = Akta.objects.get(id=pk)

    template_path = 'strap/pdf_ajb.html'
    context = {'buatakta': buatakta}
    # Buat objek tanggapan Django, dan tentukan content_type sebagai pdf
    response = HttpResponse(content_type='application/pdf')
    # jika langsung mau di download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Jika pdf mau ditampilkan attachment dihapus
    response['Content-Disposition'] = 'filename="report.pdf"'
    # temukan template dan render.
    template = get_template(template_path)
    html = template.render(context)

    # buat pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # jika error tampil sebagai dibawah
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required(login_url='login')
def render_pdf_ah(request, pk):
    akta = Akta.objects.all()
    buatakta = Akta.objects.get(id=pk)

    template_path = 'strap/pdf_ah.html'
    context = {'buatakta': buatakta, 'akta' : akta}
    # Buat objek tanggapan Django, dan tentukan content_type sebagai pdf
    response = HttpResponse(content_type='application/pdf')
    # jika langsung mau di download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Jika pdf mau ditampilkan attachment dihapus
    response['Content-Disposition'] = 'filename="report.pdf"'
    # temukan template dan render.
    template = get_template(template_path)
    html = template.render(context)

    # buat pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # jika error tampil sebagai dibawah
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required(login_url='login')
def render_pdf_aphb(request, pk):
    buatakta = Akta.objects.get(id=pk)

    template_path = 'strap/pdf_aphb.html'
    context = {'buatakta': buatakta}
    # Buat objek tanggapan Django, dan tentukan content_type sebagai pdf
    response = HttpResponse(content_type='application/pdf')
    # jika langsung mau di download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Jika pdf mau ditampilkan attachment dihapus
    response['Content-Disposition'] = 'filename="report.pdf"'
    # temukan template dan render.
    template = get_template(template_path)
    html = template.render(context)

    # buat pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # jika error tampil sebagai dibawah
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required(login_url='login')
def render_pdf_skmht(request, pk):
    buatakta = Akta.objects.get(id=pk)

    template_path = 'strap/pdf_skmht.html'
    context = {'buatakta': buatakta}
    # Buat objek tanggapan Django, dan tentukan content_type sebagai pdf
    response = HttpResponse(content_type='application/pdf')
    # jika langsung mau di download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Jika pdf mau ditampilkan attachment dihapus
    response['Content-Disposition'] = 'filename="report.pdf"'
    # temukan template dan render.
    template = get_template(template_path)
    html = template.render(context)

    # buat pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # jika error tampil sebagai dibawah
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required(login_url='login')
def render_pdf_apht(request, pk):
    buatakta = Akta.objects.get(id=pk)

    template_path = 'strap/pdf_apht.html'
    context = {'buatakta': buatakta}
    # Buat objek tanggapan Django, dan tentukan content_type sebagai pdf
    response = HttpResponse(content_type='application/pdf')
    # jika langsung mau di download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Jika pdf mau ditampilkan attachment dihapus
    response['Content-Disposition'] = 'filename="report.pdf"'
    # temukan template dan render.
    template = get_template(template_path)
    html = template.render(context)

    # buat pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # jika error tampil sebagai dibawah
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



@login_required(login_url='login')
def export(request):
    akta_resource = AktaResources()
    dataset = akta_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Laporan.xls"'

    return response

# @login_required(login_url='login')
# def render_pdf_laporan(request):
#     buatakta = Akta.objects.all()

#     template_path = 'strap/pdf_laporan.html'
#     context = {'buatakta': buatakta
#     }
#     # Buat objek tanggapan Django, dan tentukan content_type sebagai pdf
#     response = HttpResponse(content_type='application/pdf')
#     # jika langsung mau di download
#     # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#     # Jika pdf mau ditampilkan attachment dihapus
#     response['Content-Disposition'] = 'filename="report.pdf"'
#     # temukan template dan render.
#     template = get_template(template_path)
#     html = template.render(context)

#     # buat pdf
#     pisa_status = pisa.CreatePDF(
#         html, dest=response)
#     # jika error tampil sebagai dibawah
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response