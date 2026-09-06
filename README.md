<h1 align="center">Tri-Level Chess</h1>

<p align="center">
  Chess played across three stacked boards, in your browser, from a single HTML file.<br>
  Orbit the stack, lift a piece off one level and set it down on another.<br>
  A visual interaction sandbox — <b>not</b> a chess-rules engine.
</p>

<p align="center">
  <a href="https://github.com/umutseve4/threejs-multilevel-chess/actions/workflows/static-validation.yml"><img src="https://github.com/umutseve4/threejs-multilevel-chess/actions/workflows/static-validation.yml/badge.svg" alt="Static validation"></a>
  <img src="https://img.shields.io/badge/board%20levels-3-FF4D4F?style=flat-square" alt="3 levels">
  <img src="https://img.shields.io/badge/source%20files-1%20HTML-FF4D4F?style=flat-square" alt="1 HTML file">
</p>

---

## Run it in 30 seconds

```bash
git clone https://github.com/umutseve4/threejs-multilevel-chess && cd threejs-multilevel-chess
python -m http.server 8000
```

Open http://localhost:8000. An internet connection is required — Three.js loads
from a version-pinned jsDelivr URL.

## Controls

| Input | Action |
|---|---|
| Drag | Orbit the camera |
| Wheel | Zoom |
| Click a piece, then a square | Move |
| Click an opposing piece | Capture |
| **Reset view** | Restore the default camera |
| **Reset pieces** | Restore the initial layout |

## Validation

```bash
python -m unittest discover -s tests -v
```

The dependency-free static suite checks document structure,
accessibility-critical controls, the pinned CDN dependency, expected board
invariants, and repository hygiene. It runs on every push and pull request
through GitHub Actions.

## Limits

- **Not a rules engine.** Pieces can move between any empty squares across levels. Turns and captures are tracked; legal chess movement, check, checkmate, castling, promotion, and draw rules are intentionally out of scope.
- No AI opponent, no move history, no notation, no save/load, no multiplayer.
- Requires network access on load (CDN-hosted Three.js) — it will not run fully offline.
- The test suite is static: it inspects the document, not the rendered scene. Browser/GPU behavior needs a separate manual pass.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the change workflow and
[SECURITY.md](SECURITY.md) for private vulnerability reporting.
