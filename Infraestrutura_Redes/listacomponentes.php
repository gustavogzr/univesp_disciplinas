<?php
$user = "alunoinfra";
$password = "Aluno123#@";
$database = "exemploinfra";
$table = "computador";

try {
    $db = new PDO("mysql:host=localhost;dbname=$database", $user, $password);
    echo "<h2>Lista de Componentes de Um Computador</h2><ol>";
    foreach($db->query("SELECT conteudo FROM $table") as $row) {
        echo "<li>" . $row['conteudo'] . "</li>";
    }
    echo "</ol>";
} catch (PDOException $e) {
    print "Ocorreu um erro! - " . $e->getMessage() . "<br/>";
    die();
}