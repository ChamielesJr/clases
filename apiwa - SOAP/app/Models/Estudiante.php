<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Estudiante extends Model
{
    protected $fillable = ['nombre', 'cedula', 'correo', 'paralelo_id'];

    public function paralelo()
    {
        return $this->belongsTo(Paralelo::class);
    }
}
