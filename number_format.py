# -*- encoding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2012-2014 NaN Projectes de Programari Lliure, S.L.
#                         All Rights Reserved.
#                         http://www.NaN-tic.com
#
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
##############################################################################

from decimal import Decimal
import math

SUPPORTED_LANGS = ('en', 'es', 'ca')

TENS_UNITS_SEP = {
    'en': u"-",
    'es': u" y ",
    'ca': u"-",
}
CURRENCY_DECIMALS_SEP = {
    'en': u"with",
    'es': u"con",
    'ca': u"amb",
}
NOT_CURRENCY_DECIMALS_SEP = {
    'en': u"dot",
    'es': u"coma",
    'ca': u"coma",
}

CURRENCY_INTEGER_NAME = {
    0: {'en': u"Euros", 'es': u"Euros", 'ca': u"Euros"},
    1: {'en': u"Euro", 'es': u"Euro", 'ca': u"Euro"},
    2: {'en': u"Euros", 'es': u"Euros", 'ca': u"Euros"},
}
CURRENCY_DECIMALS_NAME = {
    0: {'en': u"Cents", 'es': u"Céntimos", 'ca': u"Cèntims"},
    1: {'en': u"Cent", 'es': u"Céntimo", 'ca': u"Cèntim"},
    2: {'en': u"Cents", 'es': u"Céntimos", 'ca': u"Cèntims"},
}

TENS = {
    20: {'en': u"Twenty", 'es': u"Venti", 'ca': u"Vint"},
    30: {'en': u"Thirty", 'es': u"Treinta", 'ca': u"Trenta"},
    40: {'en': u"Forty", 'es': u"Cuarenta", 'ca': u"Quaranta"},
    50: {'en': u"Fifty", 'es': u"Cincuenta", 'ca': u"Cinquanta"},
    60: {'en': u"Sixty", 'es': u"Sesenta", 'ca': u"Seixanta"},
    70: {'en': u"Seventy", 'es': u"Setenta", 'ca': u"Setanta"},
    80: {'en': u"Eighty", 'es': u"Ochenta", 'ca': u"Vuitanta"},
    90: {'en': u"Ninety", 'es': u"Noventa", 'ca': u"Noranta"},
}

HUNDREDS = {
    100: {'en': u"One Hundred", 'es': u"Ciento", 'ca': u"Cent"},
    200: {'en': u"Two Hundred", 'es': u"Doscientos", 'ca': u"Dos-cents"},
    300: {'en': u"Three Hundred", 'es': u"Trescientos", 'ca': u"Tres-ents"},
    400: {
        'en': u"Four Hundred",
        'es': u"Cuatrocientos",
        'ca': u"Quatre-cents"},
    500: {'en': u"Five Hundred", 'es': u"Quinientos", 'ca': u"Cinc-cents"},
    600: {'en': u"Six Hundred", 'es': u"Seiscientos", 'ca': u"Sis-cents"},
    700: {'en': u"Seven Hundred", 'es': u"Setecientos", 'ca': u"Set-cents"},
    800: {'en': u"Eight Hundred", 'es': u"Ochocientos", 'ca': u"Vuit-cents"},
    900: {'en': u"Nine Hundred", 'es': u"Novecientos", 'ca': u"Nou-cents"},
}

GREATER = {
    1000: {'en': u"One Thousand", 'es': u"Mil", 'ca': u"Mil"},
    1000000: {'en': u"One Million", 'es': u"Millones", 'ca': u"Milions"},
}

UNITS = TENS.copy()
UNITS.update(HUNDREDS)
UNITS.update(GREATER)
UNITS.update({
    0: {'en': u"Zero", 'es': u"Cero", 'ca': u"Zero"},
    1: {'en': u"One", 'es': u"Un", 'ca': u"Un"},
    2: {'en': u"Two", 'es': u"Dos", 'ca': u"Dos"},
    3: {'en': u"Three", 'es': u"Tres", 'ca': u"Tres"},
    4: {'en': u"Four", 'es': u"Cuatro", 'ca': u"Quatre"},
    5: {'en': u"Five", 'es': u"Cinco", 'ca': u"Cinc"},
    6: {'en': u"Six", 'es': u"Seis", 'ca': u"Sis"},
    7: {'en': u"Seven", 'es': u"Siete", 'ca': u"Set"},
    8: {'en': u"Eight", 'es': u"Ocho", 'ca': u"Vuit"},
    9: {'en': u"Nine", 'es': u"Nueve", 'ca': u"Nou"},
    10: {'en': u"Ten", 'es': u"Diez", 'ca': u"Deu"},
    11: {'en': u"Eleven", 'es': u"Once", 'ca': u"Onze"},
    12: {'en': u"Twelve", 'es': u"Doce", 'ca': u"Dotze"},
    13: {'en': u"Thirteen", 'es': u"Trece", 'ca': u"Tretze"},
    14: {'en': u"Fourteen", 'es': u"Catorce", 'ca': u"Catorze"},
    15: {'en': u"Fifteen", 'es': u"Quince", 'ca': u"Quinze"},
    16: {'en': u"Sixteen", 'es': u"Dieciséis", 'ca': u"Setze"},
    17: {'en': u"Seventeen", 'es': u"Diecisiete", 'ca': u"Disset"},
    18: {'en': u"Eighteen", 'es': u"Dieciocho", 'ca': u"Divuit"},
    19: {'en': u"Nineteen", 'es': u"Diecinueve", 'ca': u"Dinou"},
    # When the values is exactly '20', is so called
    20: {'es': u"Veinte", 'ca': u"Vint"},
    21: {'es': u"Veintiún", 'ca': u"Vint-i-un"},
    22: {'es': u"Veintidós", 'ca': u"Vint-i-dos"},
    23: {'es': u"Veintitrés", 'ca': u"Vint-i-tres"},
    24: {'es': u"Veinticuatro", 'ca': u"Vint-i-quatre"},
    25: {'es': u"Veinticinco", 'ca': u"Vint-i-cinc"},
    26: {'es': u"Veintiséis", 'ca': u"Vint-i-sis"},
    27: {'es': u"Veintisiete", 'ca': u"Vint-i-set"},
    28: {'es': u"Veintiocho", 'ca': u"Vint-i-vuit"},
    29: {'es': u"Veintinueve", 'ca': u"Vint-i-nou"},
    # When the values is exactly '100', is so called
    100: {'en': u"Hundred", 'es': u"Cien", 'ca': u"Cent"},
    1000: {'en': u"Thousand", 'es': u"Mil", 'ca': u"Mil"},
    1000000: {'en': u"Million", 'es': u"Un Millón", 'ca': u"Un Milió"},
})


