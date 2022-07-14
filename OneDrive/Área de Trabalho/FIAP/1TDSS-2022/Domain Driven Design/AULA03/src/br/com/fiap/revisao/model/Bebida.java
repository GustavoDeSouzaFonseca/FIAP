package br.com.fiap.revisao.model;

public class Bebida extends Produto {
	
	//Atributos
	private int litragem;
	private String embalagem;
	
	public Bebida () {}
	
	public Bebida(String nome, double preco, int estoque, boolean refrigerado, String sabor, int litragem,
			String embalagem) {
		super(nome, preco, estoque, refrigerado, sabor);
		this.litragem = litragem;
		this.embalagem = embalagem;
	}




	public int getLitragem() {
		return litragem;
	}
	public void setLitragem(int litragem) {
		this.litragem = litragem;
	}
	public String getEmbalagem() {
		return embalagem;
	}
	public void setEmbalagem(String embalagem) {
		this.embalagem = embalagem;
	}
	
	
}
