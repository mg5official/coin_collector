from __future__ import annotations

import typer

from .game import run_game

app = typer.Typer(help="Coin Collector – Einfache 2D-Sammelspiel-Übung")


@app.command()
def play(
    level: str = typer.Option(..., help="Pfad zur Level-JSON"),
    fps: int = typer.Option(60, help="Ziel-FPS"),
    debug: bool = typer.Option(False, help="Debug-Outlines anzeigen"),
):
    """Startet das Spiel mit den angegebenen Parametern."""
    run_game(level_path=level, fps=fps, debug=debug)


if __name__ == "__main__":
    app()
