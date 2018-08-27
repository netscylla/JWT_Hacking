# JWT_Hacking
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fnetscylla%2FJWT_Hacking.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fnetscylla%2FJWT_Hacking?ref=badge_shield)

Collection of scripts that aid in penetration testing of JSON Web Tokens

## JWTCrack.py
Used to perform a threaded dictionary attack against the secret keyword of HS256 signed tokens

``` 
usage: JWTCrack.py [-h] [-a {HS256,HS384,HS512}] [-t THREADS]
                   encoded_jwt wordlist

====================== JWTCrack (c)2018 Netscylla ======================
Disclaimer: This program is free to use at your own risk! More details on the
disclaimer and license available here:
https://github.com/netscylla/JWT_Hacking

positional arguments:
  encoded_jwt           Base64 Encoded JWT String
  wordlist              Dictionary wordlist file used to bruteforce the JWT

optional arguments:
  -h, --help            show this help message and exit
  -a {HS256,HS384,HS512}, --algorithm {HS256,HS384,HS512}
                        HMAC Algorithm (default: HS256)
  -t THREADS, --threads THREADS
                        Number of threads (default: 8)
```


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fnetscylla%2FJWT_Hacking.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fnetscylla%2FJWT_Hacking?ref=badge_large)