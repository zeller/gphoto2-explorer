<?php include('utils/calendar.php'); ?>
<html><head></head>
<body>

<?php
$photos_db = new PDO('sqlite:db/photos_datetime.db');
$result = $photos_db->query('SELECT * FROM photos_datetime');
$years = array();
foreach($result as $row) {
  $filename=$row['filename'];
  $datetime=strtotime($row['datetime']);
  $year = date('Y', $datetime);
  $month = date('n', $datetime);
  $day = date('j', $datetime);
  $months = array($month => array($day));
  if(array_key_exists($year, $years)) {
    $months = $years[$year];
    $url = array(sprintf('album.php?year=%d&month=%d&day=%d', $year, $month, $day), 'linked-day');
    $days = array($day => $url);
    if(array_key_exists($month, $months)) {
      $days = $months[$month];
      $days[$day] = $url;
    }
    $months[$month] = $days;
  }
  $years[$year] = $months;
}
$photos_db = null;
?>

<div>
<?php foreach($years as $year => $months) { ?>
<?php foreach($months as $month => $days) { ?>
<div style="width: 250px; height: 200px; border: 1px solid black; overflow: hidden; float: left; padding: 10px; margin: 10px"><center>
<?php
echo generate_calendar($year, $month, $days, 3); 
?>
</center></div>
<?php } ?>
<?php } ?>
</div>

<div style='clear: both;'>
<hr>
<center>gphoto2 photo explorer</center>
</div>

</body>
</html>
