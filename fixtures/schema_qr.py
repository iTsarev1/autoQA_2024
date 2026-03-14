from pytest import fixture


@fixture
def resp_schema_get_qr():
    return {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "number": {"type": "integer"},
            "customer": {"type": "object"},
            "name": {"type": "string"},
            "delivery": {"type": "object"},
            "requirements": {"type": "object"},
            "status": {"type": "string"},
            "responseDate": {"type": "string"},
            "comment": {"type": ["string", "null"]},
            "quoteItemsCount": {"type": "integer"},
            "cost": {"type": ["number", "null"]},
            "purchaseStatusCount": {"type": "object"},
            "discountLastDateResponse": {"type": ["string", "null"]},
            "updatedAt": {"type": "string"},
            "purchaseType": {"type": "string"},
            "isExpress": {"type": "boolean"},
            "maxPriceOfContract": {"type": ["number", "null"]},
            "listMethodSignContract": {
                "type": "array",
                "items": {"type": "string"}
            }
        }
    }