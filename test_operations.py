import functions as func
import dades


def test_ordenar_nom():
    assert (
        func.ordenar_per_nom(dades.llista) == dades.llista2_orde_nom_desc
    )


def test_ordenar_per_naiximent_fail():
    pass


def test_ordenar_per_naiximent():
    assert (
        func.ordenar_per_naiximent(dades.llista)
        == dades.llista2_ordedata_desc
    )
