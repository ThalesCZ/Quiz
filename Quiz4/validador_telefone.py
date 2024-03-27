
import re

def validar_telefone(telefone):
    padrao = r'^(\([1-9]{2}\) )?[2-9][0-9]{3,4}\-[0-9]{4}$'
    return re.match(padrao, telefone) is not None
