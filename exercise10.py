class NonPositiveError(Exception):
    pass


class PositiveList(list):

    def append(self, element):
        if not element > 0:
            raise NonPositiveError
        super().append(element)

