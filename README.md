# What sdict is?
`stdict` is a console tool to lookup words in online Oxford Dictionary. `sdict` is written on Python and
requires Python 3 interpreter.

# Usage example

```shell
$ ./stdict magic

[noun]

1. The power of apparently influencing events by using mysterious or supernatural forces.

[adjective]

1. Having or apparently having supernatural powers.
2. Wonderful; exciting.

[verb]

1. Move, change, or create by or as if by magic.
```

# Options

```bash
$ sdict [options] <word>
```

Possible options are:

option | description 
---------|------------
--no-color | Do not colorize output

# Requiremets

* [Python Requests](http://docs.python-requests.org/en/master/)
* [lxml libray](https://lxml.de/)
