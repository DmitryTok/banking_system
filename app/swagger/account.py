CREATE_ACCOUNT_DOC = {
    "tags": ["Account"],
    "consumes": ["application/json"],
    "parameters": [
        {
            "in": "body",
            "name": "account",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "User's name",
                        "example": "Alice",
                    },
                    "initial_balance": {
                        "type": "number",
                        "format": "float",
                        "description": "Initial account balance",
                        "example": 1500.50,
                    },
                },
            },
        }
    ],
    "responses": {
        200: {
            "description": "Account successfully created",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "Unique account identifier",
                        "example": 1,
                    },
                    "name": {"type": "string", "example": "Alice"},
                    "balance": {
                        "type": "number",
                        "format": "float",
                        "example": 1500.50,
                    },
                },
            },
        },
        400: {
            "description": "Request error, required fields missing",
            "schema": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "example": "name and initial_balance are required",
                    }
                },
            },
        },
    },
}
