import typer
import time
from rich import print
from typing_extensions import Annotated
from rich.progress import track

app = typer.Typer()


@app.command()
def main():
    currency = typer.prompt("What currency would you like to process?")
    print(f"Process currency {currency.upper()}")
    total = 0
    with typer.progressbar(range(1000)) as progress:
        for value in progress:
            # Fake processing time
            time.sleep(0.01)
            total += 1
    print(f"Processed {total} things.")


if __name__ == "__main__":
    app()
