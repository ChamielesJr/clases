<?php

use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Response;

// Ruta principal que muestra la vista de bienvenida
Route::get('/', function () {
    return view('welcome');
});

// Ruta para exponer el archivo WSDL (GET)
Route::get('/wsdl', function () {
    return Response::make(file_get_contents(storage_path('wsdl/servicio.wsdl')), 200, [
        'Content-Type' => 'text/xml'
    ]);
});
