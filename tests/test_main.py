from pytest import MonkeyPatch
from question_name import main, ask_name

def test_ask_name(monkeypatch: MonkeyPatch) -> None:
    inputs = ["walter", "noah"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    assert ask_name() == "hello walter"
    
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    assert ask_name() == "Hallo Noahtje!"


def test_main(monkeypatch: MonkeyPatch):
    monkeypatch.setattr("builtins.input", lambda _:"walter2")
    assert main() == None

