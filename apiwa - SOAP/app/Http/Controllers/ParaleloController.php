<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Paralelo;
use Illuminate\Support\Facades\Log;

class ParaleloController extends Controller
{
    public function index()
    {
        $paralelos = Paralelo::all();

        return response()->json($paralelos);
    }

    public function store(Request $request)
    {
        Log::info('Datos que llegan en la petición', $request->all());

        $request->validate([
            'nombre' => 'required|string|max:100|unique:paralelos',
        ]);

        $paralelo = Paralelo::create($request->all());
        Log::info('Paralelo creado con ID: ' . $paralelo->id);

        return response()->json([
            'mensaje' => 'Paralelo creado exitosamente',
            'paralelo' => $paralelo
        ], 201);
    }

    public function show($id)
    {
        $paralelo = Paralelo::find($id);

        if (!$paralelo) {
            return response()->json(['mensaje' => 'Paralelo no encontrado'], 420);
        }

        return response()->json($paralelo);
    }

    public function update(Request $request, $id)
    {
        $paralelo = Paralelo::find($id);

        if (!$paralelo) {
            return response()->json(['mensaje' => 'Paralelo no encontrado'], 420);
        }

        $request->validate([
            'nombre' => 'required|string|max:100|unique:paralelos,nombre,' . $id,
        ]);

        $paralelo->update($request->all());

        return response()->json([
            'mensaje' => 'Paralelo actualizado exitosamente',
            'paralelo' => $paralelo
        ]);
    }

    public function destroy($id)
    {
        $paralelo = Paralelo::find($id);

        if (!$paralelo) {
            return response()->json(['mensaje' => 'Paralelo no encontrado'], 404);
        }

        $paralelo->delete();

        return response()->json(['mensaje' => 'Paralelo eliminado exitosamente']);
    }
}