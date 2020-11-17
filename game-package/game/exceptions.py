class GameUnitException(Exception):
    def __init__(self, message='', code=000):
        super.__init__(message)
        self.error_message = '~' * 50 + '\n'
        self.error_dict = {
            000: "Error 000: Unspecified Error",
            100: "Error 100: Health Meter Error",
            200: "Error 200: Attack Issue. Ignored"
        }

        try:
            self.error_message += self.error_dict[code]
        except KeyError:
            self.error_message += self.error_dict[000]
        self.error_message = '~' * 50 + '\n'

class HealthMeterException(GameUnitException):
    def __init__(self, message='', code=000):
        super.__init__(message)
        self.error_message = "Health Meter Error"