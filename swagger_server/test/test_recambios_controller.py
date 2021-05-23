# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.http_problem import HTTPProblem  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.recambios import Recambios  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRecambiosController(BaseTestCase):
    """RecambiosController integration test stubs"""

    def test_upm_aos_recambio_delete(self):
        """Test case for upm_aos_recambio_delete

        Elimina un recambio.
        """
        response = self.client.open(
            '/recambios/{recambioId}'.format(recambio_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_recambio_get(self):
        """Test case for upm_aos_recambio_get

        Recupera una pieza de recambio específico identificado por su ID.
        """
        response = self.client.open(
            '/recambios/{recambioId}'.format(recambio_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_recambio_options(self):
        """Test case for upm_aos_recambio_options

        Proporciona la lista de los métodos HTTP soportados.
        """
        response = self.client.open(
            '/recambios/{recambioId}'.format(recambio_id=56),
            method='OPTIONS')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_recambio_put(self):
        """Test case for upm_aos_recambio_put

        Modifica un recambio.
        """
        body = None
        headers = [('if_match', 'if_match_example')]
        response = self.client.open(
            '/recambios/{recambioId}'.format(recambio_id=56),
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_recambios_cget(self):
        """Test case for upm_aos_recambios_cget

        Obtiene todas las piezas de recambio de un taller
        """
        response = self.client.open(
            '/recambios',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_recambios_coptions(self):
        """Test case for upm_aos_recambios_coptions

        Proporciona la lista de los métodos HTTP soportados.
        """
        response = self.client.open(
            '/recambios',
            method='OPTIONS')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upm_aos_recambios_post(self):
        """Test case for upm_aos_recambios_post

        Crea un nuevo recambio
        """
        body = None
        response = self.client.open(
            '/recambios',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
