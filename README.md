# Agregação-para-dispositivos-IoT

## Description

The project consists of developing a platform that gather's data from several Internet of Thing (IoT) devices through several specilized progams in collection, agregation, processing, etc.

The project is part of the evaluation of the classes
 - Sistemas Distribuídos em Grande Escala (SDGE)
 - Paradigmas de Sistemas Distribuídos (PSD)

which are part of the SD profile on the course MEI in the University of Minho.

## Authors

- [Ana Rita Peixoto](https://github.com/rita-peixoto)
- [André Gonçalves](https://github.com/andredsg)
- [Henrique Neto](https://github.com/K1yps)
- [Márcia Teixeira](https://github.com/teixeiramarcia)

## Build

### Aggregator
    java -cp src/aggregator:jeromq-0.5.2.jar src/aggregator/Aggregator.java

### Collector
    ./rebar3 compile
    erl -pa out/default/lib/chumak/ebin -eval # erlang terminal
    c("src/collector/collector.erl"). % compile collector module
    collector:start(). % runs a collector

### Device
    erl -pa out/default/lib/chumak/ebin -eval # erlang terminal
    c("src/device/device.erl"). % compile device module
    device:main("U1", "P1", "T1"). % create a single device
    device:run_multiple_devices("DevicesInfoExample.txt"). % run the multiple devices as are in file

### Client
    ...
