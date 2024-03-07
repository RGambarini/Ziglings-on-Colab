# Ziglings-on-Colab
Zig is a general-purpose programming language and toolchain for maintaining robust, optimal, and reusable software. Ziglings are tiny broken programs written in zig that can be used to learn the language. This serves as an extension of the original repo https://codeberg.org/ziglings/exercises to provide a [Google Colab notebook](https://colab.research.google.com) for the exercises.

Link to the notebook: https://colab.research.google.com/drive/1W34UVnRQDH_2KpYVIfUvjKwPBuupp8tO?usp=sharing

Note: Copy the notebook by going 'File' > 'Save a copy in Drive' in the toolbar of the notebook.

This repo is intended to be self serving by providing the python code to generate the neccesary notebook. If not updated to the latest version, modify the python script with the appropriate link for the x86_64 architecture. The script clones the [Ziglings repo](https://codeberg.org/ziglings/exercises.git) now hosted in codeberg that can be used, preferentially, in Google Colab.

The notebook is organized so that it first installs zig into the runtime and adds the path of the installation. There is no need to keep the installation saved in your drive as zig in its nature is intended to be quick to download and install. Every code cell thereafter is automatically organized in the manner in which it is intended in the original repo. The files are written using magic commands and it is followed by an execution cell.

Other useful links:

Zig website: https://ziglang.org
Current documentation for zig: https://ziglang.org/learn/
Cookbook: https://zigcc.github.io/zig-cookbook/
