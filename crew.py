import os
from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

load_dotenv()  # lê o .env automaticamente

# ============================================================
# MODELO GEMINI (API)
# ============================================================

llm = LLM(
    model="gemini-3.6-flash",
    temperature=0.7,
    max_retries=5  # tenta novamente antes de desistir
)


# ============================================================
# AGENTE ENDOCRINOLOGISTA
# ============================================================

endocrino = Agent(
    role="Endocrinologista",
    goal=(
        "Analisar o contexto clínico do paciente sob a perspectiva "
        "endocrinológica, considerando diagnóstico, exames, "
        "medicamentos e condições metabólicas."
    ),
    backstory=(
        "Você é um agente especialista em endocrinologia "
        "responsável por analisar informações clínicas relacionadas "
        "ao metabolismo e às doenças endócrinas."
    ),
    llm=llm,
    verbose=False
)


# ============================================================
# AGENTE CARDIOLOGISTA
# ============================================================

cardiologista = Agent(
    role="Cardiologista",
    goal=(
        "Analisar o contexto clínico do paciente sob a perspectiva "
        "cardiovascular, considerando doenças cardiovasculares, "
        "exames e medicamentos."
    ),
    backstory=(
        "Você é um agente especialista em cardiologia "
        "responsável por analisar condições cardiovasculares "
        "e suas relações com o tratamento do paciente."
    ),
    llm=llm,
    verbose=False
)


# ============================================================
# AGENTE NEFROLOGISTA
# ============================================================

nefrologista = Agent(
    role="Nefrologista",
    goal=(
        "Analisar o contexto clínico do paciente sob a perspectiva "
        "renal, considerando função renal, exames e medicamentos."
    ),
    backstory=(
        "Você é um agente especialista em nefrologia "
        "responsável por analisar condições renais "
        "e suas relações com as terapias utilizadas."
    ),
    llm=llm,
    verbose=False
)


# ============================================================
# AGENTE NUTRICIONISTA
# ============================================================

nutricionista = Agent(
    role="Nutricionista",
    goal=(
        "Analisar o contexto clínico do paciente sob a perspectiva "
        "nutricional, considerando condições clínicas, alimentação "
        "e terapias."
    ),
    backstory=(
        "Você é um agente especialista em nutrição clínica "
        "responsável por analisar aspectos nutricionais "
        "relacionados ao tratamento do paciente."
    ),
    llm=llm,
    verbose=False
)


# ============================================================
# FUNÇÃO PRINCIPAL
# ============================================================

def executar_analise(text):

    task_endocrino = Task(
        description=f"""
Analise o seguinte contexto clínico do paciente
exclusivamente sob a perspectiva endocrinológica.

CONTEXTO DO PACIENTE:

{text}

Considere:

- diabetes;
- controle glicêmico;
- medicamentos;
- exames;
- condições metabólicas.

Apresente uma análise objetiva.
""",
        expected_output="Análise endocrinológica objetiva do contexto clínico.",
        agent=endocrino
    )

    task_cardiologia = Task(
        description=f"""
Analise o seguinte contexto clínico do paciente
exclusivamente sob a perspectiva cardiovascular.

CONTEXTO DO PACIENTE:

{text}

Considere:

- doenças cardiovasculares;
- pressão arterial;
- medicamentos;
- fatores de risco;
- possíveis relações entre terapias.

Apresente uma análise objetiva.
""",
        expected_output="Análise cardiovascular objetiva do contexto clínico.",
        agent=cardiologista
    )

    task_nefrologia = Task(
        description=f"""
Analise o seguinte contexto clínico do paciente
exclusivamente sob a perspectiva nefrológica.

CONTEXTO DO PACIENTE:

{text}

Considere:

- função renal;
- medicamentos;
- condições renais;
- exames laboratoriais;
- possíveis relações entre terapias.

Apresente uma análise objetiva.
""",
        expected_output="Análise nefrológica objetiva do contexto clínico.",
        agent=nefrologista
    )

    task_nutricao = Task(
        description=f"""
Analise o seguinte contexto clínico do paciente
exclusivamente sob a perspectiva nutricional.

CONTEXTO DO PACIENTE:

{text}

Considere:

- alimentação;
- condições metabólicas;
- medicamentos;
- necessidades nutricionais;
- possíveis relações entre terapias e alimentação.

Apresente uma análise objetiva.
""",
        expected_output="Análise nutricional objetiva do contexto clínico.",
        agent=nutricionista
    )

    crew = Crew(
        agents=[endocrino, cardiologista, nefrologista, nutricionista],
        tasks=[task_endocrino, task_cardiologia, task_nefrologia, task_nutricao],
        verbose=False
    )

    print(">>> INICIANDO CREW...")
    resultado = crew.kickoff()
    print(">>> CREW FINALIZOU.")

    return str(resultado)