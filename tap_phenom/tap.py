"""Phenom tap class."""

from __future__ import annotations

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_phenom import streams


class TapPhenom(Tap):
    """Singer tap for Phenom."""

    name = "tap-phenom"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "token",
            th.StringType,
            required=True,
            description="API Token for Phenom",
        ),
    ).to_dict()

    def discover_streams(self) -> list[Stream]:
        """Return a list of discovered streams.

        Returns:
            A list of Phenom streams.
        """
        return [
            streams.Jobs(tap=self),
        ]
