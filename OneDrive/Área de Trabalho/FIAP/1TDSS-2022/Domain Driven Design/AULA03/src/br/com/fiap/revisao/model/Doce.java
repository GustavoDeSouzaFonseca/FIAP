package br.com.fiap.revisao.model;

public class Doce extends Produto{
	
	private boolean acucar;
	private String recheio;
	
	public Doce () {}
	
	public Doce(String nome, double preco, int estoque, boolean refrigerado, String sabor, boolean acucar,
			String recheio) {
		super(nome, preco, estoque, refrigerado, sabor);
		this.acucar = acucar;
		this.recheio = recheio;
	}

	public boolean isAcucar() {
		return acucar;
	}

	public void setAcucar(boolean acucar) {
		this.acucar = acucar;
	}

	public String getRecheio() {
		return recheio;
	}

	public void setRecheio(String recheio) {
		this.recheio = recheio;
	}

}
