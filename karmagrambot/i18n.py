import gettext
import locale
from .config import LANGUAGE
from babel.numbers import format_decimal

locale.setlocale(locale.LC_TIME, LANGUAGE)

language = gettext.translation('base', localedir='locale', languages=[LANGUAGE]) # ver como pegar a linguagem do config
language.install()
_tr = language.gettext

def _n(number):
    format_decimal(number, locale=LANGUAGE)
