from django.shortcuts import render, HttpResponse
from .models import Invoice, Dividend, Movement

def index():
    return HttpResponse("Hello, world. You're at the polls index.")

# visão para o cliente


def invoice(request, user_id):
    invoices = Invoice.objects.filter(dividend=user_id)
    user_info = Dividend.objects.filter(_id=user_id)
    moviments = Movement.objects.filter(div_id=user_id)
    return render(
        request, 'main_invoice.hrml', {
            'invoices': invoices, 'info': user_info, 'moviments': moviments
        }
    )


# função para gerar as faturas: fechamento da fatura 10 dias anstes da data da fatura - o sistema gera essa fatura.
# função para mostar o saldo do cliente
# visão do admin ficarã para o pai e ivanilson.
# rotas de registro de movimentação
# rotas para ver a fatura do cliente - ivanilson - acessar pelo celular
# cliente pode ver seu saldo ainda disponível, e faturas
