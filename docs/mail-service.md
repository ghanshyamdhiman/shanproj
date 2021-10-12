# Mail Service

### Actions
1. Consume the messages published by the Order Service from the RabbitMQ broker

2. Send the following HTTP request to the [Mail Provider](mail-provider.md)

    `POST mail/send`

    Body:
    ```json
    {
        "type": "STRING",
        "payload": {
            "order": {
                "order_id": "UUID",
                "created_at": "DATETIME"
            },
            "product": {
                "name": "STRING",
                "price": "FLOAT"
            },
            "user": {
                "first_name": "STRING",
                "last_name": "STRING"
            }
        }
    }
    ```
