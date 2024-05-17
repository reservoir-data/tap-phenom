"""REST client handling, including PhenomStream base class."""

from __future__ import annotations

import typing as t

from singer_sdk import RESTStream
from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.pagination import BaseOffsetPaginator


class PhenomStream(RESTStream[t.Any]):
    """Phenom stream class."""

    page_size = 50

    url_base = "https://api.phenom.com"
    records_jsonpath = "$[*]"

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Get an authenticator object.

        Returns:
            The authenticator instance for this REST stream.
        """
        token: str = self.config["token"]
        return BearerTokenAuthenticator.create_for_stream(
            self,
            token=token,
        )

    @property
    def http_headers(self) -> dict[str, str]:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        return {"User-Agent": f"{self.tap_name}/{self._tap.plugin_version}"}

    def get_new_paginator(self) -> BaseOffsetPaginator:
        """Get a pagination object."""
        return BaseOffsetPaginator(start_value=0, page_size=self.page_size)

    def get_url_params(
        self,
        context: dict[str, t.Any] | None,  # noqa: ARG002
        next_page_token: int | None,
    ) -> dict[str, t.Any]:
        """Get URL query parameters.

        Args:
            context: Stream sync context.
            next_page_token: Next offset.

        Returns:
            Mapping of URL query parameters.
        """
        params: dict[str, t.Any] = {
            "limit": self.page_size,
            "offset": next_page_token or 0,
        }
        return params
