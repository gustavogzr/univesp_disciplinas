<?php
function myTest() {
    static $x = 0;
    echo $x . "<br>";
    $x++;
}

myTest();
myTest();
myTest();
echo $x; //não pode ser acessada porque é uma variável local
?>