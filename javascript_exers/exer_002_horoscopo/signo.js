function validacao_dados(){
    function removerAcentos(str) {
    return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    }

  
    
    var sig=document.forms["horoscopo"]["signo"].value.toLowerCase();
    var nome=document.forms["horoscopo"]["nome"].value;
    var c1=document.forms["horoscopo"]["senha"].value;
    var c2=document.forms["horoscopo"] ["confirmeSenha"].value;
    var e=document.forms["horoscopo"]["email"].value;
    var arrobapos=e.indexOf("@");
    var s = removerAcentos(sig);
  
    if(sig==null || sig=="")
        {alert("Seu signo precisa ser informado.");return false;
        }
    if(nome==null ||nome=="")
        {alert("Seu nome precisa ser informado.");
        return false;
        }
    if(document.forms["horoscopo"]["senha"].value.length<8)
    {
        alert("Senha curta. Digite pelo menos 8 caracteres.");return false;
    }
    if(c1 != c2){
        alert("Senha diferente. Tente novamente."); return false;
    }
    if (arrobapos<1)
    {
        alert("Endereço de e-mail inválido!");
        return false;
    }


    switch (s){
      case 'aries':
          alert('O periodo do seu Signo é: 21 de março – 19 de abril e pertence ao Elemento: Fogo');
          break;
      case 'touro':
          alert('O periodo do seu Signo é: 20 de abril – 20 de maio e pertence ao Elemento: Terra');
          break;
          case 'gemeos':
          alert('O periodo do seu Signo é: 21 de maio – 20 de junho e pertence ao Elemento: Ar');
          break;
          case 'cancer':
          alert('O periodo do seu Signo é: 21 de junho – 22 de julho e pertence ao Elemento: Água');
          break;
          case 'leao':
          alert('O periodo do seu Signo é: 23 de julho – 22 de agosto e pertence ao Elemento: Fogo');
          break;
          case 'virgem':
          alert('O periodo do seu Signo é: 23 de agosto – 22 de setembro e pertence ao Elemento: Terra');
          break;
          case 'libra':
          alert('O periodo do seu Signo é: 23 de setembro – 22 de outubro e pertence ao Elemento: Ar');
          break;
          case 'escorpiao':
          alert('O periodo do seu Signo é: 23 de outubro – 21 de novembro e pertence ao Elemento: Água');
          break;
          case 'sagitario':
          alert('O periodo do seu Signo é: 22 de novembro – 21 de dezembro e pertence ao Elemento: Fogo');
          break;
          case 'capricornio':
          alert('O periodo do seu Signo é: 22 de dezembro – 19 de janeiro e pertence ao Elemento: Terra');
          break;
          case 'aquario':
          alert('O periodo do seu Signo é: 20 de janeiro – 18 de fevereiro e pertence ao Elemento: Ar');
          break;
          case 'peixes':
          alert('O periodo do seu Signo é: 19 de fevereiro – 20 de março e pertence ao Elemento: Água');
          break;
          
          default:
              alert("Signo não encontrado!");
    }

}
  