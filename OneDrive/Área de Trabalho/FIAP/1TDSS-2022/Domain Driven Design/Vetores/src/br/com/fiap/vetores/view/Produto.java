package br.com.fiap.vetores.view;

public class Produto {
	//ATRIBUTOS
	private int quantidade;
	private double preco;
	private double desconto;
	
	//CONSTRUCTORS
	public Produto (int quantidade, double preco, double desconto) {
		this.quantidade = quantidade;
		this.preco = preco;
		this.desconto = desconto;
	}
	
	//GETTERS AND SETTERS
	public int getQuantidade() {
		return quantidade;
	}
	public void setQuantidade(int quantidade) {
		this.quantidade = quantidade;
	}
	public double getPreco() {
		return preco;
	}
	public void setPreco(float preco) {
		this.preco = preco;
	}
	public double getDesconto() {
		return desconto;
	}
	public void setDesconto(float desconto) {
		this.desconto = desconto;
	}

	//OVERRIDE
	@Override
	public String toString() {
		return "Produto [quantidade=" + quantidade + ", preco=" + preco + ", desconto=" + desconto + "]";
	}

	
	
	
	

}
