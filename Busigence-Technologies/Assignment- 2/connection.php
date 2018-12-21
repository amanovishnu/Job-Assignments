<?php
$servername = $_POST["hostname"];
$username = $_POST["username"];
$password = $_POST["password"];

// Create connection
$conn = mysqli_connect($servername, $username, $password);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Create database
$sql = "SHOW DATABASES";
$result = mysqli_query($conn, $sql);
while ($row = mysqli_fetch_array($result)) {        
    echo $row[0]."<br>";        
}
mysqli_close($conn);
?>