import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from gerador_senhas import GeradorSenhaApp

@pytest.fixture
def app():
    return GeradorSenhaApp()

@pytest.mark.parametrize("tamanho", range(4, 40))
def test_gerar_senha_tamanho(app, tamanho):
    senha = app.gerar_senha(tamanho)
    assert len(senha) == tamanho

def test_gerar_senha_tipos_caracteres(app):
    app.incluir_maiusculas.set(True)
    app.incluir_minusculas.set(True)
    app.incluir_numeros.set(True)
    app.incluir_simbolos.set(True)
    
    for _ in range(50):
        senha = app.gerar_senha(1000)
        assert any(c.isupper() for c in senha), "Não gerou maiúscula"
        assert any(c.islower() for c in senha), "Não gerou minúscula"
        assert any(c.isdigit() for c in senha), "Não gerou número"
        assert any(not c.isalnum() for c in senha), "Não gerou símbolo"

def test_validar_forca(app):
    forte = app.validar_forca("Abc123!@#xyz")
    media = app.validar_forca("Abc12345")
    fraca = app.validar_forca("abc")
    assert forte[0] == "Forte"
    assert media[0] == "Média"
    assert fraca[0] == "Fraca"

def test_limitar_texto(app):
    texto = "abcdefghijklmno"
    limitado = app.limitar_texto(texto, 10)
    assert limitado == "abcdefg..."
