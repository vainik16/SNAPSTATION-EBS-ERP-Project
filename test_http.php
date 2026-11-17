<?php
$ch = curl_init('http://localhost:8000/index.php');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
$html = curl_exec($ch);
preg_match('/<title>(.*?)<\/title>/is', $html, $m);
echo "Page Title: " . ($m[1] ?? 'None') . "\n";
if (strpos($html, 'username') !== false || strpos($html, 'login') !== false) {
    echo "Login form is present on page!\n";
}
