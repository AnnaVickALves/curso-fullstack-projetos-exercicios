// *MODAL FILME*//

// Elementos do modal Filme
const modal = document.getElementById("modalFilme"); // pega o modal
const botaoAbrir = document.getElementById("cadastrarfilme"); // botão que abre o modal
const fechar = document.querySelector(".fechar"); // botão "X" de fechar

// Abrir modal ao clicar no botão
botaoAbrir.onclick = () => {
  modal.style.display = "block"; 
};

// Fechar modal ao clicar no X
fechar.onclick = () => {
  modal.style.display = "none";
};

// Elementos do modal Ver Filmes
const botaoVerfilmes = document.getElementById("Verfilmes");
const modalVerfilmes = document.getElementById("modalVerfilmes");
const fecharVerfilmes = document.querySelector(".fechar-Verfilmes");

botaoVerfilmes.onclick = () => modalVerfilmes.style.display = "block";
fecharVerfilmes.onclick = () => modalVerfilmes.style.display = "none";

// Fechar modal ao clicar fora do conteúdo (para ambos os modais)
window.addEventListener('click', (event) => {
  if (event.target === modal) {
    modal.style.display = "none";
  }
  if (event.target === modalVerfilmes) {
    modalVerfilmes.style.display = "none";
  }
});





    // Validação do formulário
    function validarFormulario(event) {
        const form = document.forms[0];
        const titulo = form["titulo_filme"].value.trim();
        const classificacao = form["classificacao_indicativa"].value;
        const genero = form["genero"].value;
        const duracao = form["duracao"].value;
        const sinopse = form["sinopse"].value.trim();
        const trailer = form["trailer"].value.trim();

        if (!titulo) {
            alert("O título é obrigatório.");
            event.preventDefault();
            return false;
        }

        if (!classificacao) {
            alert("Selecione a classificação indicativa.");
            event.preventDefault();
            return false;
        }

        if (!genero) {
            alert("Selecione o gênero.");
            event.preventDefault();
            return false;
        }

        if (!duracao || duracao <= 0) {
            alert("Informe uma duração válida.");
            event.preventDefault();
            return false;
        }

        if (!sinopse) {
            alert("Informe a sinopse.");
            event.preventDefault();
            return false;
        }

        if (trailer && !validarURL(trailer)) {
            alert("Informe uma URL válida para o trailer.");
            event.preventDefault();
            return false;
        }

        return true;
    }

    function validarURL(url) {
        const pattern = /^(http|https):\/\/[^ "]+$/;
        return pattern.test(url);
    }

    const form = document.querySelector("form");
    form.addEventListener("submit", validarFormulario);

    // Lógica do multiselect customizado para subgêneros
    const selectBox = document.querySelector(".custom-multiselect .select-box");
    const checkboxes = document.getElementById("checkboxes");
    const selectedSpan = document.getElementById("selected");
    const hiddenInput = document.getElementById("sub_genero_input");

    function toggleCheckboxes() {
        if (checkboxes.style.display === "block") {
            checkboxes.style.display = "none";
        } else {
            checkboxes.style.display = "block";
        }
    }

    // Fechar o dropdown ao clicar fora
    document.addEventListener("click", (e) => {
        if (!selectBox.contains(e.target) && !checkboxes.contains(e.target)) {
            checkboxes.style.display = "none";
        }
    });

    // Atualiza o texto selecionado e o valor escondido
    checkboxes.querySelectorAll("input[type=checkbox]").forEach((checkbox) => {
        checkbox.addEventListener("change", () => {
            const selecionados = [];
            checkboxes.querySelectorAll("input[type=checkbox]:checked").forEach((checked) => {
                selecionados.push(checked.value);
            });

            if (selecionados.length > 0) {
                selectedSpan.textContent = selecionados.join(", ");
            } else {
                selectedSpan.textContent = "Selecione os subgêneros";
            }

            // Atualiza o input escondido para envio no formulário
            hiddenInput.value = selecionados.join(",");
        });
    });
