from pytest import MonkeyPatch
from ask_eight_ball import main, ask_eightball, eight_ball_answers

def test_ask_eightball(monkeypatch: MonkeyPatch) -> None:
    inputs = ["will my kids become famous", "will I live long enough to see it"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    answer1 = ask_eightball()
    assert answer1 in eight_ball_answers()
    
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    answer2 = ask_eightball()
    assert answer2 in eight_ball_answers()

    # this is kinda a flaky test, it works 19/20 times ;)
    assert answer1 != answer2

def test_main(monkeypatch: MonkeyPatch):
    monkeypatch.setattr("builtins.input", lambda _:"walter2")
    assert main() == None

