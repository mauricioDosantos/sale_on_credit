from operator import index
from telnetlib import STATUS
from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta


INVOICE_STATUS = [ 
    ('Atrasado', 'Atrasado'),
    ('Em dias', 'Em dias'),
    ('A vencer', 'A vencer')
]
SALE_STATUS = [ 
    ('Saída', 'Saída'),
    ('Entrada', 'Entrada')
]

class Dividend(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    chip_id = models.CharField(max_length=200, unique=True, null=False, blank=False)
    limit = models.IntegerField()
    due_day = models.CharField(max_length=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name.capitalize()


class Movement(models.Model):
    div_id = models.ForeignKey(Dividend, on_delete=models.CASCADE)
    value = models.FloatField(null=False)
    type = models.CharField(max_length=20, choices=SALE_STATUS, default='Saída')
    purchase_date = models.DateField(null=False)

    def __str__(self):
        #div = ", ".join(str(seg.name) for seg in self.dividens.all())
        return f'{self.type} | {self.div_id.name.capitalize()} | {self.purchase_date} | R$ {self.value}'


class Invoice(models.Model):
    sales = models.ManyToManyField(Movement)
    value = models.FloatField()
    payment_date = models.DateTimeField(default=None, blank=True, null=True)
    invoice_date = models.DateField(default= datetime.today() + relativedelta(days=10)) # previ de pagamento
    billing_month = models.DateField(default=datetime.today(), blank=True)  # data referente a fatura - sempre referete ao mês passado
    created_date = models.DateTimeField(auto_now_add=True, editable=False)  # data de criação da fatura
    status = models.CharField(max_length=20, choices=INVOICE_STATUS, default='Em dias')

    def __str__(self):
        nome = ''.join(set(div.div_id.name for div in self.sales.all()))
        return f'{nome.capitalize()} | Fechado em {self.value} | Vence {self.invoice_date}'