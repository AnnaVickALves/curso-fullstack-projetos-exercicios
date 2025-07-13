<?php
if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $nome = $_POST['nome'];

    require("conexao.php");
    mysqli_select_db($conexao, "cine_senac");

    $inserir = "INSERT INTO sala (nome) VALUES ('$nome')";

    if (mysqli_query($conexao, $inserir)) {
        echo "Sala cadastrada com sucesso!";
    } else {
        echo "Erro no cadastro: " . mysqli_error($conexao);
    }

    mysqli_close($conexao);
}
?>