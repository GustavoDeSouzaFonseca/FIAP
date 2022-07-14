package br.com.fiap.revisao.model;

public class Produto {
	
	//Atributos
	private String nome;
	private double preco;
	private int estoque;
	private boolean refrigerado;
	private String sabor;
	
	//Construtores
	public Produto() {}
	
	public Produto(String nome, double preco, int estoque, boolean refrigerado, String sabor) {
		super();
		this.nome = nome;
		this.preco = preco;
		this.estoque = estoque;
		this.refrigerado = refrigerado;
		this.sabor = sabor;
	}

	//Getters e Setters
	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public double getPreco() {
		return preco;
	}

	public void setPreco(double preco) {
		this.preco = preco;
	}

	public int getEstoque() {
		return estoque;
	}

	public void setEstoque(int estoque) {
		this.estoque = estoque;
	}

	public boolean isRefrigerado() {
		return refrigerado;
	}

	public void setRefrigerado(boolean refrigerado) {
		this.refrigerado = refrigerado;
	}

	public String getSabor() {
		return sabor;
	}

	public void setSabor(String sabor) {
		this.sabor = sabor;
	}
	
	
}
