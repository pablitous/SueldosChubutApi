from django.http import JsonResponse
from django.utils import timezone


def create_json_response(status_code, message, data=None):
    response_data = {
        'status': status_code,
        'message': message,
        'data': data,
        'timestamp': timezone.now().isoformat(),
    }

    return JsonResponse(response_data)