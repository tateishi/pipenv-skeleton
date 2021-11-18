def hello() -> None:
    """あいさつ

    'Hello, World'と表示する

    Returns:
        None
    """

    print("Hello, World")


def hello_message() -> None:
    """引数付きあいさつ

    'Hello, {message}'と表示する

    Args:
        message(str): 表示するメッセージ

    Returns:
        None
    """

    from . import lib
    print(f'Hello, {lib.greeting}')
