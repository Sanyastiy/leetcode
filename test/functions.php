<?php
require 'dbinclude.php';
function get_data($link){
    $sql = "SELECT * FROM data";

    $result = mysqli_query($link, $sql);

    $data = mysqli_fetch_all($result,MYSQLI_ASSOC);
    if($result) {echo "запрос не прошел".mysqli_error();}
    return $data;
}
