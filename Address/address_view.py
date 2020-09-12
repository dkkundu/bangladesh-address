import logging
import os
import csv
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from .models_address import (Division, District, Upazila,
                     Union, PostOffice, Village)



# PYTHON IMPORTS
logger = logging.getLogger(__name__)
CUSTOM_USER_MODEL = get_user_model()


def ajax_load_districts(request):
    division_id = request.GET.get('division_id')
    try:
        districts = District.objects.filter(
            division_id=division_id).order_by('district')
    except ValueError:
        districts = District.objects.none()
    return render(request, 'Address/load_districts.html', {'districts': districts})


def ajax_load_upazilas(request):
    district_id = request.GET.get('district_id')
    try:
        upazilas = Upazila.objects.filter(
            district_id=district_id).order_by('upazila')
    except ValueError:
        upazilas = Upazila.objects.none()
    return render(request, 'Address/load_upazilas.html', {'upazilas': upazilas})


def ajax_load_unions(request):
    upazila_id = request.GET.get('upazila_id')
    try:
        unions = Union.objects.filter(
            upazila_id=upazila_id).order_by('union')
    except ValueError:
        unions = Union.objects.none()
    return render(request, 'Address/load_unions.html', {'unions': unions})


def ajax_load_postoffice(request):
    upazila_id = request.GET.get('upazila_id')
    print(upazila_id, 'Hello...')
    try:
        postoffices = PostOffice.objects.filter(
            upazila_id=upazila_id).order_by('postoffice')
    except ValueError:
        postoffices = PostOffice.objects.none()
    return render(request, 'Address/load_postoffice.html',
                  {'postoffices': postoffices})


def ajax_load_village(request):
    union_id = request.GET.get('union_id')
    print(union_id, '......')
    try:
        villages = Village.objects.filter(
            union_id=union_id).order_by('village_name')
    except ValueError:
        villages = Village.objects.none()
    return render(request, 'Address/load_village.html', {'villages': villages})



def import_district(request):
    if request.POST:
        pwd = os.path.dirname(__file__)
        with open(pwd + '/csv_source/District.csv', encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=',')
            count = 0
            for row in reader:
                district_name = row['District_Name'].strip()
                divission_name = row['Division_Name'].strip()
                district_code = row['District'].strip()

                if not district_name:
                    continue
                if not divission_name:
                    continue
                district = District.objects.filter(district=district_name)
                print("district paisi-------", district)
                if not district:
                    divisions = Division.objects.filter(
                        division=divission_name)
                    print("divisions paisi-------", divisions)
                    if divisions:
                        divisions = divisions[0]
                    else:
                        divisions = Division(division=divission_name)
                        print("notun division --save hoche---")
                        divisions.save()
                    created_district = District(district=district_name,
                                                district_code=district_code,
                                                division=divisions)
                    created_district.save()
                else:
                    print("existrAddress/ing---")
                count = count + 1
                print(count)
    return render(request, "Address/import_district.html")


def import_upazila(request):
    if request.POST:
        pwd = os.path.dirname(__file__)
        with open(pwd + '/csv_source/upojila.csv', encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=',')
            count = 0
            for row in reader:
                upozilla_name = row['Upazilla_Name'].strip()
                district_name = row['District_Name'].strip()
                upazila_code = row['Upazilla_code'].strip()

                if not upozilla_name:
                    continue
                if not district_name:
                    continue
                upozilla = Upazila.objects.filter(upazila=upozilla_name)
                print("district paisi-------", upozilla)
                if not upozilla:
                    district = District.objects.filter(district=district_name)
                    # print("divisions paisi-------", divisions)
                    if district:
                        district = district[0]
                    else:
                        district = District(district=district_name)
                        print("notun division --save hoche---")
                        district.save()
                    created_upozilla = Upazila(upazila=upozilla_name,
                                               upazila_code=upazila_code,
                                               district=district)
                    created_upozilla.save()
                else:
                    print("existring---")
                count = count + 1
                print(count)
    return render(request, "Address/import_upazila.html")


def import_union(request):
    if request.POST:
        pwd = os.path.dirname(__file__)
        with open(pwd + '/csv_source/union_villages.csv', encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=',')
            count = 0
            for row in reader:
                union_Name = row['Union_Name'].strip()
                upazilla_Name = row['Upazilla_Name'].strip()
                union_code = row['Union_code'].strip()
                if not union_Name:
                    continue
                if not upazilla_Name:
                    continue
                union = Union.objects.filter(union=union_Name,
                                             upazila__upazila=upazilla_Name)
                print("union-------", union)
                if not union:
                    upazila = Upazila.objects.filter(upazila=upazilla_Name)
                    # print("divisions paisi-------", divisions)
                    if upazila:
                        upazila = upazila[0]
                    else:
                        upazila = Upazila(upazila=upazilla_Name)
                        print("notun division --save hoche---")
                        upazila.save()
                    created_upozilla = Union(union=union_Name,
                                             union_code=union_code,
                                             upazila=upazila)
                    created_upozilla.save()
                else:
                    print("existring---")
                count = count + 1
                print(count)
    return render(request, "Address/import_union.html")


def import_village(request):
    if request.POST:
        pwd = os.path.dirname(__file__)
        with open(pwd + '/csv_source/union_villages.csv', encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=',')
            count = 0
            for row in reader:
                village_name = row['Village_Name'].strip()
                union_name = row['Union_Name'].strip()
                village_code = row['Village_code'].strip()
                union_code = row['Union_code'].strip()
                if len(village_code) > 3:
                    village_code = "0" + village_code
                if not village_name:
                    continue
                if not union_name:
                    continue
                village = Village.objects.filter(
                    village_name=village_name, union__union=union_name)
                print("Village paisi-------", village)
                if not village:
                    union = Union.objects.filter(
                        union=union_name, union_code=union_code)
                    # print("divisions paisi-------", divisions)
                    if union:
                        union = union[0]
                    else:
                        union = Union(union=union_name)
                        print("notun division --save hoche---")
                        union.save()
                    created_village = Village(village_name=village_name,
                                              village_code=village_code,
                                              union=union)
                    created_village.save()
                else:
                    print("existring---")
                count = count + 1
                print(count)
    return render(request, "Address/import_village.html")



def updated_database(request):
    return render(request, "Address/updated_database.html")
