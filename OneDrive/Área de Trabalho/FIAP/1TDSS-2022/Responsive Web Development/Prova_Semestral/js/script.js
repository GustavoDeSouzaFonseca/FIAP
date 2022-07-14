const botaoSubmit = document.getElementById('btnEnviar')
  botaoSubmit.addEventListener("click", () => {
          const campos = document.querySelectorAll("input[type='text'], input[type='email']")
            for (let i = 0; i < campos.length; i++)
            { if (campos[i].value == "")
            { alert("O CAMPO " + campos[i].placeholder + " não foi preenchido!")
                         return } } document.querySelector('.cadastro').submit()
    alert("Cadastro realizado com sucesso!")
});