<?php
date_default_timezone_set('Etc/UTC');
$pdo = new PDO('mysql:host=localhost;dbname=speedtest', 'dbuser', '123');
$qInsert = 'INSERT INTO `speedtest`.`speedtests` ( `date`, `time`, `download`, `upload`, `ping`, `ipAddress`, `serverId`, `serverName`, `distance`, `sponsor`, `share`) 
VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)';

$stmt = $pdo->prepare($qInsert);

$fh = fopen('data/data.csv', 'r');

if ($fh !== false) {
    $rowCount = 0;
    while (($row = fgetcsv($fh, 1000)) !== false) {
        $rowCount++;
        if ($rowCount > 1) {

            $dateR = date_parse($row[3]);
            $timestamp = mktime($dateR['hour'], $dateR['minute'], $dateR['second'], $dateR['month'], $dateR['day'], $dateR['year']);
            $formattedDate = date('Y-m-d',$timestamp);
            $formattedTime = date('H:i:s', $timestamp);

            $date = $formattedDate;
            $time = $formattedTime;
            $download = $row[6];
            $upload = $row[7];
            $ping = $row[5];
            $ipAddress = $row[9];
            $serverId = $row[0];
            $serverName = $row[3];
            $distance = $row[4];
            $sponsor = $row[2];
            $share = $row[8];
            $rs = $stmt->execute([
                $date,
                $time,
                $download,
                $upload,
                $ping,
                $ipAddress,
                $serverId,
                $serverName,
                $distance,
                $sponsor,
                $share
            ]);
            var_dump($rs);
        }
    }
    fclose($fh);
}

