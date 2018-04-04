# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CalculoVazaoAguaDomiciliar
                                 A QGIS plugin
 Calcula a somatória da vazão de água de domicílios baseado no hub mais próximo
                              -------------------
        begin                : 2018-04-04
        copyright            : (C) 2018 by Eder Nilson
        email                : eder.nilson@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Eder Nilson'
__date__ = '2018-04-04'
__copyright__ = '(C) 2018 by Eder Nilson'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CalculoVazaoAguaDomiciliar class from file CalculoVazaoAguaDomiciliar.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .calculo_vazao_agua_domiciliar import CalculoVazaoAguaDomiciliarPlugin
    return CalculoVazaoAguaDomiciliarPlugin()
