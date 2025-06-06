<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use Tests\TestCase;
use Models\Paralelo;

class ParaleloTest extends TestCase
{
    /**
     * A basic feature test example.
     */
    public function test_example(): void
    {
        //creamos dos paralelos de prueba 
        Paralelo::factory()->create(['nombre'=> 'P1']);
        Paralelo::factory()->create(['nombre'=> 'P2']);

        //procederemos a cambiar la ruta de raiz por la ruta de paralelos
        //$response = $this->get('/');
        $response = $this->getJson('/api/paralelos');

        //procedemos a enviar una respuesta de exito
        //$response->assertStatus(200);
        
        $response->assertStatus(200)
        ->assertJsonFragment(['nombre'=> 'P1'])
        ->assertJsonFragment(['nombre'=> 'P2']);

    }
}
