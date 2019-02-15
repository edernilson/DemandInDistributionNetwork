# -*- coding: utf-8 -*-

"""
/***************************************************************************
 DemandInDistributionNetwork
                                 A QGIS plugin
 Calcula demanda dos Nós baseado no consumo de domicílios mais próximo
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

import processing

from PyQt4.QtCore import QCoreApplication, QSettings
from qgis.core import QgsVectorFileWriter, QgsMapLayerRegistry, QgsExpression, QgsFeatureRequest

from processing.core.GeoAlgorithm import GeoAlgorithm
from processing.core.parameters import ParameterVector, ParameterTableField
from processing.core.outputs import OutputVector
from processing.tools import dataobjects, vector


class CalculoVazaoAguaDomiciliarAlgorithm(GeoAlgorithm):
    """Estima a demanda nos nós(hub), baseado no consumo dos domicílios. O cálculo é realizado somando a 
    demanda nos domicílios, e designando a demanda total em os nós da rede de distribuição. 
    Este plugin de processamento executa internamente o componente 'Distance to nearest hub (Distância para o centro mais próximo)'.
    """

    # Camadas (layers)
    camada_orig = None
    camada_dest = None
    # Origem
    inputFilenameOrigin = None
    coluna_orig = None
    # Destino
    inputFilenameHub = None
    coluna_dest_id = None
    coluna_dest_total = None

    # Constantes
    INPUT_LAYER_ORIGIN = 'INPUT_LAYER_ORIGIN'
    INPUT_FIELD_ORIGIN = 'INPUT_FIELD_ORIGIN'

    INPUT_LAYER_DEST = 'INPUT_LAYER_DEST'
    INPUT_FIELD_DEST_ID = 'INPUT_FIELD_DEST_ID'
    INPUT_FIELD_DEST_TOTAL = 'INPUT_FIELD_DEST_TOTAL'

    OUTPUT_LAYER = 'OUTPUT_LAYER'

    def defineCharacteristics(self):

        # The name that the user will see in the toolbox
        self.name = QCoreApplication.translate("@default", 'Calculates the Demand Flow in Nodes')

        # The branch of the toolbox under which the algorithm will appear
        self.group = QCoreApplication.translate("@default", 'Algorithms')

        # We add the input vector layer. It can have any kind of geometry
        # It is a mandatory (not optional) one, hence the False argument
        self.addParameter(ParameterVector(self.INPUT_LAYER_ORIGIN,
            QCoreApplication.translate("@default", 'Layer of origin (households):'), [ParameterVector.VECTOR_TYPE_ANY], False))

        self.addParameter(ParameterTableField(self.INPUT_FIELD_ORIGIN,
                          QCoreApplication.translate("@default", 'Field of origin of consumption in households:'), self.INPUT_LAYER_ORIGIN,
                          datatype=0, optional=False))

        self.addParameter(ParameterVector(self.INPUT_LAYER_DEST,
            QCoreApplication.translate("@default", 'Target Layer (Nodes):'), [ParameterVector.VECTOR_TYPE_ANY], False))

        self.addParameter(ParameterTableField(self.INPUT_FIELD_DEST_ID,
                          QCoreApplication.translate("@default", 'Id field (identifier) of the target layer:'), self.INPUT_LAYER_DEST,
                          optional=False))

        self.addParameter(ParameterTableField(self.INPUT_FIELD_DEST_TOTAL,
                          QCoreApplication.translate("@default", 'Destination Layer Demand Field:'), self.INPUT_LAYER_DEST,
                          datatype=0, optional=False))

        # We add a vector layer as output
        self.addOutput(OutputVector(self.OUTPUT_LAYER,
            QCoreApplication.translate("@default", 'Line output layer for nodes with shorter distance:')))

    def zeraColuna(self):
        it = self.camada_dest.getFeatures()
        index = self.camada_dest.fieldNameIndex(self.coluna_dest_total)
        self.camada_dest.startEditing()
        for feat in it:
            self.camada_dest.changeAttributeValue(feat.id(), index, 0)
        self.camada_dest.commitChanges()

    def atualizaCamadaDest(self, id, total):
        exp = QgsExpression("{} = '{}'".format(self.coluna_dest_id, str(id)))
        request = QgsFeatureRequest(exp)
        feat = self.camada_dest.getFeatures(request) 
        index = self.camada_dest.fieldNameIndex(self.coluna_dest_total)
        self.camada_dest.startEditing()
        for f in feat:
            self.camada_dest.changeAttributeValue(f.id(), index, total)
        self.camada_dest.commitChanges()

    def processAlgorithm(self, progress):
        # Origem
        self.inputFilenameOrigin = self.getParameterValue(self.INPUT_LAYER_ORIGIN)
        self.coluna_orig = self.getParameterValue(self.INPUT_FIELD_ORIGIN)

        # Destino
        self.inputFilenameHub = self.getParameterValue(self.INPUT_LAYER_DEST)
        self.coluna_dest_id = self.getParameterValue(self.INPUT_FIELD_DEST_ID)
        self.coluna_dest_total = self.getParameterValue(self.INPUT_FIELD_DEST_TOTAL)

        # Saida
        output = self.getOutputValue(self.OUTPUT_LAYER)

        # Obtem as camadas
        self.camada_orig = dataobjects.getObjectFromUri(self.inputFilenameOrigin)
        self.camada_dest = dataobjects.getObjectFromUri(self.inputFilenameHub)

        # Zera o valor do campo (field) da demanda
        self.zeraColuna()

        # Processa plugin distancetonearesthub
        camada_saida = processing.runalg('qgis:distancetonearesthub', self.camada_orig, self.camada_dest, self.coluna_dest_id, 1, 0, output)

        camada_saida = dataobjects.getObjectFromUri(camada_saida['OUTPUT'])

        indice_coluna_group = camada_saida.fieldNameIndex("HubName")
        indice_coluna_totalizar = camada_saida.fieldNameIndex(self.coluna_orig)
        ids = camada_saida.uniqueValues(indice_coluna_group,limit=10000)
        for id in ids:
            total = 0.0
            exp = QgsExpression("HubName = '{}'".format(str(id)))
            request = QgsFeatureRequest(exp)
            feat = camada_saida.getFeatures(request)
            for f in feat:
                total += f.attributes()[indice_coluna_totalizar]
            self.atualizaCamadaDest(id, total)
