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
"""

__author__ = 'Eder Nilson'
__date__ = '2018-04-04'
__copyright__ = '(C) 2018 by Eder Nilson'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect

from processing.core.Processing import Processing

from demanda_em_redes_distribuicao_provider import DemandaEmRedesDistribuicaoProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class DemandaEmRedesDistribuicaoPlugin:

    def __init__(self):
        self.provider = DemandaEmRedesDistribuicaoProvider()

    def initGui(self):
        Processing.addProvider(self.provider)

    def unload(self):
        Processing.removeProvider(self.provider)
