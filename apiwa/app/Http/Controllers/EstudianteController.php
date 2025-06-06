<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Estudiante;
use Illuminate\Support\Facades\Log;

class EstudianteController extends Controller
{
    public function index()
    {
        $estudiantes = Estudiante::with('paralelo')->get();

        $resultado = $estudiantes->map(function ($est) {
            return [
                'id' => $est->id,
                'nombre' => $est->nombre,
                'cedula' => $est->cedula,
                'correo' => $est->correo,
                'paralelo' => $est->paralelo->nombre ?? null,
            ];
        });

        return response()->json($resultado);
    }

    public function store(Request $request)
    {
        Log::info('Intentando crear estudiante', $request->all());

        $request->validate([
            'nombre' => 'required|string|max:100',
            'cedula' => 'required|string|max:10|unique:estudiantes',
            'correo' => 'required|email',
            'paralelo_id' => 'required|exists:paralelos,id'
        ]);

        $data = $request->only(['nombre', 'cedula', 'correo', 'paralelo_id']);
        $estudiante = Estudiante::create($data);

        Log::info('Estudiante creado con ID:' . $estudiante->id);

        return response()->json([
            'mensaje' => 'Estudiante creado exitosamente',
            'estudiante' => $estudiante
        ], 201);
    }

    public function show(string $id)
    {

        $estudiante = Estudiante::with('paralelo')->find($id);

        if (!$estudiante) {
            return response()->json([
                'mensaje' => 'Estudiante no encontrado'
            ], 404);
        }

        return response()->json([
            'id' => $estudiante->id,
            'nombre' => $estudiante->nombre,
            'cedula' => $estudiante->cedula,
            'correo' => $estudiante->correo,
            'paralelo' => $estudiante->paralelo->nombre ?? null,
        ]);
    }

    public function update(Request $request, string $id)
    {
        $estudiante = Estudiante::find($id);

        if (!$estudiante) {
            return response()->json(['mensaje' => 'Estudiante no encontrado'], 404);
        }

        $request->validate([
            'nombre' => 'sometimes|required|string|max:100',
            'cedula' => 'sometimes|required|string|max:10|unique:estudiantes,cedula,' . $id,
            'correo' => 'sometimes|required|email',
            'paralelo_id' => 'sometimes|required|exists:paralelos,id',
        ]);

        $estudiante->update($request->all());

        return response()->json([
            'mensaje' => 'Estudiante actualizado exitosamente',
            'estudiante' => $estudiante
        ]);
    }

    public function destroy(string $id)
    {
        $estudiante = Estudiante::find($id);

        if (!$estudiante) {
            return response()->json(['mensaje' => 'Estudiante no encontrado'], 404);
        }

        $estudiante->delete();

        return response()->json(['mensaje' => 'Estudiante eliminado exitosamente']);
    }

}