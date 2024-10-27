#!/usr/bin/env python3

"""Return error code if parties are found that are not in the past.

Author: Jochen Kupperschmidt
"""

from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date
from pathlib import Path
import sys
import tomllib


@dataclass(frozen=True, slots=True)
class Party:
    path: Path
    slug: str
    title: str
    end_on: date


def main(filenames: list[str]) -> None:
    if not filenames:
        return

    paths = map(Path, filenames)
    parties = map(load_party, paths)
    parties_not_over = select_parties_not_over(parties)

    if parties_not_over:
        print_parties_not_in_past(parties_not_over)
        sys.exit(1)


def load_party(path: Path) -> Party:
    toml = path.read_text()
    data = tomllib.loads(toml)

    return Party(
        path=path,
        slug=data['slug'],
        title=data['title'],
        end_on=data['end_on'],
    )


def select_parties_not_over(parties: Iterable[Party]) -> list[Party]:
    today = date.today()
    return list(filter(lambda party: party.end_on > today, parties))


def print_parties_not_in_past(parties: Iterable[Party]) -> None:
    write_error_line('Found parties not in the past:')
    for party in parties:
        write_error_line(f'+ "{party.title}" ends on {party.end_on}')
        write_error_line(f'  - file: {party.path}')


def write_error_line(text: str) -> None:
    sys.stderr.write(f'{text}\n')


if __name__ == '__main__':
    filenames = sys.argv[1:]
    main(filenames)
