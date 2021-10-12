import uuid
from django.db import models
  
class Orders(models.Model):
    user_id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)

    product_code = models.CharField(max_length=50)

    def __dir__(self):
        return self.user_id
