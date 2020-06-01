from items.models import Item, BookedItem
from items.serializers import ItemSerializer, BookedItemSerializer
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

import sys
sys.path.append('../')
from meridien import views_template

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def item_list(request):
    return views_template.obj_list(request, Item, ItemSerializer)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def item_detail(request, pk):
    return views_template.obj_detail(request, pk, Item, ItemSerializer)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def booked_item_list(request):
    return views_template.obj_list(request, BookedItem, BookedItemSerializer)

@api_view(['GET'])
@permission_classes([IsAuthenticated])    
@csrf_exempt
def booked_item_detail(request, pk):
    return views_template.obj_detail(request, pk, BookedItem, BookedItemSerializer)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt    
def booked_item_from_booking_id(request, booking_id):
    items = BookedItem.objects.filter(booking_source=booking_id)
    
    if request.method == 'GET':
        booked_item_serializer = BookedItemSerializer(items, many=True)
        return JsonResponse(booked_item_serializer.data, safe=False)