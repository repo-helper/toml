from toml.tz import TomlTz as TomlTz
from typing import Any, IO, MutableMapping, Optional, Type, Union

unicode = str
basestring = str
unichr = chr
FNFError = FileNotFoundError
FNFError = IOError
TIME_RE: Any

class TomlDecodeError(ValueError):
    msg: Any = ...
    doc: Any = ...
    pos: Any = ...
    lineno: Any = ...
    colno: Any = ...
    def __init__(self, msg: Any, doc: Any, pos: Any) -> None: ...

class CommentValue:
    val: Any = ...
    comment: Any = ...
    def __init__(self, val: Any, comment: Any, beginline: Any, _dict: Any) -> None: ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def dump(self, dump_value_func: Any): ...

def load(
        f: Union[str, list, IO[str]],
        _dict: Type[MutableMapping[str, Any]] = ...,
        decoder: Optional[TomlDecoder] = ...,
        ) -> MutableMapping[str, Any]: ...

def loads(
        s: str,
        _dict: Type[MutableMapping[str, Any]] = ...,
        decoder: Optional[TomlDecoder] = ...,
        ) -> MutableMapping[str, Any]: ...

class InlineTableDict: ...

class TomlDecoder:
    def __init__(self, _dict: Any = ...) -> None: ...
    def get_empty_table(self): ...
    def get_empty_inline_table(self): ...
    def load_inline_object(self, line: Any, currentlevel: Any, multikey: bool = ..., multibackslash: bool = ...) -> None: ...
    def load_line(self, line: Any, currentlevel: Any, multikey: Any, multibackslash: Any): ...
    def load_value(self, v: Any, strictly_valid: bool = ...): ...
    def bounded_string(self, s: Any): ...
    def load_array(self, a: Any): ...
    def preserve_comment(self, line_no: Any, key: Any, comment: Any, beginline: Any) -> None: ...
    def embed_comments(self, idx: Any, currentlevel: Any) -> None: ...

class TomlPreserveCommentDecoder(TomlDecoder):
    saved_comments: Any = ...
    def __init__(self, _dict: Any = ...) -> None: ...
    def preserve_comment(self, line_no: Any, key: Any, comment: Any, beginline: Any) -> None: ...
    def embed_comments(self, idx: Any, currentlevel: Any) -> None: ...
