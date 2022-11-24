# Turtle Plotter
This repository contains python codes for plotting a svg file or robot code using turtle graphics. 

![plot](https://github.com/aras-labs/Turtle-Plotter/blob/main/assets/plot.png?raw=true)

## Installation
1. Install python
2. Install the requirements
```
pip install -r requirements.txt
```

## Usage
```
$> python plot.py -h
usage: Turtle Plotter [-h] -f FILE -t {code,svg}

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Input file.
  -t {code,svg}, --type {code,svg}
                        Input type.
  -c CONFIG_FILE, --config CONFIG_FILE
                        Plotter's Config file.
```

### Plotting SVG File
```
python plot.py -t svg -f files/output.svg
```

### Plotting Code File
```
python plot.py -t code -f files/code.txt -c files/kamal.properties.txt
```