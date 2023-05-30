<?php
$servername = "sql313.epizy.com";
$username = "epiz_34253770";
$password = "s9RPLCj0RKDvq";
$db = 'epiz_34253770_weather_datadb';

// Create a connection
$conn = mysqli_connect($servername, $username, $password, $db);

$city = "Doncaster";

// Define the SQL SELECT statement
$sql = "SELECT * FROM weather_data
        WHERE name = '$city'
        GROUP BY name, DATE(date)
        ORDER BY date DESC LIMIT 6";

// Execute the SQL statement
$result = mysqli_query($conn, $sql);

// Fetch the weather data and store it in an array
$weather_data = array();
while ($row = mysqli_fetch_assoc($result)) {
    $weather_data[] = $row;
}

// Check if data is not present in the database
if (empty($weather_data)) {
    $api_key = "526f1ac5cce94c390f972b13c12309ce"; // Replace with your OpenWeatherMap API key
    $api_url = "https://api.openweathermap.org/data/2.5/weather?q=" . urlencode($city) . "&units=metric&appid=" . $api_key;

    // Make a GET request to the API endpoint and get the response as a JSON string
    $response = file_get_contents($api_url);

    // Decode the JSON string into a PHP object
    $data = json_decode($response, true);

    // Define the SQL INSERT statement
    $insert_sql = "INSERT INTO weather_data(date, temperature, max_temperature, humidity, pressure, wind, name, weather_description)
                   VALUES (CURRENT_TIMESTAMP, '" . $data['main']['temp'] . "','" . $data['main']['temp_max'] . "','" . $data['main']['humidity'] . "','" . $data['main']['pressure'] . "', '" . $data['wind']['speed'] . "','" . $data['name'] . "','" . $data['weather'][0]['description'] . "')";

    // Execute the SQL statement
    mysqli_query($conn, $insert_sql);

    // Fetch the newly inserted weather data and add it to the array
    $new_weather_data = array();
    $new_weather_data[] = mysqli_fetch_assoc(mysqli_query($conn, "SELECT * FROM weather_data WHERE name = '$city' ORDER BY date DESC LIMIT 1"));
    $weather_data = array_merge($new_weather_data, $weather_data);
}

// Close the database connection
mysqli_close($conn);
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Data</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="hello.css">
</head>

<body>
    <div class="container">
        <div class="past-weather">
            <h2>Past Weather</h2>
            <?php $previous_date = null; // Variable to store the previous date ?>
            <?php foreach ($weather_data as $data): ?>
                <?php $current_date = date('l, F j, Y', strtotime($data['date'])); // Get the current date
                if ($current_date != $previous_date): ?>
                    <div class="weather-boxes">
                        <div class="weather-box">
                            <div class="weather-date"><?= $data['date'] ?></div>
                            <div class="weather-city">City: <?= $data['name'] ?></div>
                            <div class="weather-description">Weather: <?= $data['weather_description'] ?></div>
                            <div class="weather-temperature">Temperature: <?= $data['temperature'] ?>&deg;C</div>
                            <div class="weather-humidity">Humidity: <?= $data['humidity'] ?>% Humidity</div>
                            <div class="weather-pressure">Pressure: <?= $data['pressure'] ?> hPa Pressure</div>
                            <div class="weather-wind">Wind-speed: <?= $data['wind'] ?> m/s Wind</div>
                        </div>
                    </div>
                <?php endif; ?>
                <?php $previous_date = $current_date; // Set the current date as the previous date for the next iteration ?>
            <?php endforeach; ?>
        </div>
    </div>
</body>

</html>
