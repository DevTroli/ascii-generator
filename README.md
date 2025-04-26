# 🎨 AsciiArt Generator CLI

## 🚀 O Projeto

**AsciiArt Generator** é uma ferramenta de linha de comando que transforma texto simples em banners artísticos ASCII, perfeitos para documentação, terminais, e projetos que precisam de um toque visual especial!

 █████╗ ███████╗ ██████╗██╗██╗  █████╗ ██████╗ ████████╗
██╔══██╗██╔════╝██╔════╝██║██║ ██╔══██╗██╔══██╗╚══██╔══╝
███████║███████╗██║     ██║██║ ███████║██████╔╝   ██║   
██╔══██║╚════██║██║     ██║██║ ██╔══██║██╔══██╗   ██║   
██║  ██║███████║╚██████╗██║██║ ██║  ██║██║  ██║   ██║   
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   

## ✨ Funcionalidades

- 🖌️ **Múltiplos estilos**: Block, Classic e Fancy
- 📄 **Exportação flexível**: Terminal, arquivos de texto e HTML
- 🔄 **Modo biblioteca**: Use como módulo em seus próprios projetos Python
- 💻 **Interface CLI simples**: Intuitiva e fácil de usar
- 🌐 **Suporte a caracteres especiais**: Amplo suporte para símbolos e pontuação

## 📋 Pré-requisitos

- Python 3.6 ou superior

## 🔧 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/DevTroli/ascii-generator.git
   cd ascii-generator
   ```

2. Sem dependências externas! 🎉 O projeto usa apenas bibliotecas padrão do Python.

## 🎮 Uso

### Como ferramenta de linha de comando

```bash
# Gerar arte básica
python asciiArt.py -t "Hello World"

# Escolher um estilo específico
python asciiArt.py -t "ASCII ART" -s fancy

# Salvar em um arquivo de texto
python asciiArt.py -t "BANNER" -s block -o banner.txt

# Exportar como HTML
python asciiArt.py -t "WEB BANNER" -s fancy --html banner.html

# Listar todos os estilos disponíveis
python asciiArt.py --list-styles
```

### Como biblioteca em seu código

```python
from asciiArt import generate_art, save_to_file, export_html

# Gerar arte ASCII
banner = generate_art("Meu Projeto", "block")
print(banner)

# Salvar em arquivo
save_to_file(banner, "banner_projeto.txt")

# Exportar como HTML
export_html(banner, "banner_projeto.html", "Banner do Meu Projeto")
```

## 📊 Estrutura do Projeto

```
ascii-generator/
├── asciiArt.py         # Script principal e biblioteca 
├── exemplo.py          # Exemplo de uso como módulo
├── test_asciiArt.py    # Testes unitários
├── README.md           # Esta documentação
└── banners/            # Pasta criada para armazenar banners de exemplo
```

## 🧪 Testes

Execute os testes unitários para verificar se tudo está funcionando corretamente:

```bash
python test_asciiArt.py
```

## 🛠️ Arquitetura e Decisões Técnicas

### Princípios de Design

O projeto foi construído seguindo alguns princípios importantes:

1. **KISS (Keep It Simple, Stupid)**: Mantemos o código simples e direto, sem dependências externas.
2. **DRY (Don't Repeat Yourself)**: Reutilizamos código através de funções bem definidas.
3. **Modularidade**: O código pode ser usado como ferramenta CLI ou como biblioteca.
4. **Extensibilidade**: Novos estilos podem ser facilmente adicionados ao dicionário `STYLES`.

### Estrutura de Dados

A escolha de usar dicionários para armazenar os estilos facilita:
- Acesso rápido O(1) para cada caractere
- Extensibilidade (adicionar novos estilos é simples)
- Legibilidade do código

### Algoritmo de Geração

O algoritmo de geração é elegante em sua simplicidade:

1. Cada caractere no texto de entrada é convertido para seu equivalente ASCII art
2. As linhas correspondentes são concatenadas horizontalmente
3. O resultado final é a junção vertical dessas linhas

Este approach é eficiente e fácil de entender, pois:
- A complexidade é O(n), onde n é o tamanho do texto de entrada
- A memória utilizada é proporcional ao tamanho da saída
- O código é determinístico e previsível

## 🧠 Jornada de Desenvolvimento: Soft Skills & Engenharia

### 🔍 Identificação do Problema

Todo projeto começa com um problema a ser resolvido. No caso do AsciiArt Generator, o problema era: "Como adicionar elementos visuais interessantes a interfaces de texto e documentação via CLI?"

### 🤔 Pensamento Analítico e Solução de Problemas

Desenvolver esta ferramenta exigiu:

1. **Decomposição do problema**: Dividimos a tarefa em partes menores:
   - Como representar caracteres em ASCII art?
   - Como juntar esses caracteres para formar palavras?
   - Como disponibilizar diferentes estilos?

2. **Abstração**: Criamos representações simples para conceitos complexos:
   - Um caractere ASCII art é uma lista de linhas
   - Um estilo é um dicionário de caracteres
   - Um banner é uma concatenação horizontal e vertical

### 🎯 Pragmatismo e Foco

Em vez de criar um sistema complexo com infinitas possibilidades, escolhemos um escopo bem definido:
- Três estilos distintos
- Conjunto essencial de caracteres
- Interface minimalista, mas completa

### 📚 Aprendizados para Iniciantes

Se você está começando em desenvolvimento:

1. **Estruturas de dados importam**: A escolha de usar dicionários foi fundamental para a clareza do código.
2. **CLI é poderosa**: Interfaces de linha de comando são eficientes e versáteis.
3. **Testes são essenciais**: Escrever testes ajuda a garantir que tudo funcione corretamente.
4. **Documentação clara**: Um bom README faz toda a diferença para quem vai usar seu código.
5. **KISS**: Nem sempre mais complexo significa melhor.

### 🌱 Crescimento e Próximos Passos

Para evoluir este projeto, considere:
- Adicionar mais estilos artísticos
- Implementar cores para terminal
- Criar uma interface web simples
- Adicionar suporte para caracteres Unicode mais amplos

## 📝 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

## 🙏 Agradecimentos

- Comunidade de ASCII que mantém viva esta forma de arte
- Todos os desenvolvedores que valorizam interfaces de terminal e documentação bem formatada

---

⌨️ com ❤️ por @DevTroli 😊
