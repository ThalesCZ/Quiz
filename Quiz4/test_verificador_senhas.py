from verificador_senhas import verificar_senha_segura

def test_senha_curta():
    assert verificar_senha_segura("Abcd!23") == False

def test_sem_maiusculas():
    assert verificar_senha_segura("senha123!") == False

def test_sem_minusculas():
    assert verificar_senha_segura("SENHA123!") == False

def test_sem_especiais():
    assert verificar_senha_segura("Senha123") == False

def test_senha_segura():
    assert verificar_senha_segura("Senha@123") == True