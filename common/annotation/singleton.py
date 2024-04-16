class Singleton:

    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if not self.instance:
            print(*args, **kwargs)
            self.instance = self.cls(*args, **kwargs)
        return self.instance


def singleton(cls):
    return Singleton(cls)
