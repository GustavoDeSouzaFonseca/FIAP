package br.com.fiap.revisao.model;

public class Venda {
	private String cliente;
	private Produto produto;
	private String formaPagamento;
	private int quantidade;
	
	public Venda() {}
	
	public Venda(String cliente, Produto doce, String formaPagamento, int quantidade) {
		super();
		this.cliente = cliente;
		this.produto = doce;
		this.formaPagamento = formaPagamento;
		this.quantidade = quantidade;
	}
	
	//Métodos 
	//Tirar a quantidade do estoque e retornar o valor a ser pago
	public double finalizarVenda() {
		produto.setEstoque(produto.getEstoque()- quantidade); //
		return getProduto().getPreco() * quantidade;
	}
	
	public String getCliente() {
		return cliente;
	}
	public void setCliente(String cliente) {
		this.cliente = cliente;
	}
	public Produto getProduto() {
		return produto;
	}
	public void setProduto(Produto produto) {
		this.produto = produto;
	}
	public String getFormaPagamento() {
		return formaPagamento;
	}
	public void setFormaPagamento(String formaPagamento) {
		this.formaPagamento = formaPagamento;
	}
	public int getQuantidade() {
		return quantidade;
	}
	public void setQuantidade(int quantidade) {
		this.quantidade = quantidade;
	}
	
	
}
