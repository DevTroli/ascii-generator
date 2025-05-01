#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AsciiArt Generator - Gerador de arte ASCII para terminais e documentos
Suporta integração de texto e imagens com múltiplos estilos e otimizações de performance
"""

import sys
import argparse
import os
import time
from typing import List, Dict, Tuple, Optional
import json
from PIL import Image, ImageEnhance, ImageOps
import requests
from io import BytesIO
import hashlib
import tempfile
import shutil

# ==================== CONFIGURAÇÕES E CONSTANTES ====================

CACHE_DIR = os.path.join(tempfile.gettempdir(), "asciiart_cache")
os.makedirs(CACHE_DIR, exist_ok=True)

CACHE_EXPIRATION = 86400  # 1 dia em segundos
ASPECT_CORRECTION = 0.55

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

# Enhanced character sets for different visual densities
IMAGE_STYLES = {
    "default": " .:-=+*#%@",
    "blocks": " ░▒▓█",
    "detailed": " .'`^\",:;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$",
    "inverse": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ",
    "minimal": " .:ox%#",
    "matrix": " .:-=+*#%@$",
    "dots": " ⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿"
}

# ==================== FUNÇÕES PRINCIPAIS ====================

def generate_art(text: str, style: str = "block") -> str:
    """
    Gera arte ASCII para texto com verificação robusta de estilos e caracteres.
    
    Args:
        text: Texto a ser convertido
        style: Estilo escolhido (block/classic/fancy)
    
    Returns:
        String com a arte ASCII formatada
    """
    if style not in STYLES:
        raise ValueError(f"Estilo inválido: {style}. Opções: {', '.join(STYLES.keys())}")
    
    charset = STYLES[style]
    text = text.upper()
    height = len(next(iter(charset.values())))
    result = [""] * height

    for char in text:
        char_data = charset.get(char, charset.get(' '))
        for i in range(height):
            result[i] += char_data[i] + " "
    
    return "\n".join(result)

def process_image(
    image_path: str,
    width: int = 40,
    height: Optional[int] = None,
    style: str = "default",
    contrast: float = 1.0,
    brightness: float = 1.0,
    invert: bool = False,
    compact: bool = False,
    optimize_for: str = "terminal"
) -> str:
    """
    Processa imagem para ASCII com tratamento unificado de erros e opções de otimização.
    
    Args:
        image_path: Caminho local ou URL
        width: Largura desejada
        height: Altura desejada (opcional)
        style: Estilo de densidade
        contrast: Ajuste de contraste
        brightness: Ajuste de brilho
        invert: Inverter cores
        compact: Modo compacto
        optimize_for: Destino (terminal/markdown/html)
    
    Returns:
        Arte ASCII da imagem processada
    """
    try:
        img = fetch_image(image_path)
        img = apply_image_adjustments(img, contrast, brightness, invert)
        
        if compact:
            width, height = calculate_compact_dimensions(img, width, optimize_for)
        else:
            width, height = calculate_dimensions(img, width, height)
        
        img = img.resize((width, height), Image.LANCZOS)
        return render_ascii(img, style)
    
    except Exception as e:
        raise ValueError(f"Erro ao processar imagem: {str(e)}")

def generate_doc_banner(title: str, subtitle: str = "", style: str = "block", width: int = 80) -> str:
    """
    Gera um banner estilizado para documentação (README.md etc.)
    
    Args:
        title: Título principal
        subtitle: Subtítulo (opcional)
        style: Estilo ASCII (block/classic/fancy)
        width: Largura máxima do banner
        
    Returns:
        String formatada com o banner ASCII
    """
    # Gerar arte ASCII para o título
    title_art = generate_art(title, style)
    
    # Calcular largura baseada no título ou usar a especificada
    art_width = max(len(line) for line in title_art.split('\n'))
    effective_width = min(art_width, width)
    
    # Criar bordas e separadores
    border = "═" * effective_width
    empty_line = " " * effective_width
    
    # Construir o banner
    banner = []
    banner.append(f"╔{border}╗")
    banner.append(f"║{'DOCUMENTATION BANNER'.center(effective_width)}║")
    banner.append(f"╚{border}╝")
    banner.append(empty_line)
    banner.append(title_art)
    
    if subtitle:
        subtitle_lines = [f"║ {line.ljust(effective_width-4)} ║" 
                         for line in wrap_text(subtitle, effective_width-4)]
        banner.append(empty_line)
        banner.append(f"╔{'═' * (effective_width-2)}╗")
        banner.extend(subtitle_lines)
        banner.append(f"╚{'═' * (effective_width-2)}╝")
    
    return "\n".join(banner)

# ==================== FUNÇÕES DE APOIO ====================

def fetch_image(image_path: str) -> Image.Image:
    """
    Obtém imagem de URL ou arquivo local com cache inteligente e tratamento de erros.
    """
    if image_path.startswith(('http://', 'https://')):
        return fetch_remote_image(image_path)
    return load_local_image(image_path)

def fetch_remote_image(url: str) -> Image.Image:
    """Baixa e armazena imagem remota com cache validado."""
    url_hash = hashlib.md5(url.encode()).hexdigest()
    cache_file = os.path.join(CACHE_DIR, f"{url_hash}.png")

    if is_cache_valid(cache_file):
        return Image.open(cache_file)
    
    try:
        response = requests.get(url, stream=True, timeout=15)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img.save(cache_file)
        return img
    except Exception as e:
        raise ValueError(f"Falha ao baixar URL {url}: {str(e)}")

def load_local_image(path: str) -> Image.Image:
    """Carrega imagem local com verificação de existência."""
    if not os.path.exists(path):
        raise ValueError(f"Arquivo não encontrado: {path}")
    try:
        return Image.open(path)
    except Exception as e:
        raise ValueError(f"Erro ao abrir imagem {path}: {str(e)}")

def is_cache_valid(cache_file: str) -> bool:
    """Verifica se o cache é válido e está dentro do prazo de expiração."""
    return os.path.exists(cache_file) and \
           (os.path.getmtime(cache_file) > (time.time() - CACHE_EXPIRATION))

def wrap_text(text: str, width: int) -> List[str]:
    """Quebra texto em múltiplas linhas respeitando o limite de largura."""
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        if len(' '.join(current_line + [word])) <= width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines

# ==================== PROCESSAMENTO DE IMAGEM ====================

def apply_image_adjustments(
    img: Image.Image,
    contrast: float,
    brightness: float,
    invert: bool
) -> Image.Image:
    """Aplica ajustes de imagem de forma sequencial e otimizada."""
    img = img.convert('L')
    
    if contrast != 1.0:
        img = ImageEnhance.Contrast(img).enhance(contrast)
    if brightness != 1.0:
        img = ImageEnhance.Brightness(img).enhance(brightness)
    if invert:
        img = ImageOps.invert(img)
    
    return img

def calculate_dimensions(
    img: Image.Image,
    target_width: int,
    target_height: Optional[int]
) -> Tuple[int, int]:
    """Calcula dimensões mantendo aspect ratio com correção para fontes."""
    orig_width, orig_height = img.size
    aspect = orig_height / orig_width
    
    if target_height is None:
        target_height = int(target_width * aspect * ASPECT_CORRECTION)
    else:
        target_width = int(target_height / (aspect * ASPECT_CORRECTION))
    
    return (max(target_width, 10), max(target_height, 5))

def calculate_compact_dimensions(
    img: Image.Image,
    target_width: int,
    optimize_for: str
) -> Tuple[int, int]:
    """Calcula dimensões para modo compacto com restrições específicas."""
    width_map = {
        'terminal': min(target_width, 100),
        'markdown': min(target_width, 70),
        'html': target_width
    }
    width = width_map.get(optimize_for, 80)
    aspect = img.height / img.width
    height = int(width * aspect * ASPECT_CORRECTION)
    return (width, max(height, 5))

def render_ascii(img: Image.Image, style: str) -> str:
    """Renderiza a imagem em ASCII usando o estilo especificado."""
    chars = IMAGE_STYLES.get(style, IMAGE_STYLES["default"])
    pixels = img.load()
    return "\n".join(
        "".join(chars[min(pixels[x, y] * (len(chars)-1) // 255, len(chars)-1)]
        for x in range(img.width))
        for y in range(img.height)
    )

# ==================== EXPORTAÇÃO E SAÍDA ====================

def save_output(content: str, filename: str, file_type: str = "text"):
    """Salva conteúdo em arquivo com tratamento para diferentes formatos."""
    try:
        if file_type == 'html':
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(generate_html_template(content))
        else:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
        print(f"Arte salva em {filename}")
    except Exception as e:
        raise ValueError(f"Erro ao salvar arquivo {filename}: {str(e)}")

def generate_html_template(art: str, title: str = "ASCII Art") -> str:
    """Gera template HTML completo com estilos CSS integrados."""
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        pre {{ 
            background: #1a1a1a;
            color: #f0f0f0;
            padding: 20px;
            border-radius: 8px;
            font-family: monospace;
            white-space: pre-wrap;
        }}
    </style>
</head>
<body>
    <pre>{art}</pre>
</body>
</html>"""

