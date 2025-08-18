# Gerador de Senhas Seguras

Este projeto é um gerador de senhas seguras desenvolvido em Python utilizando a biblioteca **CustomTkinter** para a interface gráfica. O aplicativo oferece uma interface moderna e intuitiva, com suporte a temas claro e escuro, além de opções personalizáveis para a criação de senhas fortes.

## Funcionalidades

- Geração de senhas com comprimento configurável.  
- Inclusão opcional de letras maiúsculas, minúsculas, números e símbolos.  
- Avaliação da força da senha gerada com feedback visual.  
- Contador de senhas geradas e exibição da data/hora da geração.  
- Botões para copiar a senha para a área de transferência ou salvar em arquivo.  
- Alternância dinâmica entre tema claro e escuro via switch.  

## Tecnologias Utilizadas

- Python 3.x  
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) para interface gráfica moderna e responsiva  
- Biblioteca padrão do Python para manipulação de strings, expressões regulares e data/hora  

## Como Usar

1. Clone este repositório:

```bash
git clone https://github.com/Br-Gui/Gerador-de-senha.git
```

2. Instale as dependências:

```bash
pip install customtkinter pillow
```

3. Execute o script principal:

```bash
python gerador_senhas.py
```

4. Na interface:
   - Configure o comprimento da senha e selecione os tipos de caracteres desejados.  
   - Clique em **"Gerar Senha"** para criar uma senha segura.  
   - Use os botões para **copiar** ou **salvar** a senha gerada.  
   - Utilize o switch no canto superior direito para **alternar entre os temas claro e escuro**.  

## Estrutura do Código

- **`GeradorSenhaApp`**: Classe principal que gerencia a interface e a lógica do gerador.  
- Métodos para **geração de senha**, **validação da força**, **cópia** e **salvamento**.  
- Uso de variáveis `Tkinter` para controle dos estados dos checkboxes e campos.  

## Imagens

<img width="521" height="596" alt="478150230-148a8807-9588-4d66-933b-f2ea335d9a33" src="https://github.com/user-attachments/assets/2671f0ef-f59a-4141-afeb-9741fc255f69" />
<img width="516" height="595" alt="478150024-6e46c833-66f6-479c-9d89-26f8727e1726" src="https://github.com/user-attachments/assets/ac4b9a46-f442-4829-a71f-8fe14cf104fa" />

## Testes

O projeto conta com testes automatizados utilizando **pytest**.  

### Rodando os testes

1. Instale o pytest (se ainda não tiver):  
   ```bash
   pip install pytest
   ```
2. Na raiz do projeto, execute:  
   ```bash
   pytest -v
   ```

### O que é testado

- **Comprimento da senha**  
  Garante que a senha gerada tem exatamente o tamanho especificado.  

- **Tipos de caracteres**  
  Verifica se a senha contém **maiúsculas, minúsculas, números e símbolos** quando todas as opções estão ativadas.  

- **Validação da força**  
  Testa se a senha é classificada corretamente como **Fraca**, **Média** ou **Forte**.  

- **Limite de texto**  
  Confere se textos longos são truncados corretamente com `...`.  

### Como modificar os testes

Você pode adaptar os testes conforme sua necessidade:  

- **Mudar o tamanho da senha testada**  
  No teste `test_gerar_senha_tamanho`, o intervalo padrão é de 4 a 39 caracteres:  
  ```python
  @pytest.mark.parametrize("tamanho", range(4, 40))
  ```
  Se quiser testar apenas senhas curtas, altere para:  
  ```python
  @pytest.mark.parametrize("tamanho", range(4, 10))
  ```

- **Remover a verificação de caracteres especiais**  
  No teste `test_gerar_senha_tipos_caracteres`, atualmente todos os tipos são verificados:  
  ```python
  assert any(not c.isalnum() for c in senha), "Não gerou símbolo"
  ```
  Se você não quiser exigir símbolos, basta **comentar ou remover** essa linha.  

- **Testar apenas um tipo de caractere**  
  Você pode desligar opções no app antes de gerar a senha:  
  ```python
  app.incluir_maiusculas.set(True)
  app.incluir_minusculas.set(False)
  app.incluir_numeros.set(False)
  app.incluir_simbolos.set(False)
  senha = app.gerar_senha(20)
  assert all(c.isupper() for c in senha)
  ```

Isso dá liberdade para personalizar os testes de acordo com a política de senhas que você deseja validar.  
