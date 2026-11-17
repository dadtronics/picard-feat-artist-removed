# Feat. Artists Removed (Picard 3.0)

MusicBrainz Picard plugin that removes `(feat. X)`-style credit suffixes
from track titles, e.g. `Song (feat. Someone) (Deluxe)` → `Song (Deluxe)`.

Original plugin: **Lukas Lalinsky / Bryan Toth**. This repository is a
faithful port to the Picard 3.0 plugin format (logic unchanged; only the
registration/entry point was updated to `enable(api)` + the new metadata
processor extension points).

## Install (Picard 3.x)

Option A — let Picard do it (GUI: Options → Plugins → "Install from URL",
or CLI):

```
picard-cli plugins install https://github.com/dadtronics/picard-feat-artist-removed
```

Option B — clone into the plugins directory:

```
git clone https://github.com/dadtronics/picard-feat-artist-removed "%APPDATA%/MusicBrainz/Picard/plugins3/featartist"
```

(Delete the `.git` folder inside afterwards if you like.)

Then enable the plugin (Options → Plugins, or `picard-cli plugins enable`).

## Notes

- Runs as a track-level metadata processor; changes are in-memory until
  you save the tags.
- Matching is case-insensitive and only touches `title`.

## License

GPL-2.0-or-later. See `LICENSE`.
