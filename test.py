import typer

app = typer.Typer()


@app.command()
def main(name: str):
    print(f"Hello {name}")


@app.command()
def mains(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
