package br.com.fiap.collections.view;

import java.util.ArrayList;
import java.util.List;

import br.com.fiap.collections.model.Filme;

public class ExemploListFilmes {
	public static void main(String[] args) {
		
		//Criar uma lista de Filmes
		List<Filme> filme = new ArrayList<>();
		
		
		//Adicionar 2 filmes na lista
		filme.add(new Filme("Hari Pote", 120, "Mago"));
		filme.add(new Filme("cal ofi duti", 220, "acao"));
		
		//Exibir os dados do filme da lista
		filme.forEach(t -> System.out.println(t));
	}
}
