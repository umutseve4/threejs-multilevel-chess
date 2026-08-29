# Tri-Level Chess

An interactive three-level 3D chess prototype built with Three.js in a single HTML file.

## What it is

This is a visual interaction sandbox, **not a complete chess-rules engine**. Pieces can move between any empty squares across levels; turns and captures are tracked, but legal chess movement, check, checkmate, castling, promotion, and draw rules are intentionally out of scope.

## Run locally

Serve the repository root over HTTP, then open `index.html`:

```bash
python -m http.server 8000
```

Visit `http://localhost:8000`. An internet connection is required because Three.js is loaded from a version-pinned jsDelivr URL.

## Controls

- Drag: orbit the camera
- Wheel: zoom
- Click a piece, then a square: move
- Click an opposing piece: capture
- **Reset view**: restore the default camera
- **Reset pieces**: restore the initial layout

## Validation

The dependency-free static test suite checks the document structure, accessibility-critical controls, pinned CDN dependency, expected board invariants, and repository hygiene.

```bash
python -m unittest discover -s tests -v
```

The same suite runs on every push and pull request through GitHub Actions.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) for the change workflow and [SECURITY.md](SECURITY.md) for private vulnerability reporting guidance.
