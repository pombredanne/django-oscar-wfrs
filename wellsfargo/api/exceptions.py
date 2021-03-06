from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import APIException


class TransactionDenied(APIException):
    status_code = 403
    default_detail = _('Transaction was denied by Wells Fargo')


class CreditApplicationDenied(APIException):
    status_code = 403
    default_detail = _('Credit Application was denied by Wells Fargo')
