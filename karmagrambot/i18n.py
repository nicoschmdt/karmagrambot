import gettext
from .config import LANGUAGE

language = gettext.translation('base', localedir='locale', languages=[LANGUAGE]) # ver como pegar a linguagem do config
language.install()
_tr = language.gettext

