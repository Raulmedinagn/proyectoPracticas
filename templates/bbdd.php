<?php
	
	$conexion=mysqli_connect('localhost','root','','buscador');

?>



<!DOCTYPE html>
<html>
<head>
	<title>BBDD</title>
</head>
<body>
	<table>
		<tr>
			<td>ID</td>
			<td>Palabras clave</td>
			<td>URL de la API</td>
			<td>Json completo</td>
		</tr>


		<?php
		$sql="SELECT * from resumen_apis";
		$result=mysqli_query($conexion,$sql);

		while($mostrar=mysqli_fetch_array($result)){
		?>

		<tr>
			<td><?php echo $mostrar['id'] ?></td>
			<td><?php echo $mostrar['palabras_clave'] ?></td>
			<td><?php echo $mostrar['url_api'] ?></td>
			<td><?php echo $mostrar['json_completo'] ?></td>
		</tr>
	<?php 
	}
	 ?>
	</table>

</body>
</html>