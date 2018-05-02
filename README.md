# JWT_Hacking
Collection of scripts that aid in penetration testing of JSON Web Tokens

## JWTCrack.py
Used to perform a threaded dictionary attack against the secret keyword of HS256 signed tokens

``` 
    ======================
    JWTCrack
    (c)2018 Netscylla
    ======================
    Disclaimer: This program is free to use at your own risk!
                More details on the disclaimer and license available here: https://github.com/netscylla/JWT_Hacking
                
    Usage: JWTCrack.py [Encoded_JWT] [Wordlist] <Algorithm>"
           Endcoded_JWT = Base64 Encoded JWT String
           Wordlist     = Dictionary wordlist file used to bruteforce the JWT
           Algorithm    = (Optional) HMAC Algorithm, default=HS256
```
