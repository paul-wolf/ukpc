UKPC
========

[![Build Status](https://travis-ci.org/paul-wolf/ukpc.svg?branch=master)](https://travis-ci.org/paul-wolf/ukpc)

ukpc is a Python module that parses United Kingdom postcode strings into constituent parts:

* area
* district
* sector
* unit

Install:

    pip install ukpc

Currently, only Python 3.x is supported. Let me know if you need 2.7+ support. 

Usage:

```
>>> from ukpc import PostCode
pc = PostCode('NW3 2RR')
>>> str(pc)
'area=NW, district=3, sector=2, unit=RR'
```

You can get parts with properties as expected. We also provide
`PostCode.farea`, `PostCode.fdistrict`, `PostCode.fsector`,
`PostCode.funit` properties. Some people refer to sector as the
cumulative postcode up to and including sector rather than just the
sector number:

```
>>> pc.sector
'2'
>>> pc.fsector
'NW3 2'
```

`farea` and `area` are the same. `funit` is the input string, the full postcode.

There is not too much validation and no reformatting of postcodes! An exception will be thrown if the parser can't parse the string. The parser expects well-formed, upper-case strings as input. If you want to validate or format postcodes, there are some other projects that appear to do this well:

<https://github.com/andersonbispo/ukpcode> by @andersonbispo

<https://github.com/hamstah/ukpostcodeparser/blob/master/ukpostcodeparser/parser.py> by @hamstah

We also provide a utility for reading a file of postcodes. The file is expected to be csv and the first column only is read as a well-formed, upper-case postcode.

```
from ukpc.utils import iterate_file
iterate_file(path, callback=store_pc_in_database)
```

`callback` is any callable that you must provide. This will cause `store_pc_in_database()` to be called with a `PostCode` instance.

There is also a command line util that calls `iterate_file()`: 

```
(.env)➜  ukpc python -m ukpc.utils postcodes.csv  --stats
time in secs: 27
areas: 123
districts: 3089
sectors: 12302
units: 401
```

Get a list of all postcodes with geo information here:

<https://www.doogal.co.uk/PostcodeDownloads.php>

We follow this specification:

<https://www.mrs.org.uk/pdf/postcodeformat.pdf>


Testing
-------

	pip install pytest
	cd logtrace
 	pytest test.py --verbose

or

	python3 logtrace/test.py

Performance
-----------

