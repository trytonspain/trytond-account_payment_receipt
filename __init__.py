# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .account import *


def register():
    Pool.register(
        MoveLine,
        module='account_payment_receipt', type_='model')
    Pool.register(
        Receipt,
        module='account_payment_receipt', type_='report')
