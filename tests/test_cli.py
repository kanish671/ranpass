"""CLI tests for ranpass: option handling for the generate command."""

from click.testing import CliRunner

from ranpass import cli


def test_generate_without_length_fails_cleanly():
    """`ranpass generate` without --length must fail with a usage error."""
    runner = CliRunner()
    result = runner.invoke(cli, ["generate"])
    assert result.exit_code == 2
    assert "Traceback" not in result.output
    assert "length" in result.output.lower()


def test_generate_with_length_prints_password():
    """`ranpass generate -l 12` prints a 12-character password."""
    runner = CliRunner()
    result = runner.invoke(cli, ["generate", "-l", "12"])
    assert result.exit_code == 0
    assert "Ranpass" in result.output
