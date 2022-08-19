package br.com.fiap.collections.model;

public class Filme {
	
	private String nome;
	
	private int duracao;
	
	private String genero;

	public Filme(String nome, int duracao, String genero) {
		super();
		this.nome = nome;
		this.duracao = duracao;
		this.genero = genero;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public int getDuracao() {
		return duracao;
	}

	public void setDuracao(int duracao) {
		this.duracao = duracao;
	}

	public String getGenero() {
		return genero;
	}

	public void setGenero(String genero) {
		this.genero = genero;
	}
	
	
}
