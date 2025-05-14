<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ParaleloController extends Controller
{
    //


//método para obtener todos los registros de la tabla 
public function index(){
	return paralelo::all();
}
//método para almacenar los registros en la tabla 
public function store(request $_request){
	$request->validate([
		'nombre' =>'required|string|max:100|unique:paralelos'
	]);
    return Paralelo::create($request->all());
}
}