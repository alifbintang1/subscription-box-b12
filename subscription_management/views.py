from django.http import JsonResponse
import requests
from django.shortcuts import render

def box_list(request):
    # response = requests.get('http://34.143.166.153/api/subscriptions/all')
    # boxes = response.json()
    # return render(request, 'boxes_list.html', {'boxes': boxes})

    min_price = request.GET.get('minPrice')
    max_price = request.GET.get('maxPrice')

    if min_price and max_price:
        response = requests.get(f'http://34.143.166.153/api/subscriptions/price?minPrice={min_price}&maxPrice={max_price}')
    else:
        response = requests.get('http://34.143.166.153/api/subscriptions/all')

        
    boxes = response.json()
    return render(request, 'boxes_list.html', {'boxes': boxes})

def box_detail(request, box_id):
    response = requests.get(f'http://34.143.166.153/api/subscriptions/{box_id}')
    box = response.json()
    return render(request, 'box_detail.html', {'box': box})

def subscription_history(request):
    response = requests.get('http://34.143.166.153/api/subscriptions/history')
    history = response.json()
    return render(request, 'subscription_history.html', {'history': history})

def fetch_boxes(request):
    # Extract minPrice and maxPrice from the request's query parameters
    min_price = request.GET.get('minPrice', None)
    max_price = request.GET.get('maxPrice', None)
    name = request.GET.get('name', None)

    # Construct the URL based on the provided parameters
    
    url = f'http://34.143.166.153/api/subscriptions/price?minPrice={min_price}&maxPrice={max_price}'
    response = requests.get(url)
    data = response.json()

    if name:
        url = f'http://34.143.166.153/api/subscriptions/name?name={name}'
        data2 = requests.get(url).json()

        dict1 = {item['id']: item for item in data}
        dict2 = {item['id']: item for item in data2}

        # Finding common ids
        intersection_ids = set(dict1.keys()) & set(dict2.keys())

        # Getting the intersection items based on common ids
        intersection = [dict1[id] for id in intersection_ids]
        
        return JsonResponse(intersection, safe=False)
    
    return JsonResponse(data, safe=False)

    # try:
    #     # Making the GET request to the external API
    #     response = requests.get(url)

    #     # Check if the request was successful
    #     if response.status_code == 200:
    #         data = response.json()
    #         return JsonResponse(data, safe=False)  # Return the JSON data directly
    #     else:
    #         # Return an error JSON if the API did not succeed
    #         return JsonResponse({'error': 'Failed to fetch data', 'status_code': response.status_code}, status=response.status_code)
    # except requests.exceptions.RequestException as e:
    #     # Return an error message if an exception occurs during the request
    #     return JsonResponse({'error': str(e)}, status=500)
    

