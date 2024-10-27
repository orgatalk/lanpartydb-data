# Contributing

Do you want to add or correct data to/in this database? That's great!

Here are some things to keep in mind, though.


## File Format

The data is represented in the form of flat files, formatted in
[TOML](https://toml.io/) syntax. This should make the data sufficiently
easy to read and write by both humans and computers.

Use line feeds (LF) as end-of-line characters. Do not put blank lines
(just a single line feed) at the end of each file.


## Structure

For now, the only things modeled are LAN parties, and LAN party series.

Not every party belongs to a series, though! Some are just one-time
events.


### Party Series

Party series are listed in a single file,
[`./data/series.toml`](./data/series.toml).

A series *must* specify:

* A `slug`, which is an identifier that can nicely be used in URLs and
  the filesystem. It may only contain lower-case latin characters,
  numbers, and dashes.
* A `name`, which does not have the slug's limitations.

A series *may* have:

* `alternative_names`, which is a non-empty list of alternative names of
  the party series.

Example of an entry:

```toml
[[series]]
slug = "awesome-lan"
name = "Awesome LAN"
alternative_names = ["That Awesome LAN Party"]
```


### Parties

Parties eligible for inclusion at this point have to be **public** and
**in the past**.

Each party should be defined in its own file, which should be named
`<party slug>.toml`.

If the party is part of a series, it should be in path
`./data/parties/<series slug>`; if it is not, it should be in
`./data/parties`.

A party *must* have:

* A `slug`, which is an identifier that can nicely be used in URLs and
  the filesystem. It may only contain lower-case latin characters,
  numbers, and dashes.
* A `title`, which does not have the slug's limitations.
* A start date, `start_on`. Format: `YYYY-MM-DD`, without surrounding
  double quotes.
* An end date, `end_on`. Same format as `start_on`.

A party *may* have:

* A `series_slug`, *if* the party belongs to a series (see above).
* An `organizer_entity`, if that is somewhat relevant, maybe because it
  significantly changed at some point. If its just "a bunch of people"
  for the duration of the party, you can just leave it out. Can be a
  single string or an array of multiple strings.
* A number of `seats`. This should be the number of seats the party
  actually offered, not the number of attendees.
* A number of `attendees`. This should be the number of attendees the
  party had, or the number of tickets sold if only that information is
  available.
* `online = true`, *if* the party was online-only (e.g. during a
  pandemic). In this case, the `location` section must not be provided.
* A `location` section; see below.
* A `links` section; see below.

A location section *must* have:

* A country in the form of a two-letter `country_code`, which must be an
  [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)
  value.
* A `city`.

A location section *may* have:

* The `name` of the location.
* A `zip_code`, if the country has such a thing.
* A `street` name and, if applicable, house number.
* Geographic coordinates in the form of both `latitude` and `longitude`
  values.

A links section *must* have:

* A `website`, which:

  * *must* specify `url`, which is a common URL like
    `https://www.awesomelan.example/`.
  * *can* specify `offline`, with a value of either `false` (the
    default) or `true`.


Minimal party example:

```toml
slug = "awesomemest-lan"
title = "Awesomest LAN"
start_on = 2001-07-27
end_on = 2001-07-29

[location]
country_code = "de"
city = "Büttenwarder"
```

Full party example:

```toml
slug = "awesome-lan-4"
title = "Awesome LAN #4"
series_slug = "awesome-lan"
organizer_entity = "Awesome LAN e.V."
start_on = 2000-07-28
end_on = 2000-07-30
seats = 32
attendees = 23

[location]
name = "Gasthof zum Wattwurm"
country_code = "de"
city = "Büttenwarder"
zip_code = "22999"
street = "Kirchweg 7"
latitude = 54.03847
longitude = 8.25632

[links.website]
url = "https://www.awesomelan.example/"
```
