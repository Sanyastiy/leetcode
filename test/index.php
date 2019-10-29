<?php
require_once "dbinclude.php";
require_once "functions.php";
?>

<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Hello, VLADIT!</title>
</head>
<body>
<h1>Hello, Daniil</h1>
<div class="text" id="main-text">
    <?php
        $data=get_data($link);
    echo "<pre>";
    print_r($data);
    echo "</pre>";
    ?>
</div>
</body>
</html>
