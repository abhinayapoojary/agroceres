# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from agro_app import list_mandal
from agro_app import process_mandal
from agro_app import process_month
from agro_app import list_crop
from agro_app import list_crop_type
from agro_app import list_crop_districts
from agro_app import crop_district_result

@csrf_exempt
def display(request):
    if request.method == 'GET':
        return render(request, 'index.html')


@csrf_exempt
def select_state(request):
    if request.method == 'GET':
        return render(request, 'select_state.html')


@csrf_exempt
def select_district(request):
    if request.method == 'GET':
        return render(request, 'select_district.html')


@csrf_exempt
def area_under_growth(request):
    if request.method == 'POST':
        selected_districts = []
        for key, value in request.POST.items():
            selected_districts.append(key)
        print(selected_districts)
        return render(request, 'area_under_growth.html', {"districts": selected_districts})


@csrf_exempt
def mandal(request, dist):
    print(dist)
    mandals = list_mandal.list_mandal(dist)
    return render(request, 'list_mandal.html', {"mandals": mandals})


@csrf_exempt
def select_mandal(request):
    if request.method == 'POST':
        select_mandals = []
        for key, value in request.POST.items():
            select_mandals.append(key)

        process_mandal.process_mandal(select_mandals[0])
        return render(request, 'output1.html')


@csrf_exempt
def select_month(request):
    if request.method == 'GET':
        return render(request, 'select_month.html')

    if request.method == 'POST':
        selected_month = request.POST.get('selected_month')
        selected_day = request.POST.get('day')
        response = process_month.process_month(selected_month, selected_day)
        return HttpResponse(response, status=200)


@csrf_exempt
def get_crops(request):
    if request.method == 'GET':
        crops = list_crop.list_crop()
        return render(request, 'select_crop.html', {"crops": crops})


@csrf_exempt
def get_crop_type(request):
    if request.method == 'POST':
        selected_crop = []
        for key, value in request.POST.items():
            selected_crop.append(key)

        crop_types = list_crop_type.get_crop_types(selected_crop[0])

        return render(request, 'list_crop_types.html', {"crop_types": crop_types})


@csrf_exempt
def get_crop_district(request):
    if request.method == 'POST':
        selected_crop_type = []
        for key, value in request.POST.items():
            selected_crop_type.append(key)

        print(selected_crop_type)
        crop_districts = list_crop_districts.get_crop_district(selected_crop_type[0])

        print(crop_districts)
    return render(request, 'list_crop_district.html', {"crop_districts": crop_districts})


@csrf_exempt
def get_crop_district_result(request):
    if request.method == 'POST':
        selected_crop_district = []
        for key, value in request.POST.items():
            selected_crop_district.append(key)

        crop_result = crop_district_result.get_result(selected_crop_district[0])

        print(crop_result)
    return render(request, 'index.html')
