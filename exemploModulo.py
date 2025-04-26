#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exemplo de como usar asciiArt.py como um módulo
"""

import os
from asciiArt import generate_art, save_to_file, export_html


def main():
    # Gerar banner para um projeto
    projeto_banner = generate_art("PROJETO INCRÍVEL", "block")
    print(projeto_banner)

    # Gerar um título para documentação
    doc_title = generate_art("DOCUMENTAÇÃO", "fancy")
    print("\n" + doc_title)

    # Gerar um banner para terminal
    terminal_banner = generate_art("TERMINAL PRO", "classic")
    print("\n" + terminal_banner)

    # Salvar para um arquivo
    output_dir = "banners"

    # Criar diretório se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Salvar os banners em arquivos
    save_to_file(projeto_banner, os.path.join(output_dir, "projeto.txt"))
    save_to_file(doc_title, os.path.join(output_dir, "documentacao.txt"))

    # Exportar como HTML
    export_html(
        terminal_banner,
        os.path.join(output_dir, "terminal.html"),
        "Banner Terminal Pro",
    )

    print("\nTodos os exemplos foram gerados com sucesso!")


if __name__ == "__main__":
    main()
