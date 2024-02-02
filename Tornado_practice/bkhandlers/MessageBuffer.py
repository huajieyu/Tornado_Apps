import logging
import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.web
import os.path
import uuid

from tornado import gen
from tornado.options import define, options, parse_command_line


class MessageBuffer(object):
    def __init__(self):
        self.waiters = set()
        self.cache = []
        self.cache_size = 200

    def wait_for_messages(self, callback, cursor=None):
        print("***[MessageBuffer] wait for message function")
        if cursor:
            new_count = 0
            for msg in reversed(self.cache):
                if msg["id"] == cursor:
                    break
                new_count += 1
            if new_count:
                callback(self.cache[-new_count:])
                return
        self.waiters.add(callback)

    def cancel_wait(self, callback):
        print("***[MessageBuffer] cancel wait function")
        self.waiters.remove(callback)

    def new_messages(self, messages):
        print("***[MessageBuffer] new message function", messages)
        logging.info("Sending new message to %r listeners", len(self.waiters))
        for callback in self.waiters:
            try:
                callback(messages)
            except:
                logging.error("Error in waiter callback", exc_info=True)
        self.waiters = set()
        self.cache.extend(messages)
        print("***[MessageBuffer] cache.extend of message is ", len(self.cache))
        print("***[MessageBuffer] cache_size ", self.cache_size)

        if len(self.cache) > self.cache_size:
            self.cache = self.cache[-self.cache_size:]


