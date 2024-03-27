from typing import Dict, List, Union
from django.http import JsonResponse

class APIResponse:
    @staticmethod
    def success(data: Union[None, Dict[str, any]] = None, message: str = None, status_code: int = 200) -> JsonResponse:
        response_data = {
            "ok": True,
            "message": message,
            "data": data
        }
        return JsonResponse(response_data, status=status_code)

    @staticmethod
    def error(message: str = None, errors: Union[None, List[str]] = None, status_code: int = 400) -> JsonResponse:
        response_data = {
            "ok": False,
            "message": message,
            "errors": errors
        }
        return JsonResponse(response_data, status=status_code)
