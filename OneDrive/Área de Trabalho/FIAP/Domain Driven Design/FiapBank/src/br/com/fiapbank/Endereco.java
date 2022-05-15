package br.com.fiapbank;

public class Endereco {
	
	//Atributos
	String rua;
	short numero;
	String complemento;
	String bairro;
	String cep;
	
	//Métodos
	short getNumero(){
		return numero;
	}
			
	void setNumero(short novoNumero){
		numero = novoNumero;
	}

}
