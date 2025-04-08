<?php
// Token del bot de Telegram
define('TOKEN', '7539618081:AAHmJ5EDTDLVR6CNvihQGQ7qET4g49qgmqM');

// Capturamos el input del bot de telegram:
$input = file_get_contents('php://input');
$update = json_decode($input, true);

//Validación del msj:
if (isset($update['message'])) {
    $chatId = $update['message']['chat']['id'];
    $mensaje = strtolower(trim($update['message']['text']));

    // Respuestas de los productos según pasillo:
    if ($mensaje == 'carne' || $mensaje == 'queso' || $mensaje == 'jamón') {
        $respuesta = 'El producto se encuentra en el pasillo 1.';
    } elseif ($mensaje == 'leche' || $mensaje == 'yogurth' || $mensaje == 'cereal') {
        $respuesta = 'El producto se encuentra en el pasillo 2.';
    } elseif ($mensaje == 'bebidas' || $mensaje == 'jugos') {
        $respuesta = 'El producto se encuentra en el pasillo 3.';
    } elseif ($mensaje == 'pan' || $mensaje == 'pasteles' || $mensaje == 'tortas') {
        $respuesta = 'El producto se encuentra en el pasillo 4.';
    } elseif ($mensaje == 'detergente' || $mensaje == 'lavaloza') {
        $respuesta = 'El producto se encuentra en el pasillo 5.';
    } else {
        $respuesta = 'Lo siento, no entiendo la pregunta.';
    }

    // Enviar la respuesta al chat con el método sendMessage:
    $url = "https://api.telegram.org/bot7539618081:AAHmJ5EDTDLVR6CNvihQGQ7qET4g49qgmqM/sendMessage";
    $data = [
        'chat_id' => $chatId,
        'text' => $respuesta
    ];
    file_get_contents($url . '?' . http_build_query($data));
}
?>