def integer_to_literal(input_int, lang_code):
    assert type(input_int) == int, (
        "Invalid type of parameter. Expected 'int' "
        "but found %s" % str(type(input_int)))
    assert lang_code and lang_code in SUPPORTED_LANGS, (
        "The Language Code "
        "is not supported. The suported languages are: %s"
        % ", ".join(SUPPORTED_LANGS[:-1]) + " and " +
        SUPPORTED_LANGS[-1])

    if input_int in UNITS and lang_code in UNITS[input_int]:
        return UNITS[input_int][lang_code]

    million = int(math.floor(Decimal(str(input_int)) / 1000000))
    thousands = input_int - million * 1000000
    thousands = int(math.floor(Decimal(str(thousands)) / 1000))
    hundreds = input_int - million * 1000000 - thousands * 1000

    def __convert_hundreds(input_hundred):
        assert (input_hundred and
                type(input_hundred) == int and
                input_hundred < 1000), "Invalid Hundred input"

        if input_hundred in UNITS and lang_code in UNITS[input_hundred]:
            return [UNITS[input_hundred][lang_code]]

        res = []

        hundreds_value = (input_hundred / 100) * 100
        if hundreds_value:
            res.append(HUNDREDS[hundreds_value][lang_code])
            input_hundred -= hundreds_value
            if not input_hundred:
                return res

        if input_hundred in UNITS and lang_code in UNITS[input_hundred]:
            # values <= 30 or X0
            res.append(UNITS[input_hundred][lang_code])
            return res

        # XY; X >= 3 and y != 0
        tens_value = (input_hundred / 10) * 10
        units_value = input_hundred - tens_value
        if TENS_UNITS_SEP and lang_code in TENS_UNITS_SEP:
            res.append(TENS[tens_value][lang_code] + TENS_UNITS_SEP[lang_code]
                + UNITS[units_value][lang_code])
        else:
            res.append(TENS[tens_value][lang_code])
            res.append(UNITS[units_value][lang_code])

        return res

    converted = []
    if million:
        if million == 1:
            converted.append(UNITS[1000000][lang_code])
        else:
            converted += __convert_hundreds(million)
            converted.append(GREATER[1000000][lang_code])

        input_int -= million * 1000000

    if thousands:
        if thousands == 1:
            converted.append(UNITS[1000][lang_code])
        else:
            converted += __convert_hundreds(thousands)
            converted.append(GREATER[1000][lang_code])

    if hundreds:
        # exactly 100 is already contempleted
        converted += __convert_hundreds(hundreds)
    return u" ".join(converted)


def number_to_literal(
        input_number, lang_code, rounding=0.01, is_currency=True):
    assert lang_code and lang_code in SUPPORTED_LANGS, (
        "The Language Code "
        "is not supported. The suported languages are: %s"
        % ", ".join(SUPPORTED_LANGS[:-1]) + " and " +
        SUPPORTED_LANGS[-1])

    PREC = Decimal(str(rounding))

    input_number = Decimal(str(input_number)).quantize(PREC)

    number_int = int(math.floor(input_number))
    decimals = int((input_number - number_int) * (1 / PREC))

    res = []
    res.append(integer_to_literal(number_int, lang_code))

    if is_currency:
        if (number_int in CURRENCY_INTEGER_NAME and
                lang_code in CURRENCY_INTEGER_NAME[number_int]):
            res.append(CURRENCY_INTEGER_NAME[number_int][lang_code])
        else:
            res.append(CURRENCY_INTEGER_NAME[2][lang_code])

        if decimals:
            res.append(CURRENCY_DECIMALS_SEP[lang_code])
    elif decimals:
        res.append(NOT_CURRENCY_DECIMALS_SEP[lang_code])

    if decimals:
        res.append(integer_to_literal(decimals, lang_code))
        if is_currency:
            if (decimals in CURRENCY_DECIMALS_NAME and
                    lang_code in CURRENCY_DECIMALS_NAME[decimals]):
                res.append(CURRENCY_DECIMALS_NAME[decimals][lang_code])
            else:
                res.append(CURRENCY_DECIMALS_NAME[2][lang_code])

    return " ".join(res)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
