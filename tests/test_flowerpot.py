import flowerpot
import pytest


def test_no_flower():
    with pytest.raises(ValueError, match="Ask for a flower"):
        flowerpot.main(args=[])


def test_more_inputs():
    with pytest.raises(ValueError, match="Ask for one flower at a time"):
        flowerpot.main(["tulip", "sunflower"])


def test_invalid_flower():
    with pytest.raises(ValueError, match="Not a valid flower"):
        flowerpot.main(["tree"])


@pytest.mark.parametrize(
    ["command", "expected_output"],
    [
        pytest.param("rose", flowerpot.ROSE, id="rose"),
        pytest.param("sunflower", flowerpot.SUNFLOWER, id="sunflower"),
        pytest.param("tulip", flowerpot.TULIP, id="tulip"),
    ],
)
def test_valid_flowers(command, expected_output, capsys):
    flowerpot.main([command])

    captured = capsys.readouterr().out
    assert captured == expected_output + "\n"
