"""
先天性の傷病治療によるC型肝炎患者に係るQOL向上等のための調査研究事業の実装
"""

from openfisca_core.periods import DAY
from openfisca_core.variables import Variable
from openfisca_japan.entities import 人物


class 先天性の傷病治療によるC型肝炎患者に係るQOL向上等のための調査研究事業(Variable):
    value_type = float
    entity = 人物
    definition_period = DAY
    label = "先天性の傷病治療によるC型肝炎患者に係るQOL向上等のための調査研究事業の調査研究協力謝金"
    reference = "https://www.med.niigata-u.ac.jp/ifc/tebiki/blood/05.html"

    def formula(対象人物, 対象期間, parameters):
        先天性の血液凝固因子異常症である = 対象人物("先天性の血液凝固因子異常症である", 対象期間)
        C型肝炎ウイルスに感染している = 対象人物("C型肝炎ウイルスに感染している", 対象期間)
        血液製剤の投与によってC型肝炎ウイルスに感染した = 対象人物("血液製剤の投与によってC型肝炎ウイルスに感染した", 対象期間)
        肝硬変や肝がんに罹患しているまたは肝移植をおこなった = 対象人物("肝硬変や肝がんに罹患しているまたは肝移植をおこなった", 対象期間)
        対象者である = 先天性の血液凝固因子異常症である \
            * C型肝炎ウイルスに感染している \
            * 血液製剤の投与によってC型肝炎ウイルスに感染した \
            * 肝硬変や肝がんに罹患しているまたは肝移植をおこなった

        謝金 = parameters(対象期間).福祉.感染症.先天性の傷病治療によるC型肝炎患者に係るQOL向上等のための調査研究事業.調査研究協力謝金
        return 対象者である * 謝金
