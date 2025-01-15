class ServiceError(Exception):
    def __init__(self, message, code,internal_error_code):
        super().__init__(message)
        self.code = code
        self.internal_error_code = internal_error_code


class ItemNotFoundError(ServiceError):
    def __init__(self, item_name):
        super().__init__(f"Item '{item_name}' not found in pricing rules.", code="ITEM_NOT_FOUND",internal_error_code="CK001")

