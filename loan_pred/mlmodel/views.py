from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


def home(request):
    return render(request,"index.html")

@csrf_exempt 
def predict(request):
     if request.method == 'POST':
        try:
            try:
                data = json.loads(request.body)
                print(data)
                return JsonResponse({ 
                "sucess":True,
                "data": str(data) })
            except: 
                try : 
                    data={'no_of_dependents' : request.POST.get('no_of_dependents'),
                    'education' : request.POST.get('education'),
                    'self_employed' : request.POST.get('self_employed'),
                    'income_annum' : request.POST.get('income_annum'),
                    'loan_amount' : request.POST.get('loan_amount'),
                    'loan_term' : request.POST.get('loan_term'),
                    'cibil_score' : request.POST.get('cibil_score'),
                    'residential_assets_value' : request.POST.get('residential_assets_value'),
                    'commercial_assets_value' : request.POST.get('commercial_assets_value'),
                    'luxury_assets_value' : request.POST.get('luxury_assets_value'),
                    'bank_asset_value' : request.POST.get('bank_asset_value')}
                    print(data)
                    return JsonResponse({ 
                    "sucess":True,
                    "data": str(data) })
                except Exception as e :
                    return JsonResponse({ 
                    "sucess":False,
                    "data": str(e) })
            
        except Exception as e :
            return JsonResponse({ 
            "sucess":False,
            "data": str(e) })

