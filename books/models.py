import uuid 
from django.contrib.auth import get_user_model
#我們需要get_user_model,這樣我們才能Customer模型．．

from django.db import models
from django.urls import reverse


class Book(models.Model): 
    id = models.UUIDField( primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk':str(self.pk)})

class Review(models.Model):
    book = models.ForeignKey(
    #book這個字段是所謂的1對多的fk，將Book模型和Review模型連接
    #有點類似join，Review有點類似外表。Book是主表..
    #只有外表才能發出fk，一般外表發出的fk，一般會加入的related_name
    #一般是本表的復數形式。這是由於外表屬於一對多裏面的多
    #book field is the one-to-many fk that links books to review
    #這是標準操作。。 
        Book,
        on_delete = models.CASCADE,
        related_name = 'reviews',
    )

    review = models.CharField(max_length=255)
    author = models.ForeignKey(
    #and then we'll also link to the author field to auto-populate the
    #current user with the reivew
    #用get_user_model()可以ref to  custom  user model 

        get_user_model(),
        on_delete=models.CASCADE,
        )
    def __str__(self):
        return self.review



