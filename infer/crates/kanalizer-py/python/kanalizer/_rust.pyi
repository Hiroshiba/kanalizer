from typing import Final, Literal, overload

__version__: Final[str]
"""バージョン。"""

INPUT_CHARS: Final[set[str]]
"""Kanalizerの入力に使える文字の一覧。"""
OUTPUT_CHARS: Final[set[str]]
"""Kanalizerから出力されうる文字の一覧。"""

Strategy = Literal["greedy", "top_k", "top_p"]
"""デコードのアルゴリズム。"""

ErrorMode = Literal["error", "warning", "ignore"]
"""
エラー処理のモード。

- "error" : エラーを発生させる。
- "warning" : 警告を表示する。
- "ignore" : エラーを無視する。
"""

@overload
def convert(
    word: str,
    /,
    *,
    max_length: int = 32,
    on_invalid_input: ErrorMode = "error",
    on_incomplete: ErrorMode = "warning",
    strategy: Literal["greedy"] = "greedy",
) -> str: ...
@overload
def convert(
    word: str,
    /,
    *,
    max_length: int = 32,
    on_invalid_input: ErrorMode = "error",
    on_incomplete: ErrorMode = "warning",
    strategy: Literal["top_k"],
    k: int = 10,
) -> str: ...
@overload
def convert(
    word: str,
    /,
    *,
    max_length: int = 32,
    on_invalid_input: ErrorMode = "error",
    on_incomplete: ErrorMode = "warning",
    strategy: Literal["top_p"],
    p: float = 0.9,
    t: float = 1.0,
) -> str: ...
def convert(
    word: str,
    /,
    *,
    max_length: int = 32,
    strategy: Strategy = "greedy",
    on_invalid_input: ErrorMode = "error",
    on_incomplete: ErrorMode = "warning",
    **kwargs,
) -> str:
    """
    変換を行う。

    Parameters
    ----------
    word : str
        英単語。
    max_length : int, default 32
        最大の出力長。
    on_invalid_input : ErrorMode, default "error"
        入力に無効な文字が含まれていた場合の挙動。
        "error"以外の場合は、無効な文字を無視して変換を続行する。
    on_incomplete : ErrorMode, default "warning"
        変換が終了しなかった場合の挙動。
    strategy : Strategy, default "greedy"
        デコードのアルゴリズム。
    k : int, default 10
        strategy="top_k"のときのみ有効。Top-KアルゴリズムのK。
    p : float, default 0.9
        strategy="top_p"のときのみ有効。Top-PアルゴリズムのP。
    t : float, default 1.0
        strategy="top_p"のときのみ有効。Top-PアルゴリズムのTemperature。

    Raises
    ------
    ValueError
        - error_on_invalid_inputがTrue、かつ`word`が空文字列の場合。
        - error_on_invalid_inputがTrue、かつ`word`にKanalizerの入力に使えない文字が含まれている場合。
        - `max_length`が0以下の場合。
    IncompleteConversionError
        - `error_on_incomplete`がTrue、かつ変換が終了しなかった場合。
    """
    ...
