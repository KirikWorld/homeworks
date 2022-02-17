from datetime import datetime


class DateSlug:
    regex = '\d{4}-[0-1]\d-[0-3]\d'

    def to_python(self, value):
        return datetime.strptime(value, "%Y-%m-%d")

    def to_url(self, value):
        return value.strftime("%Y-%m-%d")
