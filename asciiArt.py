#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AsciiArt Generator - Um gerador de arte ASCII via linha de comando
Desenvolvido para criar banners de texto artísticos para terminais e documentos
"""

import sys
import argparse
import os
from typing import List, Dict, Tuple, Optional
import json

# Definição dos estilos de caracteres para banners
STYLES = {
    "block": {
        "A": ["  █████  ", " ██   ██ ", "███████ ", "██   ██ ", "██   ██ "],
        "B": ["██████  ", "██   ██ ", "██████  ", "██   ██ ", "██████  "],
        "C": [" ██████ ", "██      ", "██      ", "██      ", " ██████ "],
        "D": ["██████  ", "██   ██ ", "██   ██ ", "██   ██ ", "██████  "],
        "E": ["███████ ", "██      ", "█████   ", "██      ", "███████ "],
        "F": ["███████ ", "██      ", "█████   ", "██      ", "██      "],
        "G": [" ██████  ", "██       ", "██   ███ ", "██    ██ ", " ██████  "],
        "H": ["██   ██ ", "██   ██ ", "███████ ", "██   ██ ", "██   ██ "],
        "I": ["██ ", "██ ", "██ ", "██ ", "██ "],
        "J": ["     ██ ", "     ██ ", "     ██ ", "██   ██ ", " █████  "],
        "K": ["██   ██ ", "██  ██  ", "█████   ", "██  ██  ", "██   ██ "],
        "L": ["██      ", "██      ", "██      ", "██      ", "███████ "],
        "M": [
            "███    ███ ",
            "████  ████ ",
            "██ ████ ██ ",
            "██  ██  ██ ",
            "██      ██ ",
        ],
        "N": ["███    ██ ", "████   ██ ", "██ ██  ██ ", "██  ██ ██ ", "██   ████ "],
        "O": [" ██████  ", "██    ██ ", "██    ██ ", "██    ██ ", " ██████  "],
        "P": ["██████  ", "██   ██ ", "██████  ", "██      ", "██      "],
        "Q": [" ██████  ", "██    ██ ", "██    ██ ", "██  ▄ ██ ", " ██████  "],
        "R": ["██████  ", "██   ██ ", "██████  ", "██   ██ ", "██   ██ "],
        "S": [" ██████  ", "██       ", " ██████  ", "      ██ ", " ██████  "],
        "T": ["████████ ", "   ██    ", "   ██    ", "   ██    ", "   ██    "],
        "U": ["██    ██ ", "██    ██ ", "██    ██ ", "██    ██ ", " ██████  "],
        "V": ["██    ██ ", "██    ██ ", "██    ██ ", " ██  ██  ", "  ████   "],
        "W": ["██     ██ ", "██     ██ ", "██  █  ██ ", "██ ███ ██ ", " ███ ███  "],
        "X": ["██   ██ ", " ██ ██  ", "  ███   ", " ██ ██  ", "██   ██ "],
        "Y": ["██    ██ ", " ██  ██  ", "  ████   ", "   ██    ", "   ██    "],
        "Z": ["███████ ", "    ██  ", "   ██   ", " ██     ", "███████ "],
        "0": [
            " ██████  ",
            "██  ████ ",
            "██ ██ ██ ",
            "████  ██ ",
            " ██████  ",
        ],
        "1": [
            "  ██  ",
            " ███  ",
            "  ██  ",
            "  ██  ",
            "████  ",
        ],
        "2": [
            " ██████  ",
            "██    ██ ",
            "    ███  ",
            " ███     ",
            "███████  ",
        ],
        "3": [
            " ██████  ",
            "      ██ ",
            " ██████  ",
            "      ██ ",
            " ██████  ",
        ],
        "4": [
            "██   ██ ",
            "██   ██ ",
            "███████ ",
            "     ██ ",
            "     ██ ",
        ],
        "5": [
            "███████ ",
            "██      ",
            "███████ ",
            "     ██ ",
            "███████ ",
        ],
        "6": [
            " ██████  ",
            "██       ",
            "███████  ",
            "██    ██ ",
            " ██████  ",
        ],
        "7": [
            "███████ ",
            "    ██  ",
            "   ██   ",
            "  ██    ",
            " ██     ",
        ],
        "8": [
            " ██████  ",
            "██    ██ ",
            " ██████  ",
            "██    ██ ",
            " ██████  ",
        ],
        "9": [
            " ██████  ",
            "██    ██ ",
            " ███████ ",
            "      ██ ",
            " ██████  ",
        ],
        " ": [
            "    ",
            "    ",
            "    ",
            "    ",
            "    ",
        ],
        ".": [
            "    ",
            "    ",
            "    ",
            "    ",
            " ██ ",
        ],
        ",": [
            "    ",
            "    ",
            "    ",
            " ██ ",
            "██  ",
        ],
        "!": [
            "██ ",
            "██ ",
            "██ ",
            "   ",
            "██ ",
        ],
        "?": [
            " ████  ",
            "██  ██ ",
            "   ██  ",
            "       ",
            "   ██  ",
        ],
        "-": [
            "       ",
            "       ",
            "█████  ",
            "       ",
            "       ",
        ],
        "_": [
            "        ",
            "        ",
            "        ",
            "        ",
            "██████  ",
        ],
        "&": [
            " ███    ",
            "██ ██   ",
            " ████ ██",
            "██  ██  ",
            " ███ ██ ",
        ],
        "/": [
            "     ██ ",
            "    ██  ",
            "   ██   ",
            "  ██    ",
            " ██     ",
        ],
        "\\": [
            "██      ",
            " ██     ",
            "  ██    ",
            "   ██   ",
            "    ██  ",
        ],
        "@": [
            " ██████  ",
            "██    ██ ",
            "██ ██ ██ ",
            "██ ██ ██ ",
            " ███████ ",
        ],
        "#": [
            " ██  ██  ",
            "████████ ",
            " ██  ██  ",
            "████████ ",
            " ██  ██  ",
        ],
        "$": [
            " ██████  ",
            "██ ██    ",
            " ██████  ",
            "    ██ ██",
            " ██████  ",
        ],
        "%": [
            "███   ██ ",
            "███  ██  ",
            "    ██   ",
            "   ██    ",
            "  ██     ",
        ],
        "^": [
            "  ██    ",
            " ████   ",
            "██  ██  ",
            "        ",
            "        ",
        ],
        "*": [
            "   ██    ",
            " ██████  ",
            "   ██    ",
            "  ████   ",
            " ██  ██  ",
        ],
        "(": [
            "  ██ ",
            " ██  ",
            " ██  ",
            " ██  ",
            "  ██ ",
        ],
        ")": [
            " ██  ",
            "  ██ ",
            "  ██ ",
            "  ██ ",
            " ██  ",
        ],
        "[": [
            "████ ",
            "██   ",
            "██   ",
            "██   ",
            "████ ",
        ],
        "]": [
            "████ ",
            "   ██",
            "   ██",
            "   ██",
            "████ ",
        ],
        "{": [
            "  ███",
            " ██  ",
            "███  ",
            " ██  ",
            "  ███",
        ],
        "}": [
            "███  ",
            "  ██ ",
            "  ███",
            "  ██ ",
            "███  ",
        ],
        ":": [
            "    ",
            " ██ ",
            "    ",
            " ██ ",
            "    ",
        ],
        ";": [
            "    ",
            " ██ ",
            "    ",
            " ██ ",
            "██  ",
        ],
        '"': [
            "██ ██ ",
            "██ ██ ",
            "      ",
            "      ",
            "      ",
        ],
        "'": [
            " ██ ",
            " ██ ",
            "    ",
            "    ",
            "    ",
        ],
        "`": [
            "██   ",
            " ██  ",
            "     ",
            "     ",
            "     ",
        ],
        "~": [
            "      ",
            " ██ ██",
            "██ ██ ",
            "      ",
            "      ",
        ],
        "+": [
            "       ",
            "  ██   ",
            "██████ ",
            "  ██   ",
            "       ",
        ],
        "=": [
            "       ",
            "██████ ",
            "       ",
            "██████ ",
            "       ",
        ],
    },
    "classic": {
        "A": ["   A   ", "  A A  ", " AAAAA ", "A     A", "A     A"],
        "B": ["BBBB  ", "B   B ", "BBBB  ", "B   B ", "BBBB  "],
        "C": [" CCC ", "C    ", "C    ", "C    ", " CCC "],
        "D": ["DDDD  ", "D   D ", "D   D ", "D   D ", "DDDD  "],
        "E": ["EEEEE", "E    ", "EEE  ", "E    ", "EEEEE"],
        "F": ["FFFFF", "F    ", "FFF  ", "F    ", "F    "],
        "G": [" GGG  ", "G     ", "G  GG ", "G   G ", " GGG  "],
        "H": ["H   H", "H   H", "HHHHH", "H   H", "H   H"],
        "I": ["III", " I ", " I ", " I ", "III"],
        "J": ["    J", "    J", "    J", "J   J", " JJJ "],
        "K": ["K   K", "K  K ", "KKK  ", "K  K ", "K   K"],
        "L": ["L    ", "L    ", "L    ", "L    ", "LLLLL"],
        "M": ["M     M", "MM   MM", "M M M M", "M  M  M", "M     M"],
        "N": ["N    N", "NN   N", "N N  N", "N  N N", "N   NN"],
        "O": [" OOO ", "O   O", "O   O", "O   O", " OOO "],
        "P": ["PPPP ", "P   P", "PPPP ", "P    ", "P    "],
        "Q": [" QQQ  ", "Q   Q ", "Q   Q ", "Q  Q  ", " QQ Q "],
        "R": ["RRRR ", "R   R", "RRRR ", "R  R ", "R   R"],
        "S": [" SSS ", "S    ", " SSS ", "    S", "SSSS "],
        "T": ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  "],
        "U": ["U   U", "U   U", "U   U", "U   U", " UUU "],
        "V": ["V     V", "V     V", " V   V ", "  V V  ", "   V   "],
        "W": ["W     W", "W     W", "W  W  W", "W W W W", " W   W "],
        "X": ["X   X", " X X ", "  X  ", " X X ", "X   X"],
        "Y": ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "],
        "Z": ["ZZZZZ", "   Z ", "  Z  ", " Z   ", "ZZZZZ"],
        "0": [" 000 ", "0   0", "0   0", "0   0", " 000 "],
        "1": ["  1  ", " 11  ", "  1  ", "  1  ", " 111 "],
        "2": [" 222 ", "2   2", "   2 ", "  2  ", "22222"],
        "3": ["3333 ", "    3", " 333 ", "    3", "3333 "],
        "4": ["4  4 ", "4  4 ", "44444", "   4 ", "   4 "],
        "5": ["55555", "5    ", "5555 ", "    5", "5555 "],
        "6": [" 666 ", "6    ", "6666 ", "6   6", " 666 "],
        "7": ["77777", "   7 ", "  7  ", " 7   ", "7    "],
        "8": [" 888 ", "8   8", " 888 ", "8   8", " 888 "],
        "9": [" 999 ", "9   9", " 9999", "    9", " 999 "],
        " ": ["    ", "    ", "    ", "    ", "    "],
        ".": ["   ", "   ", "   ", "   ", " . "],
        ",": ["   ", "   ", "   ", " , ", ",  "],
        "!": [" ! ", " ! ", " ! ", "   ", " ! "],
        "?": [" ?? ", "?  ?", "  ? ", "    ", "  ? "],
        "-": ["     ", "     ", "-----", "     ", "     "],
        "_": ["     ", "     ", "     ", "     ", "_____"],
        "&": [" &   ", "&  & ", " &&& ", "&  & ", " && &"],
        "/": ["    /", "   / ", "  /  ", " /   ", "/    "],
        "\\": ["\\    ", " \\   ", "  \\  ", "   \\ ", "    \\"],
        "@": [" @@@ ", "@   @", "@ @ @", "@  @ ", " @@@ "],
        "#": [" # # ", "#####", " # # ", "#####", " # # "],
        "$": [" $$$ ", "$ $  ", " $$$ ", "  $ $", " $$$ "],
        "%": ["%   %", "   % ", "  %  ", " %   ", "%   %"],
        "^": [" ^  ", "^ ^ ", "    ", "    ", "    "],
        "*": ["     ", " * * ", "  *  ", " * * ", "     "],
        "(": ["  (", " ( ", " ( ", " ( ", "  ("],
        ")": [")  ", " ) ", " ) ", " ) ", ")  "],
        "[": ["[[", "[ ", "[ ", "[ ", "[["],
        "]": ["]]", " ]", " ]", " ]", "]]"],
        "{": [" {{", " { ", "{  ", " { ", " {{"],
        "}": ["}} ", " } ", "  }", " } ", "}} "],
        ":": ["   ", " : ", "   ", " : ", "   "],
        ";": ["   ", " ; ", "   ", " ; ", ";  "],
        '"': ['" "', '" "', "   ", "   ", "   "],
        "'": [" '", " '", "  ", "  ", "  "],
        "`": ["`  ", " ` ", "   ", "   ", "   "],
        "~": ["    ", "~ ~ ", "    ", "    ", "    "],
        "+": ["     ", "  +  ", "+++++", "  +  ", "     "],
        "=": ["     ", "=====", "     ", "=====", "     "],
    },
    "fancy": {
        "A": ["    _    ", "   / \\   ", "  / _ \\  ", " / ___ \\ ", "/_/   \\_\\"],
        "B": [" ____  ", "| __ ) ", "|  _ \\ ", "| |_) |", "|____/ "],
        "C": ["  ____ ", " / ___|", "| |    ", "| |___ ", " \\____|"],
        "D": [" ____  ", "|  _ \\ ", "| | | |", "| |_| |", "|____/ "],
        "E": [" _____ ", "| ____|", "|  _|  ", "| |___ ", "|_____|"],
        "F": [" _____ ", "|  ___|", "| |_   ", "|  _|  ", "|_|    "],
        "G": ["  ____ ", " / ___|", "| |  _ ", "| |_| |", " \\____|"],
        "H": [" _   _ ", "| | | |", "| |_| |", "|  _  |", "|_| |_|"],
        "I": [" ___ ", "|_ _|", " | | ", " | | ", "|___|"],
        "J": ["     _ ", "    | |", " _  | |", "| |_| |", " \\___/ "],
        "K": [" _  __", "| |/ /", "| ' / ", "| . \\ ", "|_|\\_\\"],
        "L": [" _     ", "| |    ", "| |    ", "| |___ ", "|_____|"],
        "M": [" __  __ ", "|  \\/  |", "| |\\/| |", "| |  | |", "|_|  |_|"],
        "N": [" _   _ ", "| \\ | |", "|  \\| |", "| |\\  |", "|_| \\_|"],
        "O": ["  ___  ", " / _ \\ ", "| | | |", "| |_| |", " \\___/ "],
        "P": [" ____  ", "|  _ \\ ", "| |_) |", "|  __/ ", "|_|    "],
        "Q": ["  ___  ", " / _ \\ ", "| | | |", "| |_| |", " \\__\\_\\"],
        "R": [" ____  ", "|  _ \\ ", "| |_) |", "|  _ < ", "|_| \\_\\"],
        "S": [" ____  ", "/ ___| ", "\\___ \\ ", " ___) |", "|____/ "],
        "T": [" _____ ", "|_   _|", "  | |  ", "  | |  ", "  |_|  "],
        "U": [" _   _ ", "| | | |", "| | | |", "| |_| |", " \\___/ "],
        "V": ["__     __", "\\ \\   / /", " \\ \\ / / ", "  \\ V /  ", "   \\_/   "],
        "W": [
            "__        __",
            "\\ \\      / /",
            " \\ \\ /\\ / / ",
            "  \\ V  V /  ",
            "   \\_/\\_/   ",
        ],
        "X": ["__  __", "\\ \\/ /", " \\  / ", " /  \\ ", "/_/\\_\\"],
        "Y": ["__   __", "\\ \\ / /", " \\ V / ", "  | |  ", "  |_|  "],
        "Z": [" _____", "|__  /", "  / / ", " / /_ ", "/____|"],
        "0": ["  ___  ", " / _ \\ ", "| | | |", "| |_| |", " \\___/ "],
        "1": [" _ ", "/ |", "| |", "| |", "|_|"],
        "2": [" ____  ", "|___ \\ ", "  __) |", " / __/ ", "|_____|"],
        "3": [" _____ ", "|___ / ", "  |_ \\ ", " ___) |", "|____/ "],
        "4": [" _  _   ", "| || |  ", "| || |_ ", "|__   _|", "   |_|  "],
        "5": [" ____  ", "| ___| ", "|___ \\ ", " ___) |", "|____/ "],
        "6": ["  __   ", " / /_  ", "| '_ \\ ", "| (_) |", " \\___/ "],
        "7": [" _____ ", "|___  |", "   / / ", "  / /  ", " /_/   "],
        "8": ["  ___  ", " ( _ ) ", " / _ \\ ", "| (_) |", " \\___/ "],
        "9": ["  ___  ", " / _ \\ ", "| (_) |", " \\__, |", "   /_/ "],
        " ": ["    ", "    ", "    ", "    ", "    "],
        ".": ["    ", "    ", "    ", " _  ", "(_) "],
        ",": ["    ", "    ", "    ", " _  ", "( ) "],
        "!": [" _ ", "| |", "| |", "|_|", "(_)"],
        "?": [" ___ ", "|__ \\", "  / /", " |_| ", " (_) "],
        "-": ["      ", "      ", " ____ ", "|____|", "      "],
        "_": ["        ", "        ", "        ", "        ", "|______|"],
        "&": ["  ___   ", " ( _ )  ", " / _ \\/\\", "| (_>  <", " \\___/\\/"],
        "/": ["    __", "   / /", "  / / ", " / /  ", "/_/   "],
        "\\": ["__    ", "\\ \\   ", " \\ \\  ", "  \\ \\ ", "   \\_\\"],
        "@": ["   ___  ", "  / _ \\ ", " | | | |", " | |_| |", "  \\___/ "],
        "#": ["  _  _  ", " _|| || ", "|_ || ||", " _||_||_", "|_|  |_|"],
        "": ["  _  ", " | | ", "/ __)", "\\__ \\", "(___/"],
        "%": [" _  __", "(_)/ /", "  / / ", " / /_ ", "/_/(_)"],
        "^": [" /\\ ", "|/\\|", "    ", "    ", "    "],
        "*": ["      ", " __/\\__", " \\    /", " /_  _\\", "   \\/   "],
        "(": ["  __", " / /", "| | ", "| | ", " \\_\\"],
        ")": ["__  ", "\\ \\ ", " | |", " | |", "/_/ "],
        "[": [" __ ", "| _|", "| | ", "| | ", "|__|"],
        "]": [" __ ", "|_ |", " | |", " | |", "|__|"],
        "{": ["  __", " / /", "| | ", " \\ \\", "  \\_\\"],
        "}": ["__  ", "\\ \\ ", " | |", "/ / ", "\\_\\ "],
        ":": ["    ", " _  ", "(_) ", " _  ", "(_) "],
        ";": ["    ", " _  ", "(_) ", " _  ", "/ ) "],
        '"': [" _ _ ", "( | )", " V V ", "     ", "     "],
        "'": [" _ ", "( )", " V ", "   ", "   "],
        "`": [" _ ", "( )", " V ", "   ", "   "],
        "~": ["     ", " /\\/|", "|/\\/ ", "     ", "     "],
        "+": ["      ", "  _   ", " | |  ", "_| |_ ", "\\___/ "],
        "=": ["      ", " ____ ", "|____|", "|____|", "      "],
    },
}


def generate_art(text: str, style: str = "block") -> str:
    """
    Gera arte ASCII para o texto fornecido usando o estilo especificado.

    Args:
        text: O texto para converter em arte ASCII
        style: O estilo da arte (block, classic, ou fancy)

    Returns:
        String contendo a arte ASCII gerada
    """
    if style not in STYLES:
        raise ValueError(
            f"Estilo '{style}' não encontrado. Estilos disponíveis: {', '.join(STYLES.keys())}"
        )

    # Verificar quais caracteres são suportados pelo estilo
    charset = STYLES[style]

    # Converter o texto para maiúsculas para compatibilidade
    text = text.upper()

    # Determinar a altura das letras (assumindo altura consistente em um estilo)
    height = len(next(iter(charset.values())))

    # Inicializar o resultado
    result = [""] * height

    # Gerar a arte
    for char in text:
        if char not in charset:
            char = " "  # Usar espaço para caracteres não suportados

        # Adicionar cada linha do caractere ao resultado
        for i in range(height):
            result[i] += charset[char][i] + " "

    return "\n".join(result)


def save_to_file(art: str, filename: str):
    """
    Salva a arte ASCII em um arquivo.

    Args:
        art: A arte ASCII a ser salva
        filename: O nome do arquivo de saída
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(art)

    print(f"Arte salva em '{filename}'")


