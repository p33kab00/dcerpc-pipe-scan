# dcerpc-pipe-scan

dcerpc-pipe-scan is an open source script that automates the process of identifying accessible MSRPC bindings. 

**The dcerpc-pipe-scan project is sponsored by [CGI](https://www.cgi.com/en).**

Installation
----

You can download dcerpc-pipe-scan by cloning the [Git](https://github.com/p33kab00/dcerpc-pipe-scan) repository:

    git clone https://github.com/p33kab00/dcerpc-pipe-scan.git

dcerpc-pipe-scan works out of the box with [Python](http://www.python.org/download/) version **2.6.x** and **2.7.x** on any platform.

Usage
----

Identify accessible pipes and bindings:

    $ python dcerpc-pipe-scan.py 192.168.5.131 445
    [*] dcerpc-pipe-scan 0.1
    [*] by p33kab00 (mudnorb@gmail.com)
    [*] # of checks: 43

    [+] Found accessible endpoint
    Computer Browser
    Provider:	Browser (\PIPE\browser)
    UUID:	    6bffd098-a112-3610-9833-012892020162 v0.0

    [+] Found accessible endpoint
    LSA DS access
    Provider:	lsass.exe (\PIPE\lsarpc)
    UUID:	    3919286a-b10c-11d0-9ba8-00c04fd92ef5 v0.0

    [+] Found accessible endpoint
    SAM access
    Provider:	lsass.exe (\PIPE\samr)
    UUID:	    12345778-1234-abcd-ef00-0123456789ac v1.0

    [+] Found accessible endpoint
    LSA access
    Provider:	lsass.exe (\PIPE\lsarpc)
    UUID:	    12345778-1234-abcd-ef00-0123456789ab v0.0

    [*] Found 4 possible bindings in 421 ms.
