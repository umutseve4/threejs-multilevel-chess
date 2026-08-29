# Contributing

## Scope

Keep the project dependency-light and understandable as a single-page Three.js prototype. A change should improve interaction, accessibility, rendering quality, documentation, or validation without presenting the sandbox as a complete chess-rules engine.

## Workflow

1. Create a focused branch.
2. Make the smallest coherent change.
3. Run `python -m unittest discover -s tests -v`.
4. Open a pull request that explains the user-visible effect and validation evidence.

For visual changes, include before/after evidence and check both desktop and narrow viewports. Do not commit generated caches, local servers, editor settings, or credentials.
