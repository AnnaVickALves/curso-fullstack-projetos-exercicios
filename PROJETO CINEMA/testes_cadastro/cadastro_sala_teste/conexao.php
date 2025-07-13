<?php
    $conexao = MySQLi_connect("localhost","root", "");
    if(!$conexao){
        die('Não foi possivel conectar ao banco de dados.
            Erro detectado'.MySQLi_connect_error());
    }

    echo'Conexão bem-sucedida.';
    //MySQLi_select_db($conexao,"cine_senac");

    /*
    $tabela_sala = "CREATE TABLE sala
    (
        id_sala INT(10) AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(50) NOT NULL
    )";

    if (MySQLi_query($conexao, $tabela_sala)){
        echo "A tabela sala foi criada com sucesso\n!";
    } else{
        echo 'Erro ao criar tabela sala: '.MySQLi_error($conexao, $tabela_sala)."\n";
    }*/

    mysqli_set_charset($conexao,"utf8");
    //mysqli_close($conexao);
?>
