# GPS2City

A simple Python3-based program to find the nearest city using a serial GPS.

This program was originally made for our storm chasing mobile live streaming operations to give an idea of our location while in the field automatically.

This program is not optimized for single lookups. It loads the entire database into memory on program start to enable super fast lookups that easily keep up with a GPS stream. Future versions may optimize functionality further.

- [Setup](#setup)
  - [Cities Database](#cities-database)
  - [Database Conversion](#database-conversion)
  - [Python Libraries](#python-libraries)
- [Running](#running)
  - [Pyinstaller](#pyinstaller)

## Setup

### Cities Database

Currently, GPS2City requires a cities database from SimpleMaps. More options may be added in the future if needed.

SimpleMaps has a [US Cities Database](https://simplemaps.com/data/us-cities) and a [World Cities Database](https://simplemaps.com/data/world-cities). Either *should* work but if you do not need international cities we recommend using the US Cities Database for much faster speed.

For both databases there is a free and a paid version. The free version of the US Cities Database includes ~31k cities and the free version of the World Cities Database includes ~40k cities. The paid version of the US Cities Database is $99 and includes ~109k cities and the paid version of the World Cities Database is $199 and inclues ~1.9M cities. For each database there is also a "comprehensive" paid option which you do not need for this program. It includes more metadata about each city than is needed here.

The free versions have free but likely less frequent updates and the paid versions have free updates for 12 months with additional 12 month extensions for $39 each.

For simplicity we have not included a copy of the free versions with this repo. They are easy to download and getting them directly from the SimpleMaps website ensures you always have the most up to date copy. Please do not redistribute any copy of this software with the paid versions of the databases and remember to credit SimpleMaps in accordance to their website when distributing this software with the free database. Licensing details can be found on the pages linked above and should be included in the database downloads, please respect them.

### Database Conversion

We will convert the database from SimpleMaps to inline Python variables using the included `smtovar.py` program. After downloading the database, unzip the archive in the same directory as `smtovar.py` and `GPS2City.py`. We only need the csv file from this.

Once the `.csv`, `smtovar.py`, and `GPS2City.py` files are in the same directory, you can simply run `python3 smtovar.py` or `python smtovar.py`. **If the `.csv` file is not named `uscities.csv` you will need to edit the variable called `smdbfile` in `smtovar.py` first and change it to the proper filename.** This should only be the case if you download the World Cities Database.

### Python Libraries

GPS2City requires two libraries. They can be installed as such:

```
python3 -m pip install scipy pyserial
```

*Most systems use `python` on Windows and `python3` on macOS/Linux. If one command fails, try the other.*

## Running

GPS2City is run using:

```
python3 GPS2City.py <output file> <GPS serial port>
```

*Most systems use `python` on Windows and `python3` on macOS/Linux. If one command fails, try the other.*

`GPS2City.py` is a complete program. You can safely move it to a different location on your computer assuming the required Python libraries are available. At this point it is safe to delete the `.csv` if you wish.

### Pyinstaller

Compiling a standalone executable is only recommended if running in Windows. If on MacOS or Linux, the `GPS2City.py` file is stable enough to be used standalone. Windows systems are sometimes tricky when moving across environments.

For convenience, we have included a `.spec` file that can be used with pyinstaller. To be safe with the SimpleMaps licenses, we have decided not to include premade executables *for now*. In the future we may include executables if we can confirm we can do so while complying with the license. Even if we did include prebuilt executables, they would only be using the free databases, so we recommend making them yourself if possible.

When using pyinstaller, you should use a virtual environment. `venv` is included with Python since version `3.3`.

Create and activate a virtual environment:

**Windows:**

```
python -m venv venv
venv\Scripts\activate.bat
```

**macOS / Linux:**

```
python3 -m venv venv
source venv/bin/activate
```

*Most systems use `python` on Windows and `python3` on macOS/Linux. If one command fails, try the other.*

Then install the required packages the same way as in the [Python Libraries](#python-libraries) above.

Also install pyinstaller:

```
python -m pip install pyinstaller
```

*Most systems use `python` on Windows and `python3` on macOS/Linux. If one command fails, try the other.*

Then create a bundled binary using pyinstaller:

```
python -m PyInstaller GPS2City.spec
```

*Most systems use `python` on Windows and `python3` on macOS/Linux. If one command fails, try the other.*

The final executables will be in the `dist` directory assuming the command runs successfully. You can now copy this executable wherever you need it. It should be a completely standalone build.

**The included `.spec` file runs GPS2City in the background. No console window will be shown.** The process will need to be terminated manually once started in this method.

**Windows:**

```
GPS2City.exe <output file> <GPS serial port>
```