from validador_emails import validar_email

def test_email_valido():
    assert validar_email("usuario@example.com") == True

def test_email_invalido_caracteres_especiais():
    assert validar_email("usuario@ex#ample.com") == False

def test_email_invalido_sem_arroba():
    assert validar_email("usuarioexample.com") == False

def test_email_invalido_sem_ponto():
    assert validar_email("usuario@examplecom") == False

def test_email_invalido_com_espaco():
    assert validar_email("usuario@example com") == False