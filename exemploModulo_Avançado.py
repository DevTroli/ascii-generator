#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exemplo avançado de uso do AsciiArt Generator
Este exemplo mostra como criar um logger personalizado com banners ASCII
"""

import logging
import os
import time
from datetime import datetime
from asciiArt import generate_art

class AsciiLogger:
    """
    Logger personalizado que usa banners ASCII para mensagens importantes
    """
    def __init__(self, log_file=None, level=logging.INFO):
        """
        Inicializa o logger personalizado
        
        Args:
            log_file: Caminho para o arquivo de log (opcional)
            level: Nível de logging
        """
        # Configurar logger básico
        self.logger = logging.getLogger("AsciiLogger")
        self.logger.setLevel(level)
        
        # Formatar as mensagens de log
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        # Handler para console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # Handler para arquivo se especificado
        if log_file:
            # Garantir que o diretório existe
            log_dir = os.path.dirname(log_file)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir)
                
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
    
    def info(self, message):
        """Log de informação normal"""
        self.logger.info(message)
    
    def warning(self, message):
        """Log de aviso"""
        self.logger.warning(message)
    
    def error(self, message):
        """Log de erro"""
        self.logger.error(message)
    
    def critical(self, message):
        """
        Log de erro crítico com banner ASCII
        Para erros críticos, geramos um banner ASCII para chamar atenção
        """
        banner = generate_art("ERRO CRÍTICO", "block")
        self.logger.critical(f"\n{banner}\n{message}\n")
    
    def success(self, message):
        """
        Log de sucesso com banner ASCII
        Para registrar sucessos importantes com destaque visual
        """
        banner = generate_art("SUCESSO", "fancy")
        self.logger.info(f"\n{banner}\n{message}\n")
    
    def section(self, title):
        """
        Cria uma seção no log com um banner de título
        Útil para separar logicamente diferentes partes da execução
        """
        banner = generate_art(title, "classic")
        self.logger.info(f"\n{'-' * 80}\n{banner}\n{'-' * 80}")

# Exemplo de uso
def simular_processo():
    """Função que simula um processo com logs"""
    # Criar logger
    logger = AsciiLogger(log_file="logs/processo.log")
    
    # Início do processo
    logger.section("INÍCIO DO PROCESSO")
    logger.info("Processo iniciado em " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    # Simulação de etapas
    logger.info("Verifican
