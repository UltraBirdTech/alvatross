from django.test import TestCase
from ...models.logger import Logger

class LoggerTest(TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_info(self):
        self.logger.log_info('info')

    def test_warn(self):
        self.logger.log_warn('warn')

    def test_error(self):
        self.logger.log_error('error')
