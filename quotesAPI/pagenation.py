from rest_framework import pagination

class CustomePagenation(pagination.PageNumberPagination):
    page_size = 30