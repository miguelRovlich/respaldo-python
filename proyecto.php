<?php
$rutMasAlto = 0;
$notaMasAlta = 0;
$aprobados = 0;
$reprobados = 0;
$total = 0;
$suma = 0;
$continuar = "";
while ($continuar != "n") {
    $rut = readline("Ingrese RUT: ");
    $nota = readline("Ingrese nota: ");
    if ($nota >=4) {
        $aprobados = $aprobados + 1;
    }else {
        $reprobados = $reprobados + 1;
    }
    if ($nota>$notaMasAlta) {
        $rutMasAlto = $rut;
    }
    $suma = $suma + $nota;
    $total = $total +1;
    $continuar = readline("Desea continuar? (s/n): ");
}

echo "";

$opcion = 0;
while ($opcion != 7) {
	echo "1) RUT de la persona con la calificación más alta.\n";
    echo "2) Promedio de notas del curso.\n";
    echo "3) Cantidad de alumnos aprobados.\n";
    echo "4) Cantidad de alumnos reprobados.\n";
    echo "5) Porcentaje de reprobados.\n";
    echo "6) Cantidad de alumnos procesados.\n";
    echo "7) Salir\n";
	$opcion = readline("Ingrese una opcion: ");
    if ($opcion ==1) {
        echo $rutMasAlto;
    } else  if ($opcion ==2) {
        $promedio = $suma/$total;
        echo $promedio;
    } else  if ($opcion ==3) {
        echo $aprobados;
    } else  if ($opcion == 4) {
        echo $reprobados;
    } else  if ($opcion == 5) {
        $porcentaje = round($aprobados/$reprobados*100);
        echo $porcentaje;    
    } else  if ($opcion == 6) {
        echo $total;
    }
    else {
        echo"Opcion invalida\n";
    }
}
?>