# Demandas em redes de distribuição
Algoritmos para calcular demanda em nós da rede de distribuição

**Autors**: Eder Nilson <[eder.nilson@gmail.com](mailto:eder.nilson@gmail.com)>  e Julian Cardona <[juliancardona77@gmail.com](mailto:juliancardona77@gmail.com)>
**Copyright**: Eder Nilson e Julian Cardona
**URL**: [www.edernilson.com.br](http://www.edernilson.com.br)  
**Licença**: [GNU General Public License, Version 3.0](https://www.gnu.org/licenses/gpl-3.0.pt-br.html)  
**Versão Corrente**: 0.1

Algorítimo para cálculo da demanda em nós (hub):
---- 
Estima a demanda nos nós(hub), baseado no consumo dos domicílios. O cálculo é realizado somando a demanda nos domicílios, e designando a demanda total em os nós da rede de distribuição. Este plugin de processamento é baseado no componente "Distance to nearest hub (Distância para o centro mais próximo)".
### Funcionamento: 
Dada uma camada de origem (domicílios) e outra representando pontos de destino (nós), o algoritmo calcula a distância entre cada ponto de origem (domicílios) e o ponto de detenção mais próximo (Nós), em este último é somado os consumos dos domicílios, e totalizando o valor de demanda que será designado para o NO(hub) mais próximo. Além disso, o algoritmo cria uma camada tipo “linha”, que identifica os domicílios (origem) e os Nós (destino), permitindo verificar facilmente a conectividade do geoprocessamento.