Passwords
=========

Hash Format
-----------

``$6$mUTIUrY8$RQD7x0E6j8A5KYW/8P...``

The hash value above (truncated for brevity) can be split into several fields,
each prefixed with the ``$`` character.

The first field determines which hashing algorithm has been used.

===== =========
Value Algorithm
===== =========
1     MD5
2     Blowfish
5     SHA-256
6     SHA-512
===== =========

The second field is the salt value (``mUTIUrY8`` in this case)

The last field is the hash value obtained when the algorithm is applied to the
concatenated value of the salt and password.
