<?php

require_once('Car.php');
require_once('Account.php');

$car = new Car("ARR232", new Account("Nico Assanelli", "144"));
$car->printDataCar();