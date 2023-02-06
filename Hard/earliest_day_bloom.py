class Solution(object):
    def earliestFullBloom(self, tempos_plantio, tempos_crescimento):
        tempos_crescimento_e_plantio = zip(tempos_crescimento, tempos_plantio)
        tempos_crescimento_e_plantio = sorted(tempos_crescimento_e_plantio, reverse=True) # planta primeiro quem demora mais pra crescer
        dia_hoje = 0
        dias_all_bloom = 0
        for tcrescimento, tplantio in tempos_crescimento_e_plantio:
            tempo_total = dia_hoje + tplantio + tcrescimento
            dias_all_bloom = max(dias_all_bloom, tempo_total)
            dia_hoje += tplantio
        return dias_all_bloom
   
# link do exercício: https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
