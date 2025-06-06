<?php

namespace App\Soap;

use App\Models\Estudiante;
use App\Models\Paralelo;

class ServicioSoap
{
    /**
     * Retorna todos los estudiantes
     * @return array
     */
    public function obtenerEstudiantes()
    {
        return Estudiante::all()->toArray();
    }

    /**
     * Crea un nuevo estudiante
     * @param string $nombre
     * @param string $apellido
     * @param string $email
     * @param int $paralelo_id
     * @return array
     */
    public function crearEstudiante($nombre, $apellido, $email, $paralelo_id)
    {
        $estudiante = Estudiante::create([
            'nombre' => $nombre,
            'apellido' => $apellido,
            'email' => $email,
            'paralelo_id' => $paralelo_id,
        ]);

        return $estudiante->toArray();
    }

    /**
     * Retorna todos los paralelos
     * @return array
     */
    public function obtenerParalelos()
    {
        return Paralelo::all()->toArray();
    }

    /**
     * Crea un nuevo paralelo
     * @param string $nombre
     * @return array
     */
    public function crearParalelo($nombre)
    {
        $paralelo = Paralelo::create([
            'nombre' => $nombre,
        ]);

        return $paralelo->toArray();
    }
}
