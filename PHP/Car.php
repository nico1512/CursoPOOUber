<?php

class Car {
public $id =;
public $license;
public $driver;
public $passengers;

public function __construct($license, $driver) {
    $this->license = $license;
    $this->driver = $driver;
    }
    public function PrintDataCar() {
        echo "licence: $this->lecense, conductor: {$this->driver->name}, document:
        {$this->driver->document}";
    }
}