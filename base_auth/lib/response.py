from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

def ResponseMessage(status_code=500, headers=None, content_type=None):

    response = {
        200: Response(
            {'success': ['Ok']},
            status=status.HTTP_200_OK,
            headers=headers,
            content_type=content_type
        ),
        201: Response(
            {'success': ['Created']},
            status=status.HTTP_201_CREATED,
            headers=headers,
            content_type=content_type
        ),
        204: Response(
            {'success': ['Content not found']},
            status=status.HTTP_204_NO_CONTENT,
            headers=headers,
            content_type=content_type
        ),
        400: Response(
            {'error': ['Bad request']},
            status=status.HTTP_400_BAD_REQUEST,
            headers=headers,
            content_type=content_type
        ),
        403: Response(
            {'error': ['Forbidden']},
            status=status.HTTP_403_FORBIDDEN,
            headers=headers,
            content_type=content_type
        ),
        404: Response(
            {'error': ['Not found']},
            status=status.HTTP_404_NOT_FOUND,
            headers=headers,
            content_type=content_type
        ),
        405: Response(
            {'error': ['Method not allowed.']},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
            headers=headers,
            content_type=content_type
        ),
        406: Response(
            {'error': ['Not acceptable']},
            status=status.HTTP_406_NOT_ACCEPTABLE,
            headers=headers,
            content_type=content_type
        ),
        500: Response(
            {'failed': ['Internal server error']},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            headers=headers,
            content_type=content_type
        ),
    }

    return response.get(int(status_code), Response(
        {'failed': ['Service unavailable']}, status=status.HTTP_503_SERVICE_UNAVAILABLE
    ))