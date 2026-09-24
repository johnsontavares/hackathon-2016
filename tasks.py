from crewai import Task

from agents import (
    endocrino,
    cardiologista,
    nefrologista,
    nutricionista
)


def criar_tarefas(dados_paciente):

    tarefa_endocrino = Task(
        description=(
            "Analise os dados clínicos do paciente sob a "
            "perspectiva da Endocrinologia.\n\n"

            f"Dados do paciente:\n{dados_paciente}\n\n"

            "Apresente:\n"
            "### Análise endocrinológica\n"
            "### Terapias identificadas\n"
            "### Recomendações"
        ),

        expected_output=(
            "Análise endocrinológica contendo os principais "
            "achados, terapias identificadas e recomendações."
        ),

        agent=endocrino
    )


    tarefa_cardiologista = Task(
        description=(
            "Analise os dados clínicos do paciente sob a "
            "perspectiva da Cardiologia.\n\n"

            f"Dados do paciente:\n{dados_paciente}\n\n"

            "Apresente:\n"
            "### Análise cardiovascular\n"
            "### Terapias identificadas\n"
            "### Recomendações"
        ),

        expected_output=(
            "Análise cardiovascular contendo os principais "
            "achados, terapias identificadas e recomendações."
        ),

        agent=cardiologista
    )


    tarefa_nefrologista = Task(
        description=(
            "Analise os dados clínicos do paciente sob a "
            "perspectiva da Nefrologia.\n\n"

            f"Dados do paciente:\n{dados_paciente}\n\n"

            "Apresente:\n"
            "### Análise renal\n"
            "### Terapias identificadas\n"
            "### Recomendações"
        ),

        expected_output=(
            "Análise renal contendo os principais achados, "
            "terapias identificadas e recomendações."
        ),

        agent=nefrologista
    )


    tarefa_nutricionista = Task(
        description=(
            "Analise os dados clínicos do paciente sob a "
            "perspectiva da Nutrição.\n\n"

            f"Dados do paciente:\n{dados_paciente}\n\n"

            "Apresente:\n"
            "### Avaliação nutricional\n"
            "### Recomendações alimentares"
        ),

        expected_output=(
            "Avaliação nutricional e recomendações alimentares."
        ),

        agent=nutricionista
    )


    return [
        tarefa_endocrino,
        tarefa_cardiologista,
        tarefa_nefrologista,
        tarefa_nutricionista
    ]