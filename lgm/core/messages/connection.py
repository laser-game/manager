# coding=utf-8
from contextlib import contextmanager

import pika


@contextmanager
def connection():
    # TODO: parameters from settings
    # TODo: queue declarative definition
    pika_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = pika_connection.channel()
    try:
        yield channel
    finally:
        pika_connection.close()
