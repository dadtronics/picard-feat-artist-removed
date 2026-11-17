# -*- coding: utf-8 -*-
# Feat. Artists Removed for MusicBrainz Picard (Picard 3.0 format).
#
# Original plugin by Lukas Lalinsky and Bryan Toth (v0.4, 2.x API).
# Ported to the Picard 3.0 (plugins3) format.
#
# Removes "(feat. X)" from track titles. Substitution is case insensitive.

import re

from picard import log

_feat_re = re.compile(r"\s+\(feat\. [^)]*\)", re.IGNORECASE)


def remove_featartists(track, metadata, track_node, release_node=None):
    metadata["title"] = _feat_re.sub("", metadata["title"])


def enable(api) -> None:
    """Picard 3.0 entry point: register the track metadata processor."""
    from picard.metadata import track_metadata_processors

    track_metadata_processors.register(__name__, remove_featartists)
    log.info("Feat. Artists Removed: enabled")


def disable() -> None:
    log.info("Feat. Artists Removed: disabled")
