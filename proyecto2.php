<?php
$continuar = "";
$notaMasAlta = 0;
$rutNotaAlta = 0;
$aprobados = 0;
$reprobados = 0;
$suma = 0;
$cantidadNotas = 0;
while ($continuar !="n" or $continuar != "N") {
    $rut = readline("Ingrese rut: ");
    $nota = readline("Ingrese nota: ")
    if ($nota>=4) {
        $aprobados = $aprobados + 1;
    } else{
        $reprobados = $reprobados + 1;
    }
    if($nota > $notaMasAlta) {
        $notaMasAlta = $nota;
        $rutMasAlto = $rut;
    }
    $cantidadNotas = $cantidadNotas + 1;
    $suma = $suma + $nota;
    $continuar = readline("Desea continuar? (s/n): ");
}

$opcion = 0;

while ($opcion != 7) {
    echo "1) RUT de la persona con la calificación más alta.\n";
    echo "2) Promedio de notas del curso.\n";
    echo "3) Cantidad de alumnos aprobados.\n";
    echo "4) Cantidad de alumnos reprobados.\n";
    echo "5) Porcentaje de reprobados.\n";
    echo "6) Cantidad de alumnos procesados.\n";
    echo "7) Salir\n";
    echo "\n"
    $opcion = readline("Ingrese opcion: ");
    if ($opcion ==1) {
        $promedio = $suma / $cantidadNotas;
        echo "Promedio del curso: ";
        echo $promedio;
    } elseif ($opcion == 2) {
        echo "Rut de la persona con promedio mas alto: ";
        echo $rutMasAlto;
    }elseif ($opcion == 3) {
        echo "Cantidad Aprobados: ";
        echo $aprobados;
    }elseif ($opcion == 4) {
        echo "Cantidad Reprobados: ";
        echo $reprobados;
    }elseif ($opcion == 5) {
        echo "Porcentaje Reprobados: ";
        $porcentaje = round($aprobados/$reprobados*100);
    }elseif ($opcion == 6) {
        echo "Cantidad de alumnos procesados";
        echo $cantidadNotas;
    } else {
        echo "Opcion invalida\n";
    }
}