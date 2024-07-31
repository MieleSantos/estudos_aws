import os


def log(message: str):

    print(os.environ["MINHA_VAR"])
    print(f"Log de execução apos github action: {message}")
