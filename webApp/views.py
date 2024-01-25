from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import credentials, firestore, initialize_app
from .models import Calculation


@csrf_exempt
def calculate_sum(request):

    if request.method == 'POST':
        try:

            num1 = int(request.POST.get('num1', 0))
            num2 = int(request.POST.get('num2', 0))

            # Initialize Firebase app using credentials from the JSON file
            cred = credentials.Certificate("firebase_config.json")
            firebase_app = initialize_app(cred)
            db = firestore.client()

            # Perform the calculation
            result = num1 + num2


            calculation_mongo = Calculation.objects.create(number1=num1, number2=num2, result=result)


            calculations_ref = db.collection('calculations')
            calculations_ref.add({
                'number1': num1,
                'number2': num2,
                'result': result
            })


            return JsonResponse({'result': result})

        except ValueError:
            return JsonResponse({'error': 'Invalid number format'}, status=400)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
