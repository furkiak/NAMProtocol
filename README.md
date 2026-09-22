# N.A.M. / D.A.H.A. — historical arithmetic mapping proposal

> **Archived research note, not an encryption protocol.** The proposed offset/MAP transform was never specified or implemented well enough to demonstrate reversibility, compression, confidentiality, authentication, secure deletion, or resistance to attacks. Do not use it to protect data. For real applications, use established, reviewed cryptographic libraries and protocols.

![Status: archived concept](https://img.shields.io/badge/status-archived%20concept-667085) ![License: MIT](https://img.shields.io/badge/license-MIT-blue)

N.A.M. (Natural Arithmetic Mapping; Turkish: D.A.H.A., Doğal Aritmetik Haritalama Algoritması) began as a thought experiment about representing a byte sequence as a non-negative integer and recording arithmetic steps. The original draft mixed binary and decimal notation and left critical reconstruction rules undefined. This repository now preserves the **question**, a small correct representation example, and an explicit record of what remains unproven. There is no production package or security claim.

## Reproduce the only implemented example

Requires Python 3.10+ from the standard library; no install or external service.

```sh
python examples/representation.py
python -m unittest discover -s tests -v
```

Expected demo output:

```text
bits 1010 -> decimal 10
bytes 000a -> integer 10, length 2 -> bytes 000a
```

The bit string `1010` has decimal value **10**, not 1010. Byte sequence `00 0a` also has integer value 10; its two-byte length must be retained to reconstruct the leading zero. This is ordinary encoding, **not** the proposed MAP/OFFSET transform or a cryptographic operation. The tests cover empty data, leading zeros, boundary values and invalid lengths.

```text
CURRENT, TESTED: byte sequence --(integer + byte length)--> exact byte sequence
HISTORICAL IDEA: integer --(offset steps / MAP / depth)--> ? --(reverse)--> integer
                                                    ^ no defined, tested format
```

The [mathematical status note](docs/mathematical-status.md) explains the missing rules and why the earlier security and compression assertions were withdrawn. It also lists the requirements for any future experiment. The only existing implementation is the representation example above. There is no `Test.py`, benchmark, demo website, or supported encrypted-file format.

## Maintenance status

This is a read-only historical concept. Bug reports about the representation example can include Python version, input bytes **without private data**, expected result and actual result; no future development or response time is promised. A new reversible transform would need a complete specification, round-trip tests, adversarial review and clear separation from cryptography before being described as a working protocol. The repository may be marked archived on GitHub after the local changes are published.

## Türkçe özet

N.A.M. / D.A.H.A. eski bir aritmetik dönüşüm fikridir; çalışan veya güvenli bir şifreleme protokolü değildir. Önceki metindeki ikilik `1010` örneği yanlışlıkla ondalık 1010 gibi işlenmişti. Bu depoda yalnızca bayt dizisini, uzunluğunu saklayarak tam sayıya çevirip geri alma örneği çalışır. Başta sıfır baytları korumak için uzunluk gereklidir. MAP, OFFSET, DEPTH, sıkıştırma, veri yok etme ve saldırı dayanımı için kanıtlanmış bir uygulama yoktur. Gizli veri korumak için kullanmayın; ayrıntılar [matematik durumu](docs/mathematical-status.md) dosyasındadır.

Author: Furkan Akça. Licensed under [MIT](LICENSE). See [SECURITY.md](SECURITY.md) for reporting and usage boundaries.
