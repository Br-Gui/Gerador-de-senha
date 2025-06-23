# Gerador de Senhas Seguras

Este projeto é um gerador de senhas seguras desenvolvido em Python utilizando a biblioteca CustomTkinter para a interface gráfica. O aplicativo oferece uma interface moderna e intuitiva, com suporte a temas claro e escuro, além de opções personalizáveis para a criação de senhas fortes.

## Funcionalidades

- Geração de senhas com comprimento configurável.
- Inclusão opcional de letras maiúsculas, minúsculas, números e símbolos.
- Avaliação da força da senha gerada com feedback visual.
- Contador de senhas geradas e exibição da data/hora da geração.
- Botões para copiar a senha para a área de transferência e salvar em arquivo.
- Alternância dinâmica entre tema claro e escuro via switch.

## Tecnologias Utilizadas

- Python 3.x
- CustomTkinter para interface gráfica moderna e responsiva
- Biblioteca padrão do Python para manipulação de strings, expressões regulares e data/hora

## Como Usar

1. Clone este repositório:

```

git clone <https://github.com/Br-Gui/Gerador-de-senha.git>

```

2. Instale as dependências:

```

pip install customtkinter pillow

```

3. Execute o script principal:

```

python gerador_senhas.py

```

4. Na interface, configure o comprimento da senha e selecione os tipos de caracteres desejados.
5. Clique em "Gerar Senha" para criar uma senha segura.
6. Use os botões para copiar ou salvar a senha gerada.
7. Utilize o switch no canto superior direito para alternar entre os temas claro e escuro.

## Estrutura do Código

- `GeradorSenhaApp`: Classe principal que gerencia a interface e a lógica do gerador.
- Métodos para geração de senha, validação da força, cópia e salvamento.
- Uso de variáveis Tkinter para controle dos estados dos checkboxes e campos.

