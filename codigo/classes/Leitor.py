# -*- coding: UTF-8 -*-
import re

from excecoes.CriacaoTuringException import CriacaoTuringException


class Leitor:
    arquivo = None
    linhas = None
    estadoInicial = None
    estadosFinais = None
    estados = None
    transicoes = None
    alfabeto = None
    todosSimbolos = None
    
    def __init__(self, arquivo):
        self.arquivo = open(arquivo, "r")
        self.leDados()
        self.arquivo.close()
        
    def leDados(self):
        self.linhas = self.arquivo.read().splitlines()
        while '' in self.linhas:
            self.linhas.remove('')
        self.leEstados()
        self.leEstadoInicial()
        self.leEstadosFinais()
        self.leAlfabeto()
        self.leTodosSimbolos()
        self.leTransicoes()
        
    def leEstados(self):
        self.estados = []
        aux = self.linhas[0]
        qtdEstados = int(aux.replace('\ufeff', ''))
        
        for i in range(qtdEstados):
            self.estados.append(str(i))
        
    def leEstadoInicial(self):
        aux = re.compile("{(\d+)}")
        self.estadoInicial = aux.findall(self.linhas[1])
        if (len(self.estadoInicial) != 1):
            raise CriacaoTuringException("ERRO: Ha mais de um estado inicial definido")
        self.estadoInicial = self.estadoInicial[0]
    
    def leEstadosFinais(self):
        aux = re.compile("(\d+)")
        self.estadosFinais = aux.findall(self.linhas[2])
    
    def leAlfabeto(self):
        aux = re.compile("(\w)")
        self.alfabeto = aux.findall(self.linhas[3])
    
    def leTodosSimbolos(self):
        aux = re.compile("(\w)")
        self.todosSimbolos = aux.findall(self.linhas[4])
        
    def leTransicoes(self):
        self.transicoes = []
        for i in range(6, len(self.linhas) - 2):
            aux = re.compile("(\w)")
            dados = aux.findall(self.linhas[i][:-1])
            self.transicoes.append(dados)
        self.transicoes.append(re.compile("(\w)").findall(self.linhas[-2]))