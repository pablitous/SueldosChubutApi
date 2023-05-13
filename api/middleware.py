import time
from django.http import JsonResponse
import json

class ElapsedRequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Start measuring time
        start_time = time.time()

        response = self.get_response(request)

        # Calculate elapsed time in milliseconds
        elapsed_time = format(((time.time() - start_time) * 1000),'.2f')
                

        # Add elapsed time to JSON response if it's a JsonResponse
        if isinstance(response, JsonResponse):
            response.content = response.content.decode('utf-8')  # Decode JSON content
            data = json.loads(response.content)
            data['elapsed_time_ms'] = str(elapsed_time)
            response.content = json.dumps(data)

        return response