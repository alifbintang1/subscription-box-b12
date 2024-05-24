import requests
from django.shortcuts import render

def subscription_list(request):
    response = requests.get('http://34.143.166.153/api/subscriptions/all')
    subscriptions = response.json()
    return render(request, 'subscription_list.html', {'subscriptions': subscriptions})

def subscription_detail(request, subscription_id):
    response = requests.get(f'http://34.143.166.153/api/subscriptions/all/{subscription_id}')
    subscription = response.json()
    return render(request, 'subscription_detail.html', {'subscription': subscription})

def subscription_history(request):
    response = requests.get('http://34.143.166.153/api/subscriptions/history')
    history = response.json()
    return render(request, 'subscription_history.html', {'history': history})
