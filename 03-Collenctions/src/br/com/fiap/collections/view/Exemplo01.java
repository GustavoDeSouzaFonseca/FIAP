package br.com.fiap.collections.view;

import java.util.ArrayList;
import java.util.List;

public class Exemplo01 {
	
	public static void main(String[] args) {
		List<Integer> lista = new ArrayList<>();
	
		//Adicionar um elemento na lista
		lista.add(10);
		lista.add(25);
		lista.add(1, 3);
		
		//Exibir quantidade de elementos da lista
		System.out.println("Quantidade de elementos: " + lista.size());
		
		//Recuperar elemento da primeira posição
		System.out.println("Elemento da primeira posição: " + lista.get(0));
		
		//Exibir elementos da lista
		for(int i=0; lista.size() > i; i++) {
			System.out.println(lista.get(i));
		}
		
		//Remover a pior série do conjunto na sua opinião
		lista.remove(0);
		
		//Lista esta vazia?
		System.out.println(lista.isEmpty());
		
	}

}

