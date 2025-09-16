class ZeroQuantityCategory(Exception):
    """Исключение для товаров с нулевым количеством"""
    def __init__(self,message=None):
        super().__init__(message)
