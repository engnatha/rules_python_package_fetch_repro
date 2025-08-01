import getpass

import click


@click.command()
@click.option(
    '--user',
    type=str,
    default=None,
    help='The user to greet.')
def main(*, user: str | None) -> None:
    """Prints a nice greeting message to a user."""
    print(f'Greetings, {user or getpass.getuser()}!')


if __name__ == '__main__':
    main()
