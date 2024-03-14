class Utils:
    @staticmethod
    def decode_message(data, splits = None):
        try:
            if splits:
                return data.decode().split("|", splits)
            else:
                return data.decode().split("|")
        except ValueError:
            return None, None, None