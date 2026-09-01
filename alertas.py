def analisar_riscos(temperatura, umidade, vento):
    """
    Analisa as condições climáticas e retorna
    alertas e recomendações preventivas.
    """

    alertas = []
    recomendacoes = []

    # Alerta de calor
    if temperatura >= 35:
        alertas.append("ALERTA DE CALOR EXTREMO")
        recomendacoes.append(
            "Evite exposição prolongada ao sol e procure locais frescos."
        )
        recomendacoes.append(
            "Beba bastante água ao longo do dia."
        )

    elif temperatura >= 30:
        alertas.append("ATENÇÃO: TEMPERATURA ELEVADA")
        recomendacoes.append(
            "Mantenha-se hidratado e evite atividades físicas intensas."
        )

    # Alerta de frio
    elif temperatura <= 10:
        alertas.append("ALERTA DE FRIO")
        recomendacoes.append(
            "Utilize roupas adequadas para manter o corpo aquecido."
        )

    elif temperatura <= 15:
        alertas.append("ATENÇÃO: TEMPERATURA BAIXA")
        recomendacoes.append(
            "Evite exposição prolongada ao frio."
        )

    # Alerta de baixa umidade
    if umidade < 30:
        alertas.append("ALERTA: BAIXA UMIDADE DO AR")
        recomendacoes.append(
            "Aumente a ingestão de água durante o dia."
        )
        recomendacoes.append(
            "Evite ambientes muito secos e mantenha os ambientes ventilados."
        )

    elif umidade < 40:
        alertas.append("ATENÇÃO: UMIDADE BAIXA")
        recomendacoes.append(
            "Mantenha-se hidratado."
        )

    # Vento forte
    if vento >= 50:
        alertas.append("ALERTA: VENTOS FORTES")
        recomendacoes.append(
            "Evite permanecer próximo a árvores, estruturas frágeis e placas."
        )

    # Caso nenhum risco seja identificado
    if not alertas:
        alertas.append("CONDIÇÕES CLIMÁTICAS FAVORÁVEIS")
        recomendacoes.append(
            "Não foram identificadas condições climáticas de atenção."
        )
        recomendacoes.append(
            "Continue mantendo hábitos de prevenção e hidratação."
        )

    return alertas, recomendacoes