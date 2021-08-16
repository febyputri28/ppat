from django.urls import path 
from . import views

urlpatterns = [     
    path('', views.home, name='beranda'),   

    path('aktamasuk/', views.aktamasuk, name='aktamasuk'), 
    path('delete_akta/<str:pk>', views.delete_akta, name='delete_akta'), 
    path('updateakta/<str:pk>', views.updateAkta, name='updateakta'),


    path('tampilform/', views.tampilform, name='tampilform'), 
    path('SimpanFormK/', views.SimpanFormK, name='SimpanFormK'), 

    
    # path('tambah_aktamasuk/', views.tambah_aktamasuk, name='tambah_aktamasuk'),
    # path('update_aktamasuk/<str:pk>', views.update_aktamasuk, name='update_aktamasuk'),

    path('tampilclientsatujs/', views.TampilClientSatu, name='tampilclientsatujs'),
    path('tampilclientduajs/', views.TampilClientDua, name='tampilclientduajs'),
    path('TampilKaryawan/', views.TampilKaryawan, name='TampilKaryawan'),

    # path('keyup/', views.keyup, name='keyup'),


    path('buatakta/', views.buatakta, name='buatakta'),
    path('simpanclientpertama/', views.simpanclientpertama, name='simpanclientpertama'),
    path('simpanclientkedua/', views.simpanclientkedua, name='simpanclientkedua'),
    path('simpanketerangan/', views.simpanketerangan, name='simpanketerangan'),
    path('simpantransaksi/', views.simpantransaksi, name='simpantransaksi'),

    
    path('hapusclientsatu/', views.hapusclientsatu, name='hapusclientsatu'),
    path('hapusclientkedua/', views.hapusclientkedua, name='hapusclientkedua'),
    path('hapuskaryawan/', views.hapuskaryawan, name='hapuskaryawan'),



    path('karyawan/', views.karyawan, name='karyawan'),
    path('formkaryawan/', views.Tambahkaryawan, name='formkaryawan'),
    path('updatekaryawan/<str:pk>', views.updateKaryawan, name='updatekaryawan'),

    path('jenis/', views.jenis, name='jenis'),

    path('profilsaya/', views.profilsaya, name='profilsaya'),

    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),


    path('renderpdf/<str:pk>', views.render_pdf_akta, name='renderpdf'),
    path('render_pdf_ah/<str:pk>', views.render_pdf_ah, name='render_pdf_ah'),
    path('render_pdf_aphb/<str:pk>', views.render_pdf_aphb, name='render_pdf_aphb'),
    path('render_pdf_skmht/<str:pk>', views.render_pdf_skmht, name='render_pdf_skmht'),
    path('render_pdf_apht/<str:pk>', views.render_pdf_apht, name='render_pdf_apht'),

    path('export/', views.export, name='export'),

    
    # path('render_pdf_laporan/', views.render_pdf_laporan, name='render_pdf_laporan')

    
    ]