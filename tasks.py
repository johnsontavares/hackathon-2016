from crewai import Task

from agents import (
    endocrino,
    cardiologista,
    nefrologista,
    nutricionista
)


# ============================================================
# CRIAÇÃO DAS TASKS
# ============================================================

def criar_tasks(text):

    # ========================================================
    # TASK ENDOCRINOLOGIA
    # ========================================================

    task_endocrino = Task(
        description=f"""
Analise o contexto clínico abaixo exclusivamente sob
a perspectiva endocrinológica.

CONTEXTO DO PACIENTE:

{text}

Considere:

- diagnósticos;
- controle glicêmico;
- exames;
- medicamentos;
- terapias;
- condições metabólicas.

Identifique informações relevantes para posterior
avaliação de conflitos diretos entre terapias.

Não invente informações que não estejam presentes
no contexto fornecido.

Não faça diagnóstico definitivo.

Apresente uma análise objetiva.
""",

        expected_output=(
            "Análise endocrinológica objetiva contendo "
            "diagnósticos, exames, medicamentos e terapias "
            "relevantes para a avaliação de conflitos terapêuticos."
        ),

        agent=endocrino
    )


    # ========================================================
    # TASK CARDIOLOGIA
    # ========================================================

    task_cardiologia = Task(
        description=f"""
Analise o contexto clínico abaixo exclusivamente sob
a perspectiva cardiovascular.

CONTEXTO DO PACIENTE:

{text}

Considere:

- doenças cardiovasculares;
- pressão arterial;
- exames;
- medicamentos;
- terapias cardiovasculares;
- relações entre terapias.

Identifique informações relevantes para posterior
avaliação de conflitos diretos entre terapias.

Não invente informações que não estejam presentes
no contexto fornecido.

Não faça diagnóstico definitivo.

Apresente uma análise objetiva.
""",

        expected_output=(
            "Análise cardiovascular objetiva contendo "
            "condições cardiovasculares, medicamentos e "
            "terapias relevantes para a avaliação de conflitos."
        ),

        agent=cardiologista
    )


    # ========================================================
    # TASK NEFROLOGIA
    # ========================================================

    task_nefrologia = Task(
        description=f"""
Analise o contexto clínico abaixo exclusivamente sob
a perspectiva nefrológica.

CONTEXTO DO PACIENTE:

{text}

Considere:

- função renal;
- exames laboratoriais;
- condições renais;
- medicamentos;
- terapias;
- relações entre terapias.

Identifique informações relevantes para posterior
avaliação de conflitos diretos entre terapias.

Não invente informações que não estejam presentes
no contexto fornecido.

Não faça diagnóstico definitivo.

Apresente uma análise objetiva.
""",

        expected_output=(
            "Análise nefrológica objetiva contendo função renal, "
            "exames, medicamentos e terapias relevantes para "
            "a avaliação de conflitos terapêuticos."
        ),

        agent=nefrologista
    )


    # ========================================================
    # TASK NUTRIÇÃO
    # ========================================================

    task_nutricao = Task(
        description=f"""
Analise o contexto clínico abaixo exclusivamente sob
a perspectiva nutricional.

CONTEXTO DO PACIENTE:

{text}

Considere:

- alimentação;
- condições metabólicas;
- medicamentos;
- terapias;
- aspectos nutricionais relacionados ao tratamento.

Identifique informações relevantes para posterior
avaliação de conflitos diretos entre terapias.

Não invente informações que não estejam presentes
no contexto fornecido.

Não faça diagnóstico definitivo.

Apresente uma análise objetiva.
""",

        expected_output=(
            "Análise nutricional objetiva contendo informações "
            "sobre alimentação, medicamentos e terapias "
            "relevantes para avaliação de conflitos."
        ),

        agent=nutricionista
    )


    return [
        task_endocrino,
        task_cardiologia,
        task_nefrologia,
        task_nutricao
    ]