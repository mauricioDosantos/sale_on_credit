from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


INVOICE_STATUS = [ 
    ('Atrasado', 'Atrasado'),
    ('Em dias', 'Em dias'),
    ('A vencer', 'A vencer')
]
SALE_STATUS = [ 
    ('Saída', 'Saída'),
    ('Entrada', 'Entrada')
]


class Manager(BaseUserManager):
    def create_user(self, email, password, name, chip_id):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            chip_id=chip_id
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, name, chip_id):
        user = self.create_user(
            email,
            password=password,
            name=name,
            chip_id=chip_id
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Dividend(AbstractBaseUser):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    chip_id = models.CharField(max_length=200, unique=True, null=False, blank=False)
    limit = models.IntegerField(blank=True, null=True)
    due_day = models.CharField(max_length=2, blank=True,null=True)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = Manager()
    USERNAME_FIELD = 'email'
    # isso fez aparecer no terminal
    REQUIRED_FIELDS = ['name', 'chip_id']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

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
    dividend = models.ForeignKey(Dividend, on_delete=models.CASCADE)
    value = models.FloatField()
    payment_date = models.DateTimeField(default=None, blank=True, null=True)
    invoice_date = models.DateField(default= datetime.today() + relativedelta(days=10)) # previ de pagamento
    billing_month = models.DateField(default=datetime.today().date(), blank=True)  # data referente a fatura - sempre referete ao mês passado
    created_date = models.DateTimeField(auto_now_add=True, editable=False)  # data de criação da fatura
    status = models.CharField(max_length=20, choices=INVOICE_STATUS, default='Em dias')

    def __str__(self):
        nome = ''.join(set(div.div_id.name for div in self.sales.all()))
        return f'{nome.capitalize()} | Fechado em {self.value} | Vence {self.invoice_date}'