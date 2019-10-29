<?php
$link = mysqli_connect('localhost','cb03059_test','cb03059_test','cb03059_test');
if(mysqli_connect_errno())
{
    echo"DB connection isn`t works((( with error number: ".mysqli_connect_errno()." :".mysqli_connect_error();
    exit();
}