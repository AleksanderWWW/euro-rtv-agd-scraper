import functools
from typing import Callable


ComposableFunction = Callable[[str], str]


def compose(*functions: ComposableFunction) -> ComposableFunction:
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions)
