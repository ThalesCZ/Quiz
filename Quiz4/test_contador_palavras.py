from contador_palavras import contar_palavras

def test_contar_palavras_texto_vazio():
    assert contar_palavras("") == 0

def test_contar_palavras_uma_palavra():
    assert contar_palavras("Olá") == 1

def test_contar_palavras_multipalavras():
    assert contar_palavras("Isso é um teste") == 4

def test_contar_palavras_multipalavras_com_espacos_extras():
    assert contar_palavras("   Isso  é um  teste    ") == 4

def test_contar_palavras_pontuacao():
    assert contar_palavras("Isso é um teste.") == 4

def test_contar_palavras_caracteres_especiais():
    assert contar_palavras("Isso é um teste, não é?") == 6
