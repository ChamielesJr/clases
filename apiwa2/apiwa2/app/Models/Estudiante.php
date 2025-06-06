<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Estudiante extends Model
{
    use HasFactory;

    // Campos que pueden ser asignados de forma masiva (create, update, etc.)
    protected $fillable = ['nombre', 'cedula', 'correo', 'paralelo_id'];

    // Relación inversa: un estudiante pertenece a un paralelo
    public function paralelo()
    {
        return $this->belongsTo(Paralelo::class);
    }
}
