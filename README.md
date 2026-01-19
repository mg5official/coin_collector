# Coin Collector

Kleines 2D-Spiel mit **pygame**: Du steuerst ein Rechteck (Spieler) und sammelst Münzen ein, ohne durch Wände zu laufen.
Die Level-Parameter kommen aus einer **JSON-Datei** und werden mit **pydantic** validiert.
Der Start erfolgt über eine **CLI (typer)**.

## Steuerung
- Pfeiltasten **oder** WASD: bewegen
- ESC: Spiel beenden
- Fenster schließen (X): Spiel beenden

## Start
Beispiel-Level:

```bash
uv run -m coin_collector play --level src/coin_collector/levels/level_example.json --fps 60 --debug
```

Eigenes Level (Beispiel):

```bash
uv run -m coin_collector play --level src/coin_collector/levels/max_level.json
```

## Tests

```bash
uv run pytest
```

## Ruff

```bash
uv run ruff check src tests
```
