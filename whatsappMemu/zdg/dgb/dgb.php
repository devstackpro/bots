<?php

set_time_limit(0);

$number = $_POST['number'];
$message = $_POST['message'];
$urlTxt = 'http://localhost:8000/send-message';
$lines = explode(PHP_EOL, $number);


foreach ( $lines as $line )
{
    $data = array('number' => $number, 'message' => $message);	
    $options = array(
    'http' => array(
        'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
        'method'  => 'POST',
        'content' => http_build_query($data)
    )
    );

     //Enviar
		sleep ( rand ( 1,2)); // setar randomização de segundos
		$context  = stream_context_create($options);
		$result = file_get_contents($urlTxt, false, $context);
		if ($result === FALSE) { /* Handle error */ }
		
        //list($_,$rfirst) = explode("{", $result);
        //echo "Enviado para: " . $first . " - Lead: " . $second . " - Bloco: " . $third . " - Status do envio: " . substr($rfirst,9, 4) . "<br>";

        //foreach($lines as $line){
            //echo $line . "\n";
        //}
}		
		