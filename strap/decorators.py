from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import Group

#ketika login lgsg ke home
def tolakhalaman_ini(fungsi_awal):
    def perubahan_halaman(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('beranda')
        else:
            return fungsi_awal(request, *args, **kwargs)
    return perubahan_halaman