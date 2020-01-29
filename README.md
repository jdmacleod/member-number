# Member Number
A unique numerical identifier - for organizations that manage members. No SSN's. Uses Damm check digit.

*ex.* **123000013166**

## Rationale

Any organization that needs to keep track of people can benefit from assigning unique numbers to each individual. Although it's unfortunately all too common in the US that Social Security Numbers are used for this purpose, there are so many privacy and identity theft concerns that it does not make sense to use SSN's - especially when there is a possibility of needing to share the number in any public setting - like verifying membership at a meeting, with volunteers checking individuals in...

For organizations with less than 100K individuals that need to be tracked, this member number design may be helpful.

It's a 12-digit number that has an embedded check digit. Although keying in numbers by hand is increasingly rare, the safeguard is there.

### Design

The number is 12-digits, as detailed here:

OOO-SSSSS-RRR-C

|identifier|digits|purpose|
|---|---|---|
|O - organizational identifier|3 digits|*chapter number, region number etc.*|
|S - sequential individual identifier|5 digits|*unique per individual*|
|R - randomized numbers|3 digits|*prevent trivial guessing*|
|C - check digit, using Damm algorithm|1 digit|*catch mistyped numbers*|

Although leading zeroes are supported, avoid them when possible as they complicate data handling.

## Install

1. clone the repository
2. `source .python_path`
3. `python3 test.py`
4. `python3 generate_numbers.py`

## Bugs

If you have a suggestion, enhancement, or fix, please open an issue and/or pull request.

## Thanks

Gratitude goes to H. Michael Damm for developing and sharing his [checksum algorithm](https://en.wikipedia.org/wiki/Damm_algorithm).
