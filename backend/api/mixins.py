from rest_framework import mixins, viewsets


class ListRetrieveViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    """
    Пользовательский ViewSet - объединяет ListModelMixin и RetrieveModelMixin,
    для поддержки вывода списка нескольких объектов модели и получения
    информации об одном отдельном объекте модели.
    """
