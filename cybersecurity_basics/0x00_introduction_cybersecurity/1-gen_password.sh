#!/bin/bash
tr -dc '[:alnum:]' < /dev/urandom | fold -w "$1" | head -n 1 #script generates a strong random password
# tr -dc '[:alnum:]' < /dev/urandom: - /dev/urandom: This file is a stream of raw random noise from the OS kernel. It outputs binary garbage.

# tr (Translate): It used to filter the noise.

# -d (Delete): Delete any character that does NOT match the set.

# -c (Complement): Invert the set.

# Result: "Read random noise, delete everything that is not a letter or number." We now have an infinite stream of random alphanumeric characters.

# | fold -w "$1": The stream is just one long infinite line. fold wraps text to fit a specific width.

# -w "$1": Wrap the lines at the width specified by the user (e.g., 20 characters).

# Why use this? It naturally adds a newline character at the end of the chunk, which helps format the output correctly without using printf.

# | head -n 1: Since the stream is infinite, we need to stop reading. head -n 1 grabs exactly the first line (which is $1 characters long thanks to fold) and then closes the pipe.
