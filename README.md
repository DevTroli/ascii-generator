# 🎨 AsciiArt Generator CLI
> *Transforme textos e imagens em belas artes ASCII para seu terminal e documentos*

## 🚀 Visão Geral

O **AsciiArt Generator** é uma ferramenta de linha de comando (CLI) desenvolvida em Python que permite transformar textos e imagens em arte ASCII. Ideal para desenvolvedores que desejam adicionar um toque visual criativo em documentações, banners de terminal, ou até mesmo em interfaces textuais.

A arte ASCII utiliza caracteres para criar representações visuais, transformando simples textos em elementos gráficos expressivos. Este projeto foi pensado para ser versátil e otimizado, oferecendo diferentes estilos e configurações que se adaptam a diversas necessidades.

```
 █████╗ ███████╗ ██████╗██╗██╗  █████╗ ██████╗ ████████╗
██╔══██╗██╔════╝██╔════╝██║██║ ██╔══██╗██╔══██╗╚══██╔══╝
███████║███████╗██║     ██║██║ ███████║██████╔╝   ██║   
██╔══██║╚════██║██║     ██║██║ ██╔══██║██╔══██╗   ██║   
██║  ██║███████║╚██████╗██║██║ ██║  ██║██║  ██║   ██║   
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
```

## ✨ Funcionalidades

- 🔤 **Transformação de texto em arte ASCII** com múltiplos estilos
- 🖼️ **Conversão de imagens em representações ASCII** com ajustes de contraste e brilho
- 📝 **Geração de banners para documentação** com títulos e subtítulos personalizados
- 🌐 **Suporte para imagens locais e URLs** com cache inteligente
- 💾 **Exportação em formatos de texto e HTML**
- 🧩 **Diferentes densidades e estilos visuais** para imagens
- 🔄 **Cache automático** para otimização de desempenho

## 📋 Pré-requisitos

- Python 3.6 ou superior

## 🔧 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/DevTroli/ascii-generator.git
   cd ascii-generator
   ```

2. Sem dependências externas! 🎉 O projeto usa apenas bibliotecas padrão do Python.

> 💡 **Dica:** Recomendamos a criação de um ambiente virtual antes da instalação das dependências.

## 🎮 Uso

### 📝 Modo Texto

Para converter um texto simples em arte ASCII:

```bash
python asciiart.py -t "Olá Mundo" -s block
```

### 🖼️ Modo Imagem

Para converter uma imagem em arte ASCII:

```bash
python asciiart.py -i caminho/para/imagem.jpg --width 80 --style-img default
```

Ou usando uma URL:

```bash
python asciiart.py -i https://exemplo.com/imagem.jpg --compact
```

### 📚 Modo Documentação

Para criar um banner estilizado para documentação:

```bash
python asciiart.py --doc --title "Projeto X" --subtitle "Uma ferramenta incrível para análise de dados" --style fancy
```

## 🌈 Exemplos

**Texto em estilo block:**
```
python asciiart.py -t "ASCII" -s block
```

Resultado:
```
  █████   ██████   ██████  ██  ██  
 ██   ██ ██       ██       ██  ██  
 ███████ ███████  ██       ██████  
 ██   ██      ██  ██       ██  ██  
 ██   ██ ██████    ██████  ██  ██  
```

**Imagem com ajuste de contraste:**
```
python asciiart.py -i logo.png --contrast 1.5 --style-img detailed
```

**Banner para documentação:**
```
python asciiart.py --doc --title "DevTools" --subtitle "Suite de ferramentas para desenvolvedores" --banner-width 60
```

## 🛠️ Opções e Parâmetros

### Opções Gerais
- `-t, --text`: Texto para conversão
- `-i, --image`: Caminho ou URL da imagem
- `-o, --output`: Arquivo de saída
- `--html`: Exportar como HTML

### Opções de Texto
- `-s, --style`: Estilo do texto (opções: `block`, `classic`, `fancy`)

### Opções de Imagem
- `--width`: Largura da saída em caracteres
- `--style-img`: Estilo de caracteres para imagens (opções: `default`, `blocks`, `detailed`, `inverse`, `minimal`, `matrix`, `dots`)
- `--contrast`: Ajuste de contraste (valores entre 0.1 e 3.0)
- `--brightness`: Ajuste de brilho (valores entre 0.1 e 3.0)
- `--compact`: Modo compacto para terminais

### Opções de Documentação
- `--doc`: Ativa o modo documentação
- `--title`: Título para o banner
- `--subtitle`: Subtítulo para o banner
- `--banner-width`: Largura do banner em caracteres


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

## 👥 Contribuições

Contribuições são bem-vindas! Se você tem ideias para melhorar este projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

---

⌨️ com ❤️ por @DevTroli 😊
