"""Stream type classes for tap-phenom."""

from __future__ import annotations

from singer_sdk import typing as th

from tap_phenom.client import PhenomStream


class Jobs(PhenomStream):
    """Jobs stream."""

    name = "jobs"
    path = "/jobs-api/v1/jobs"
    primary_keys = ("jobId",)
    replication_key = None

    schema = th.PropertiesList(
        th.Property("jobId", th.StringType),
    ).to_dict()
