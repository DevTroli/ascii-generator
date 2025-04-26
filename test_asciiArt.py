#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testes unitários para o gerador de Arte ASCII
"""

import unittest
import os
import tempfile
from asciiArt import generate_art, save_to_file, export_html, STYLES


class TestAsciiArtGenerator(unittest.TestCase):
    """Testes para o Gerador de Arte ASCII"""

    def test_generate_art_block(self):
        """Testa a geração de arte no estilo 'block'"""
        art = generate_art("TEST", "block")
        # Verificar se a arte não está vazia
        self.assertTrue(len(art) > 0)
        # Verificar se tem 5 linhas (altura dos caracteres no estilo block)
        self.assertEqual(len(art.split("\n")), 5)

    def test_generate_art_fancy(self):
        """Testa a geração de arte no estilo 'fancy'"""
        art = generate_art("TEST", "fancy")
        self.assertTrue(len(art) > 0)
        self.assertEqual(len(art.split("\n")), 5)

    def test_generate_art_classic(self):
        """Testa a geração de arte no estilo 'classic'"""
        art = generate_art("TEST", "classic")
        self.assertTrue(len(art) > 0)
        self.assertEqual(len(art.split("\n")), 5)

    def test_invalid_style(self):
        """Testa o comportamento com um estilo inválido"""
        with self.assertRaises(ValueError):
            generate_art("TEST", "invalid_style")

    def test_special_characters(self):
        """Testa o comportamento com caracteres especiais"""
        # Deve substituir caracteres não suportados por espaços
        art = generate_art("TEST@123", "block")
        self.assertTrue(len(art) > 0)

    def test_save_to_file(self):
        """Testa salvar a arte em um arquivo"""
        art = generate_art("TEST", "block")
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            filename = temp.name

        try:
            save_to_file(art, filename)
            # Verificar se o arquivo foi criado
            self.assertTrue(os.path.exists(filename))

            # Verificar o conteúdo do arquivo
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertEqual(content, art)
        finally:
            # Limpar
            if os.path.exists(filename):
                os.remove(filename)

    def test_export_html(self):
        """Testa exportar a arte como HTML"""
        art = generate_art("TEST", "block")
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as temp:
            filename = temp.name

        try:
            export_html(art, filename, "TEST")
            # Verificar se o arquivo foi criado
            self.assertTrue(os.path.exists(filename))

            # Verificar se o conteúdo HTML contém a arte
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn(art, content)
            self.assertIn("<title>TEST</title>", content)
        finally:
            # Limpar
            if os.path.exists(filename):
                os.remove(filename)

    def test_all_characters_defined(self):
        """Verifica se todos os estilos têm o mesmo conjunto de caracteres"""
        expected_chars = set(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?-_&/\\@#$%^*()[]{}:;\"'`~+="
        )
        for style_name, style_chars in STYLES.items():
            defined_chars = set(style_chars.keys())
            # Verifica se o estilo atual tem todos os caracteres esperados
            missing = expected_chars - defined_chars
            self.assertEqual(
                len(missing),
                0,
                f"O estilo '{style_name}' não tem definição para os caracteres: {missing}",
            )


if __name__ == "__main__":
    unittest.main()
