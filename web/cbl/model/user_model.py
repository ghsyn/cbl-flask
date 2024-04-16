class Model:
    def __init__(self):
        pass  # 특별히 초기화 필요 없음.

    def __str__(self):
        return f'{self.id}'

    def __repr__(self):
        return f'{self.id}'

    def append_variable(self, name, val):
        setattr(self, name, val)