package br.com.fiap.collections.view;

import java.util.HashSet;
import java.util.Set;

public class SetDjw3 {
	public static void main(String[] args) {
		
	
	
		//Criar um conjunto de String(Nomes de Séries)
		Set<String> conjunto = new HashSet<>();
		
		//Adicionar 2 séries 
		conjunto.add("Stranged Things");
		conjunto.add("Luanmohamed");
		
		//Exibir a quantidade de série no conjunto
		System.out.println("Quantidade de elemento: " + conjunto.size());
		
		conjunto.remove("Friends");
	
		//Exibir as séries do conjunto
		conjunto.forEach(p -> System.out.println(p));
	}
}
