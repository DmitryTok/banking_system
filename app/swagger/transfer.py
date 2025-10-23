TRANSFER_DOC = {
    "tags": ["Transfer"],
    "consumes": ["application/json"],
    "parameters": [
        {
            "in": "query",
            "name": "from_account_id",
            "required": True,
            "type": "integer",
            "description": "ID of the account to withdraw from",
            "example": 1,
        },
        {
            "in": "query",
            "name": "to_account_id",
            "required": True,
            "type": "integer",
            "description": "ID of the account to deposit into",
            "example": 2,
        },
        {
            "in": "query",
            "name": "amount",
            "required": True,
            "type": "number",
            "format": "float",
            "description": "Amount to transfer",
            "example": 100.50,
        },
    ],
    "responses": {
        200: {
            "description": "Transfer successfully completed",
            "schema": {
                "type": "object",
                "properties": {
                    "from_account": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer", "example": 1},
                            "name": {"type": "string", "example": "Alice"},
                            "balance": {
                                "type": "number",
                                "format": "float",
                                "example": 900.50,
                            },
                        },
                    },
                    "to_account": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer", "example": 2},
                            "name": {"type": "string", "example": "Bob"},
                            "balance": {
                                "type": "number",
                                "format": "float",
                                "example": 1100.50,
                            },
                        },
                    },
                },
            },
        },
        400: {
            "description": "Request error (e.g., invalid account ID or insufficient funds)",
            "schema": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "example": "Insufficient balance or account not found",
                    }
                },
            },
        },
    },
}
