package br.com.fiap.elevador.model;

public class Elevador {
	
	//Atributos
	int andarAtual, totalAndares, capacidade, quantidadePessoaAtual;
	
	//Construtor
	public Elevador(int andares, int capacidade) {
		totalAndares = andares;
		this.capacidade = capacidade;
	}
	
	//Métodos
	
	public void andar() {
		andarAtual++;
	}
	
	public int getAndarAtual() {
		return andarAtual;
	}

	public void setAndarAtual(int andarAtual) {
		this.andarAtual = andarAtual;
	}

	public int getTotalAndares() {
		return totalAndares;
	}

	public void setTotalAndares(int totalAndares) {
		this.totalAndares = totalAndares;
	}

	public int getCapacidade() {
		return capacidade;
	}

	public void setCapacidade(int capacidade) {
		this.capacidade = capacidade;
	}

	public int getQuantidadePessoaAtual() {
		return quantidadePessoaAtual;
	}

	public void setQuantidadePessoaAtual(int quantidadePessoaAtual) {
		this.quantidadePessoaAtual = quantidadePessoaAtual;
	}

	void desce() {
		andarAtual--;
	}
	
	void entra() {
		quantidadePessoaAtual++;
		
	}
	
	void sai() {
		quantidadePessoaAtual--;
	}
	
}
