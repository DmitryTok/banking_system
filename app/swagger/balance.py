DEPOSIT_DOC = {
    "tags": ["Balance"],
    "consumes": ["application/json"],
    "parameters": [
        {
            "in": "query",
            "name": "account_id",
            "required": True,
            "type": "integer",
            "description": "ID of the account to deposit into",
            "example": 1,
        },
        {
            "in": "query",
            "name": "amount",
            "required": True,
            "type": "number",
            "format": "float",
            "description": "Amount to deposit",
            "example": 100.50,
        },
    ],
    "responses": {
        200: {
            "description": "Balance successfully updated",
            "schema": {
                "type": "object",
                "properties": {
                    "account_id": {"type": "integer", "example": 1},
                    "name": {"type": "string", "example": "Alice"},
                    "balance": {
                        "type": "number",
                        "format": "float",
                        "example": 1600.75,
                    },
                },
            },
        },
        400: {
            "description": "Request error (e.g., invalid account ID)",
            "schema": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "example": "Account not found or invalid amount",
                    }
                },
            },
        },
    },
}

WITHDRAW_DOC = {
    "tags": ["Balance"],
    "consumes": ["application/json"],
    "parameters": [
        {
            "in": "query",
            "name": "account_id",
            "required": True,
            "type": "integer",
            "description": "ID of the account to withdraw from",
            "example": 1,
        },
        {
            "in": "query",
            "name": "amount",
            "required": True,
            "type": "number",
            "format": "float",
            "description": "Amount to withdraw",
            "example": 200.75,
        },
    ],
    "responses": {
        200: {
            "description": "Balance successfully updated",
            "schema": {
                "type": "object",
                "properties": {
                    "account_id": {"type": "integer", "example": 1},
                    "name": {"type": "string", "example": "Alice"},
                    "balance": {
                        "type": "number",
                        "format": "float",
                        "example": 1400.25,
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
                        "example": "Account not found or insufficient balance",
                    }
                },
            },
        },
    },
}
