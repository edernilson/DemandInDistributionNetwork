# -*- coding: utf-8 -*-

"""
/***************************************************************************
 DemandaEmRedesDistribuicao
                                 A QGIS plugin
 Algoritmos para calcular demanda em nós da rede de distribuição
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

from processing.core.AlgorithmProvider import AlgorithmProvider
from processing.core.ProcessingConfig import Setting, ProcessingConfig

from calculo_vazao_agua_domiciliar_algorithm import CalculoVazaoAguaDomiciliarAlgorithm


class DemandaEmRedesDistribuicaoProvider(AlgorithmProvider):

    DESCRIPTION = u'Algorítimos para designar demandas nos nós na rede de distribuição'
    NAME = 'DemandasDeNos'
    CALCULOSABASTECIMENTOAGUA_SETTING = 'DEMANDADENOS_SETTING'


    ACTIVATE_CAA_SETTING = 'ACTIVATE_DDN_SETTING'

    def __init__(self):
        AlgorithmProvider.__init__(self)

        # Deactivate provider by default
        self.activate = True

        # Load algorithms
        self.alglist = [CalculoVazaoAguaDomiciliarAlgorithm()]
        for alg in self.alglist:
            alg.provider = self

    def initializeSettings(self):
        """In this method we add settings needed to configure our
        provider.

        Do not forget to call the parent method, since it takes care
        or automatically adding a setting for activating or
        deactivating the algorithms in the provider.
        """
        AlgorithmProvider.initializeSettings(self)
        ProcessingConfig.addSetting(
            Setting(self.getDescription(),
                    self.CALCULOSABASTECIMENTOAGUA_SETTING,
                    'Active', True))

    def unload(self):
        """Setting should be removed here, so they do not appear anymore
        when the plugin is unloaded.
        """
        AlgorithmProvider.unload(self)
        ProcessingConfig.removeSetting(
            self.CALCULOSABASTECIMENTOAGUA_SETTING)

    def getName(self):
        """This is the name that will appear on the toolbox group.

        It is also used to create the command line name of all the
        algorithms from this provider.
        """
        return self.NAME

    def getDescription(self):
        """This is the provired full name.
        """
        return self.DESCRIPTION

    def getIcon(self):
        """We return the default icon.
        """
        return AlgorithmProvider.getIcon(self)

    def _loadAlgorithms(self):
        """Here we fill the list of algorithms in self.algs.

        This method is called whenever the list of algorithms should
        be updated. If the list of algorithms can change (for instance,
        if it contains algorithms from user-defined scripts and a new
        script might have been added), you should create the list again
        here.

        In this case, since the list is always the same, we assign from
        the pre-made list. This assignment has to be done in this method
        even if the list does not change, since the self.algs list is
        cleared before calling this method.
        """
        self.algs = self.alglist
