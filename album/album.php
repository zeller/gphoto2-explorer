<html><head></head>
<body>
<?php
$query_year = $_GET['year'];
$query_month = $_GET['month'];
$query_day = $_GET['day'];
?>
<?php
$photos_db = new PDO('sqlite:db/photos_datetime.db');
$start_datetime = date('Y-m-d', mktime(0, 0, 0, $query_month, $query_day, $query_year));
$end_datetime = date('Y-m-d', mktime(0, 0, 0, $query_month, $query_day+1, $query_year));
$sql = sprintf("SELECT * FROM photos_datetime WHERE datetime > Datetime('%s') and datetime <= Datetime('%s') ORDER BY datetime", $start_datetime, $end_datetime);
$result = $photos_db->query($sql);
foreach($result as $row) {
  $filename=$row['filename'];
  $datetime=strtotime($row['datetime']);
  $year = date('Y', $datetime);
  $month = date('n', $datetime);
  $day = date('j', $datetime);
  echo "<div style='margin:10px; float: left'><a href='photos/" . $filename . "'><img src='thumbs/" . $filename . "'/></a><br>" . date('g:i A', $datetime) . "</div>";
}
$photos_db = null;
?>

<div style='clear: both;'>
<hr>
<center>gphoto2 photo explorer</center>
</div>

</body>
</html>
