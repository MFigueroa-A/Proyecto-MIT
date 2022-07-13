<?php
$temperature = $_GET['temp'];
$humidity = $_GET['hum'];
$moisture = $_GET['soil'];
//$Fecha = $_GET['time'];

echo "La temperatura es: ".$temperature." <br>La humedad  es: ".$humidity."<br>La humedad es: ".$moisture."<br>"; 

$usuario = "root";
$contrasena = "";
$servidor = "localhost";
$basededatos = "mit";

$conexion = mysqli_connect( $servidor, $usuario, "" ) or die ("No se ha podido conectar al servidor de Base de datos");

$db = mysqli_select_db( $conexion, $basededatos ) or die ( "No se ha podido seleccionar la base de datos" );

$consulta = "INSERT INTO nodemcu (temperature, humidity, moisture) VALUES (".$temperature.", ".$humidity.", ".$moisture.")";

$resultado = mysqli_query( $conexion, $consulta );

?>