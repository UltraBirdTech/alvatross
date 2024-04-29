import datetime

class Logger():
    def __self__(self):
        self.log_info("log class initialize")

    def datetime_str(self):
        date_now = datetime.datetime.now()
        return str(date_now.strftime('%d/%m/%Y %H:%M:%S'))

    def log_info(self, log_message):
        print("[LOG][INFO][" + self.datetime_str() + "]: " + log_message)

    def log_warn(self, log_message):
        print("[LOG][WARN][" + self.datetime_str() + "]: " + log_message)

    def log_error(self, log_message):
        print("[LOG][ERROR][" + self.datetime_str() + "]: " + log_message)
