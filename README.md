# PyCut

PyCut is a pizza-making puzzle game made for the IGME-582 final project at the [Rochester Institute of Technology](https://www.rit.edu). This game teaches basic units of measure to children inspired by the Pizza Pass minigame of *[Logical Journey of the Zoombinis](https://en.wikipedia.org/wiki/Zoombinis)* (1996).

![Pizza Pass minigame](https://upload.wikimedia.org/wikipedia/en/b/bd/Original_Zoombinis_Pizza_Pass.jpg)

## About the project

This project is a game designed to run on the One Laptop per Child XO laptops. You can find more information about the scope, background, and context of the project on our [wiki](https://github.com/jflory7/PyCut/wiki).

You can also find more information about the project on the [SugarLabs wiki](https://wiki.sugarlabs.org/go/Activities/PyCut). We also hope to deploy this on the official SugarLabs download site in the near future.


## Prerequisites

### On the XO

In order to play PyCut for the XO, you will need to build the game by running these commands in a terminal.

```
$ ./setup.py genpot
$ ./setup.py build
```

### On another computer

You will need to isntall some dependencies in order to play PyCut on your system.

#### Fedora / CentOS / Red Hat-based distributions

```
$ sudo dnf install pygame
```

#### Debian / Ubuntu / apt-based distributions

```
$ sudo apt-get install python-pygame
```

## Running

To run the game, you will need to execute the main Python class.

```
$ ./PyCut.py
```

## Deploying

### On the XO

```
$ ./setup.py install
```

### On another computer

If you want to distribute the game onto another XO, execute this command.

```
$ ./setup.py dist_xo
```

Otherwise, if you want to distribute the game onto a regular computer, run this one.

```
$ ./setup.py dist
```

## Past examples

* [brendan-w/planetary](https://github.com/brendan-w/planetary)
* [ColdSauce/golems](https://github.com/ColdSauce/golems)
* [MattGuerrette/ZeroQuest](https://github.com/MattGuerrette/ZeroQuest)