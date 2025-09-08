from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserDetail, Expense
# signUp API 

def signUp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        FullName = data.get('FullName')
        email = data.get('email')
        password = data.get('password')
        
        if UserDetail.objects.filter(email=email).exists():
            return JsonResponse({'status': 'error', 'message': 'Email already exists'}, status=400) # 400 Bad Request
        
        user = UserDetail(FullName=FullName, email=email, password=password)
        user.save()
        
        return JsonResponse({'status': 'success', 'message': 'User registered successfully'},status=201) # 201 Created
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405) # 405 Method Not Allowed