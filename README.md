# The OrgaTalk LAN Party Database

The **OrgaTalk LAN Party Database** is an
[OrgaTalk](https://www.orgatalk.de/board/) project with the goal to
preserve (a part of) the history of LAN parties.

This repository is meant to collect the names, dates, and more public
information about any public LAN parties that have taken place in the
past.

As a next step, individual organizers of those events should be included
as well. Running a public LAN party takes quite some effort and deserves
some respect.

Not part of this repository is any software that actually does something
to present the data, like aggregating it and rendering it to a website,
for example. Creating software that will do this is part of the bigger
project, though.


## Data Format

The data is represented in the form of flat files, formatted in
[TOML](https://toml.io/) syntax. This should make the data sufficiently
easy to read and write by both humans and computers.

* Each party has its own file.
* All party series are listed together in a single file.
  * Not all parties are part of a series, though.


## How to Contribute

Everybody is invited to add public LAN parties to this database. This
means especially organizers of those parties as they should know the
facts of their events best. But especially for events far in the past
whose organizer teams have disbanded long ago, anyone is welcome to add
details before they are lost.

New or updated data can be submitted through a pull request (PR). If
that is not an option for you, feel free to get in touch with us and
submit data through another channel, and potentially in another format.

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for details.


## License

The OrgaTalk LAN Party Database is made available under the *Public
Domain Dedication and License (PDDL) v1.0*.

A copy of the license is included as a separate file,
[`LICENSE`](./LICENSE).

Its full text can also be found online at:
http://opendatacommons.org/licenses/pddl/1.0/


## Inception

The OrgaTalk LAN Party Database was initiated by Jochen Kupperschmidt in
January 2024 after thinking about creating something like this for a
long time.
