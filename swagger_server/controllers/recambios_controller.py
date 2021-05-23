import connexion
import six

from swagger_server.models.http_problem import HTTPProblem  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.recambios import Recambios  # noqa: E501
from swagger_server import util
from flask import make_response

example = [
    {
        "id": 3011,
        "tallerId": 80,
        "ref": 1996,
        "unidades": 2,
        "links": {
            "parent": {
                "href": "/api/v1/Recambios",
                "rel": "listaRecambios"
            },
            "self": {
                "href": "/api/v1/Recambios/3011",
                "rel": "obtener modificar eliminar"
            }
        }
    },
    {
        "id": 3012,
        "tallerId": 80,
        "ref": 7410,
        "unidades": 4,
        "links": {
            "parent": {
                "href": "/api/v1/Recambios",
                "rel": "listaRecambios"
            },
            "self": {
                "href": "/api/v1/Recambios/3012",
                "rel": "obtener modificar eliminar"
            }
        }
    },
    {
        "id": 3013,
        "tallerId": 80,
        "ref": 1458,
        "unidades": 1,
        "links": {
            "parent": {
                "href": "/api/v1/Recambios",
                "rel": "listaRecambios"
            },
            "self": {
                "href": "/api/v1/Recambios/3013",
                "rel": "obtener modificar eliminar"
            }
        }
    },
    {
        "id": 3014,
        "tallerId": 80,
        "ref": 6714,
        "unidades": 10,
        "links": {
            "parent": {
                "href": "/api/v1/Recambios",
                "rel": "listaRecambios"
            },
            "self": {
                "href": "/api/v1/Recambios/3014",
                "rel": "obtener modificar eliminar"
            }
        }
    }
]


def upm_aos_recambio_delete(recambio_id):  # noqa: E501
    """Elimina un recambio.

    Elimina el recambio identificado por recambioId. # noqa: E501

    :param recambio_id: ID del recambio
    :type recambio_id: int

    :rtype: None
    """
    return make_response(
            "{recambio_id} successfully deleted".format(recambio_id=recambio_id), 204
        )


def upm_aos_recambio_get(recambio_id):  # noqa: E501
    """Recupera una pieza de recambio específico identificado por su ID.

    Devuelve el recambio identificado por recambioId. # noqa: E501

    :param recambio_id: ID del recambio
    :type recambio_id: int

    :rtype: Recambios
    """
    return example[1]


def upm_aos_recambio_options(recambio_id):  # noqa: E501
    """Proporciona la lista de los métodos HTTP soportados.

    Devuelve una cabecera Allow con la lista de métodos HTTP soportados (separados por comas). # noqa: E501

    :param recambio_id: ID del recambio
    :type recambio_id: int

    :rtype: None
    """
    return make_response(
            "GET,PUT,DELETE,OPTIONS", 204
        )


def upm_aos_recambio_put(body, if_match, recambio_id):  # noqa: E501
    """Modifica un recambio.

    Actualiza un recambio identificado por recambioId. # noqa: E501

    :param body: Recambios data
    :type body: dict | bytes
    :param if_match: ETag del recurso que se desea modificar
    :type if_match: str
    :param recambio_id: ID del recambio
    :type recambio_id: int

    :rtype: Recambios
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return example[2]


def upm_aos_recambios_cget():  # noqa: E501
    """Obtiene todas las piezas de recambio de un taller

     # noqa: E501


    :rtype: InlineResponse200
    """
    return example


def upm_aos_recambios_coptions():  # noqa: E501
    """Proporciona la lista de los métodos HTTP soportados.

    Devuelve una cabecera Allow con la lista de métodos HTTP soportados (separados por comas). # noqa: E501


    :rtype: None
    """
    return make_response(
            "GET,PUT,DELETE,OPTIONS", 204
        )


def upm_aos_recambios_post(body):  # noqa: E501
    """Crea un nuevo recambio

    Genera una nueva pieza de recambio para un taller previamente registrado # noqa: E501

    :param body: Recambios data
    :type body: dict | bytes

    :rtype: Recambios
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return make_response(
            "{body} successfully created".format(body=body), 201
        )
