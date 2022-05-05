from rest_framework import pagination
from rest_framework.response import Response


class ProjectPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'next': self.page.next_page_number() if self.page.has_next() else None,
            'prev': self.page.previous_page_number() if self.page.has_previous() else None,
            'results': data
        })
