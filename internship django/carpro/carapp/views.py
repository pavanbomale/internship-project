import pickle
from django.shortcuts import render, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import numpy

columns = open('carapp\\artifacts\\columns.json')
f_columns = json.load(columns)

brand_model = open('carapp\\artifacts\\brand_model.json')
f_brand_model = json.load(brand_model)

scaler_file = open('carapp\\artifacts\\scaler.pickle', 'rb')
scaler = pickle.load(scaler_file)

# Create your views here.
def index(request):
    return render(request, 'index.html')

def get_brands(request):
    response_data = {}
    response_data['brands'] = f_columns['columns'][12:43]
    return HttpResponse(json.dumps(response_data))

@csrf_exempt
def get_models(request):
    try:
        brand = request.GET.get('brand')
        models = f_brand_model[brand]
        response_data = {}
        response_data['models'] = list(models)
        return HttpResponse(json.dumps(response_data)) 
    except:
        return HttpResponse([])

def get_price(request):
    context = {}
    if request.method == 'POST':
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        age = request.POST.get('age')
        km_driven = request.POST.get('km_driven')
        mileage = request.POST.get('mileage')
        cc = request.POST.get('cc')
        bhp = request.POST.get('bhp')
        seats = request.POST.get('seats')
        cost = request.POST.get('cost')
        fuel = request.POST.get('fuel')
        transmission = request.POST.get('transmission')
        
        cols = list(f_columns['columns'])
        zeros =  numpy.zeros(len(f_columns['columns']), dtype='int')
        try:
            zeros[cols.index(brand)] = 1
            zeros[cols.index(model)] = 1
            zeros[cols.index(fuel)] = 1
            zeros[cols.index(transmission)] = 1
        except:
            pass
        zeros[0] = age
        zeros[1] = km_driven
        zeros[2] = mileage
        zeros[3] = cc
        zeros[4] = bhp
        zeros[5] = seats
        zeros[6] = cost

        scaled_data = scaler.transform(numpy.array([zeros]))
   
        model_file = open('carapp\\artifacts\\used_cars.pickle', 'rb')
        model = pickle.load(model_file)
        context['prediction'] = model.predict(scaled_data)

    return render(request, 'get_price.html', context=context)