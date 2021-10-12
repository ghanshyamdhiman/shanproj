# Order Service

### Actions

1. Implement the endpoint described below.

    `POST orders/`

    Body:
    ```json
    {
        "user_id": "UUID",
        "product_code": "STRING"
    }
    ```

2. Save the order in the database.

3. Retrieve information from the [Product Service](product-service.md).

4. Retrieve information from the [User Service](user-service.md).

5. Publish the following message to the RabbitMQ Broker

    Exchange: `orders`

    Routing Key: `created_order`

    Body:
    ```json
    {
        "producer": "STRING",
        "sent_at": "DATETIME",
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
