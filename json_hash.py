import jsonpickle


class JsonHash:
    @staticmethod
    def encode(value):
        return jsonpickle.encode(value)

    @staticmethod
    def decode(value):
        return jsonpickle.decode(value)
