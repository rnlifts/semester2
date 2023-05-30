<?php
/* 
Ways to connect to a MySQL Database
1. MySQLi extension
2. PDO
*/
// Connecting to the Database
$servername = "sql307.epizy.com";
$username = "epiz_34153058";
$password = "OsiykM3pu4Cc";
$db='epiz_34153058_isa_prototype2';

// Create a connection
$conn = mysqli_connect($servername, $username, $password,$db);

$city = "Scottsdale"; // Replace with the city you want to get weather data for
$api_key = "01bb3d4e89ad105d1007aa5189f561a0"; // Replace with your OpenWeatherMap API key
$api_url = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=" . urlencode($city) . "&units=metric&appid=" . $api_key;

// Make a GET request to the API endpoint and get the response as a JSON string
$response = file_get_contents($api_url);

// Decode the JSON string into a PHP object
$data = json_decode($response);



$sql = "INSERT INTO weather_info(City,Temperature,Weather,Humidity,Pressure,Wind_Speed)
        VALUES ('" . $data->name . "','" . $data->main->temp . "','" . $data->weather[0]->description . "','" . $data->main->humidity . "','" . $data->main->pressure . "','" . $data->wind->speed . "')";

mysqli_query($conn,$sql);

$select_sql = "SELECT * FROM weather_info ORDER BY Date DESC  ";

  

$result = mysqli_query($conn, $select_sql);

// Fetch the weather data and store it in an array
$weather_info = array();
while ($row = mysqli_fetch_assoc($result)) {
    $weather_info[] = $row;
}

// Output the weather data
foreach ($weather_info as $data) {
    // your code to display the weather data
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="Diya_Shrestha_2331516.css">
  <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300&family=Poppins:wght@200&display=swap" rel="stylesheet">
  <title>Weather info</title>
  </head>
  <body>
    <h1 class="h1">Past Weather Information</h1>
    
    <section class="container">
    <?php $previous_date = null; // Variable to store the previous date ?>
    <?php foreach ($weather_info as $data): ?>
        <?php $current_date = date('l F j, Y', strtotime($data['Date'])); // Get the current date
            if ($current_date != $previous_date):?>
                <div class="card">
                <?php
                    $wicon =$data['Weather']; ?>
                <?php 
                if($wicon =="clear sky"): ?>
                <!-- weatherIcon.src = "https://openweathermap.org/img/wn/01d@2x.png"; -->
                <img src="https://openweathermap.org/img/wn/01d@2x.png" >
                <?php endif ?>
                <?php
                if($wicon=="overcast clouds"): ?>
                <!-- weatherIcon.src = "https://openweathermap.org/img/wn/01d@2x.png"; -->
                <img src="https://openweathermap.org/img/wn/04d@2x.png" >
                <?php endif ?>
                <?php
                if($wicon=="drizzle"): ?>
                <!-- weatherIcon.src = "https://openweathermap.org/img/wn/01d@2x.png"; -->
                <img src="https://openweathermap.org/img/wn/09d@2x.png" >
                <?php endif ?>
                <?php
                if($wicon=="thunderstorm"): ?>
                <!-- weatherIcon.src = "https://openweathermap.org/img/wn/01d@2x.png"; -->
                <img src="https://openweathermap.org/img/wn/11d@2x.png" >
                <?php endif ?>
                <?php
                if($wicon=="rain"): ?>
                <!-- weatherIcon.src = "https://openweathermap.org/img/wn/01d@2x.png"; -->
                <img src="https://openweathermap.org/img/wn/09d@2x.png" >
                <?php endif ?>
                <?php
                if($wicon=="snow"): ?>
                <!-- weatherIcon.src = "https://openweathermap.org/img/wn/01d@2x.png"; -->
                <img src="https://openweathermap.org/img/wn/13d@2x.png" >
                <?php endif ?>
                <?php
                if($wicon=="few clouds"): ?>
                <!-- weatherIcon.src = "https://openweathermap.org/img/wn/01d@2x.png"; -->
                <img src="https://openweathermap.org/img/wn/02d@2x.png" >
                <?php endif ?>
                <?php
                if($wicon=="mist"): ?>
                <!-- weatherIcon.src = "https://openweathermap.org/img/wn/01d@2x.png"; -->
                <img src="https://openweathermap.org/img/wn/50d@2x.png" >
                <?php endif ?>

                    <!-- <h2 class="wind speed"><?php echo $data['Weather'] ?></h2> -->
                    <p class="weather">Date:<?php echo $current_date ?></p>
                    <p class="icon"><?php echo $wicon ?></p>
                    <p class="wind speed">Wind speed:<?php echo $data['Wind_Speed'] ?>m/s</p>
                    <p class="pressure">City:<?php echo $data['City'] ?> </p>
                    <p class="pressure">Pressure:<?php echo $data['Pressure'] ?> hPa</p>
                    <p class="pressure">Temperature:<?php echo $data['Temperature'] ?> C </p>
                    <p class="humidity">Humidity:<?php echo $data['Humidity'] ?>% </p>
                    
                        
                </div>
                
            <?php endif; ?>
            <?php  $previous_date = $current_date; // Set the current date as the previous date for the next iteration ?>
    <?php endforeach; ?>
    </section>
  </body> 
  </html>