# ==================== CLI E EXECUÇÃO PRINCIPAL ====================

def configure_parser() -> argparse.ArgumentParser:
    """Configura o parser de argumentos da CLI."""
    parser = argparse.ArgumentParser(
        description="AsciiArt Generator 2.0 - Gerador avançado de arte ASCII",
        epilog="Exemplos:\n"
               "  asciiart.py -t 'Hello' -i logo.png --width 80\n"
               "  asciiart.py -i https://ex.com/img.jpg --style blocks --html"
    )

    # Grupo para texto
    text_group = parser.add_argument_group('Opções de Texto')
    text_group.add_argument('-t', '--text', help='Texto para conversão')
    text_group.add_argument('-s', '--style', default='block',
                          help=f"Estilo de texto ({'/'.join(STYLES.keys())})")

    # Grupo para imagem
    image_group = parser.add_argument_group('Opções de Imagem')
    image_group.add_argument('-i', '--image', help='Caminho/URL da imagem')
    image_group.add_argument('--width', type=int, default=80, help='Largura da saída')
    image_group.add_argument('--style-img', default='default',
                           help=f"Estilo de imagem ({'/'.join(IMAGE_STYLES.keys())})")
    image_group.add_argument('--contrast', type=float, default=1.0,
                           help='Ajuste de contraste (0.1-3.0)')
    image_group.add_argument('--compact', action='store_true',
                           help='Modo compacto para terminais')

    # Grupo de saída
    output_group = parser.add_argument_group('Opções de Saída')
    output_group.add_argument('-o', '--output', help='Arquivo de saída')
    output_group.add_argument('--html', help='Exportar como HTML')

    # Adicione este grupo para documentação
    doc_group = parser.add_argument_group('Opções para Documentação')
    doc_group.add_argument('--doc', action='store_true', 
                         help='Modo documentação (gera banner estilizado)')
    doc_group.add_argument('--title', help='Título para o banner de documentação')
    doc_group.add_argument('--subtitle', help='Subtítulo para o banner')
    doc_group.add_argument('--banner-width', type=int, default=80,
                         help='Largura do banner de documentação')
    
    return parser