def export_html(art: str, filename: str, title: str = "ASCII Art"):
    """
    Exporta a arte ASCII como uma página HTML básica.

    Args:
        art: A arte ASCII a ser exportada
        filename: O nome do arquivo HTML de saída
        title: O título da página HTML
    """
    html_content = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            background-color: #1e1e1e;
            color: #f8f8f8;
            font-family: monospace;
            font-size: 14px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
        }}
        pre {{
            text-align: center;
            white-space: pre;
            background-color: #2d2d2d;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            overflow: auto;
            max-width: 100%;
        }}
        h1 {{
            color: #61dafb;
            margin-bottom: 30px;
        }}
        .footer {{
            margin-top: 20px;
            color: #888;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <pre>{art}</pre>
    <div class="footer">Gerado com AsciiArt Generator</div>
</body>
</html>
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"HTML exportado para '{filename}'")


def list_styles():
    """Lista todos os estilos disponíveis"""
    print("Estilos disponíveis:")
    for style in STYLES.keys():
        print(f"- {style}")


def main():
    """Função principal para processar os argumentos da linha de comando"""
    parser = argparse.ArgumentParser(
        description="Gerador de Arte ASCII - Cria banners de texto artísticos para terminal e documentos",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python asciiArt.py -t "Hello World" 
  python asciiArt.py -t "ASCII ART" -s fancy -o banner.txt
  python asciiArt.py -t "TERMINAL" -s block --html output.html
  python asciiArt.py --list-styles
        """,
    )

    parser.add_argument("-t", "--text", help="Texto para converter em arte ASCII")
    parser.add_argument(
        "-s", "--style", default="block", help="Estilo da arte (block, classic, fancy)"
    )
    parser.add_argument("-o", "--output", help="Arquivo de saída (opcional)")
    parser.add_argument("--html", help="Exportar como arquivo HTML (opcional)")
    parser.add_argument(
        "--list-styles", action="store_true", help="Listar todos os estilos disponíveis"
    )

    args = parser.parse_args()

    if args.list_styles:
        list_styles()
        return

    if not args.text:
        parser.print_help()
        return

    try:
        art = generate_art(args.text, args.style)

        # Sempre mostrar a arte no terminal
        print("\nArte ASCII gerada:\n")
        print(art)
        print()

        # Salvar em arquivo de texto se solicitado
        if args.output:
            save_to_file(art, args.output)

        # Exportar como HTML se solicitado
        if args.html:
            export_html(art, args.html, f"ASCII Art: {args.text}")

    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()
