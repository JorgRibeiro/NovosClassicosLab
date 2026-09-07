"""Verifica que o pacote e seus metadados foram instalados corretamente."""

import novos_classicos_lab


def test_installed_package_version() -> None:
    assert novos_classicos_lab.__version__ == "0.1.0"
