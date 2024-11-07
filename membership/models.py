from django.db import models


class Membership(models.Model):
    first_name = models.CharField("First Name",max_length=100)
    last_name = models.CharField("Last Name",max_length=100)
    phone = models.CharField("Phone",max_length=15)
    email = models.EmailField("Email")
    saving_account = models.CharField("Saving Account", max_length=50)
    loan_account = models.CharField("Loan Account", max_length=50)
    receipt = models.FileField(upload_to='receipts/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone}"
