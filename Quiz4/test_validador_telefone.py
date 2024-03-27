from validador_telefone import validar_telefone

def test_telefone_valido_com_ddd():
    assert validar_telefone("(11) 98765-4321") == True

def test_telefone_valido_sem_ddd():
    assert validar_telefone("98765-4321") == True

def test_telefone_invalido_caracteres_especiais():
    assert validar_telefone("(11) 9@765-4321") == False

def test_telefone_invalido_tamanho():
    assert validar_telefone("(11) 987654321") == False

def test_telefone_invalido_ddd_invalido():
    assert validar_telefone("(00) 98765-4321") == False