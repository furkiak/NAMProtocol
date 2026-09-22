# Mathematical status and withdrawn claims

This is an assessment of the December 2025 concept as it existed before the archive rewrite. The historical draft remains available in Git history; this document does not endorse its use.

| Historical statement | Evidence and current status |
| --- | --- |
| Binary `1010` divided as decimal `1010 / 2 = 505` | Incorrect representation. Binary `1010` is decimal 10; the first division would be `10 / 2 = 5`. |
| Appending a `0` to an odd bit string merely makes the integer even | It doubles the represented value. Recovery needs an explicit record of that operation and the original bit or byte length. |
| MAP indices and depth always reconstruct the file | Not established. The sign and choice of each `+5`/`-5` operation, the handling of negative states, termination conditions, and the exact recorded state are unspecified. Multiple choices can lead to different paths. |
| The entire file as one natural number preserves every file | `int.from_bytes` loses leading zero bytes unless the original byte length is stored; `00 0a` and `0a` both map to integer 10. Empty input needs a separate length. The tested example carries `(integer, length)` explicitly. |
| Delta coding or MAP compression is smaller than the original | No encoder, corpus, measurement method or output format exists. General lossless transforms cannot guarantee a smaller representation for every possible input. |
| A hash provides authenticity, or a salt/offset prevents analysis | An unkeyed checksum can detect accidental changes under trusted comparison, but does not by itself authenticate a hostile input. No threat model, security proof, implementation or independent review exists for the proposed transform. |
| A transformed file is securely deleted or equivalent to secret sharing | No deletion procedure, storage lifecycle, shares/threshold construction or recovery protocol exists. Arithmetic representation alone cannot erase copies of data. |

The implemented `examples/representation.py` is intentionally limited to byte/integer conversion. It is **not** the historical transform. A future educational experiment would first need a formal input/output and state-transition specification, unambiguous reversal rules, finite termination for all supported inputs, format versioning, byte-length preservation, round-trip tests over boundary/random inputs, and reproducible size measurements. Security claims would require independent cryptanalysis; passing round-trip tests would establish correctness of a mapping, not confidentiality.

No AES/RSA/ECC comparison or numeric security/performance advantage is asserted. Use established cryptography for actual secrecy and integrity.
