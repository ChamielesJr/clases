<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class SoapController extends Controller
{
    public function handle(Request $request)
    {
        // Rutas necesarias
        $wsdl = null; // WSDL puede ser null si se usan PHPDocs
        $options = ['uri' => $request->url()];

        // Desactiva la respuesta de Laravel
        ob_clean();

        // Incluye manualmente la clase del servicio SOAP
        require_once app_path('Http/Controllers/ServicioSoap.php');

        // Crea una instancia del servidor SOAP
        $server = new \SoapServer($wsdl, $options);

        // Registra la clase que expone los métodos SOAP
        $server->setClass(\App\Soap\ServicioSoap::class);

        // Atiende la solicitud
        $server->handle();

        exit;
    }
}