def main():
    """Função principal com tratamento unificado de erros e fluxo de execução."""
    parser = configure_parser()
    args = parser.parse_args()
    
    try:
        output = []

        if args.doc:
            if not args.title:
                raise ValueError("Título é obrigatório para modo documentação (--title)")
            
            banner = generate_doc_banner(
                title=args.title,
                subtitle=args.subtitle if args.subtitle else "",
                style=args.style,
                width=args.banner_width
            )
            
            print("\n" + banner + "\n")
            
            if args.output:
                save_output(banner, args.output)
            return

        # Processar imagem se fornecida
        if args.image:
            ascii_img = process_image(
                args.image,
                width=args.width,
                style=args.style_img,
                contrast=args.contrast,
                compact=args.compact
            )
            output.append(ascii_img)
            print("\nArte da Imagem:\n" + ascii_img)

        # Processar texto se fornecido
        if args.text:
            ascii_text = generate_art(args.text, args.style)
            output.append(ascii_text)
            print("\nArte do Texto:\n" + ascii_text)

        # Gerar saída combinada
        final_art = "\n\n".join(output)
        
        # Salvar resultados
        if args.output:
            save_output(final_art, args.output, 
                       'html' if args.output.endswith('.html') else 'text')
        
        if args.html:
            save_output(final_art, args.html, 'html')

    except Exception as e:
        print(f"\nErro: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()