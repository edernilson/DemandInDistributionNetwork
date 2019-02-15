![Icone](/assets/icon.png "Icone")
# Demandas em redes de distribuição
Plugin de provedor de processamento para o QGIS 2.8 ou superior que calcula a demanda em nós da rede de distribuição.

Algorítimo para cálculo da demanda em nós (hub):
---- 
Estima a demanda nos nós(hub), baseado no consumo dos domicílios. O cálculo é realizado somando a demanda nos domicílios, e designando a demanda total em os nós da rede de distribuição. Este plugin de processamento é baseado no componente **"Distance to nearest hub (Distância para o centro mais próximo)"**.

Authors:
----
* Eder Nilson <[eder.nilson@gmail.com](mailto:eder.nilson@gmail.com)>
* Julian Cardona <[juliancardona77@gmail.com](mailto:juliancardona77@gmail.com)>

### Funcionamento: 
Dada uma camada de origem (domicílios) e outra representando pontos de destino (nós), o algoritmo calcula a distância entre cada ponto de origem (domicílios) e o ponto de detenção mais próximo (Nós), em este último é somado os consumos dos domicílios, e totalizando o valor de demanda que será designado para o NO(hub) mais próximo. Além disso, o algoritmo mostra uma camada tipo “linha”, criada pelo componente **"Distance to nearest hub"**, que identifica os domicílios (origem) e os Nós (destino), permitindo verificar facilmente a conectividade do geoprocessamento.

### Onde encontrar o algorítimo:
Uma vez instalado e ativo, este plugin adiciona o novo provedor (Algorítimos para designar demandas nos nós na rede de distribuição) na **Caixa de Ferramentas Processamento**. 
Você encontra o algorítimo na Caixa de Ferramentas sob Algorítimos para designar demandas nos nós na rede de distribuição -> Algorítimos -> Calcula a Vazão da Demanda nos Nós.

![Caixa de Ferramentas Processamento](/assets/tools_pt.png "Caixa de Ferramentas Processamento")

Configuração e Resultado:
![Configuração e Resultado](/assets/result.png "Configuração e Resultado")