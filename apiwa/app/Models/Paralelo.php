<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Paralelo extends Model
{
    use HasFactory;

    // Campo que se puede asignar de forma masiva
    protected $fillable = ['nombre'];

    // Relación: un paralelo tiene muchos estudiantes
    public function estudiantes()
    {
        return $this->hasMany(Estudiante::class);
    }
}
