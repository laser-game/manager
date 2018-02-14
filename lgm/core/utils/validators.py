# coding=utf-8
from datetime import timedelta

from django.core.validators import MaxValueValidator, MinValueValidator


class MinDurationValidator(MinValueValidator):
    def __init__(self, seconds_limit, message=None):
        super().__init__(timedelta(seconds=seconds_limit), message)


class MaxDurationValidator(MaxValueValidator):
    def __init__(self, seconds_limit, message=None):
        super().__init__(timedelta(seconds=seconds_limit), message)
