from crewai import Agent, LLM


# ============================================================
# MODELO LOCAL
# ============================================================

llm = LLM(
    model="ollama/llama3:8b",
    base_url="http://localhost:11434"
)


# ============================================================
# AGENTE ENDOCRINOLOGISTA
# ============================================================

endocrino = Agent(
    role="Endocrinologista",

    goal=(
        "Analisar o paciente sob a perspectiva endocrinológica, "
        "considerando diagnóstico, exames, medicamentos e condições clínicas."
    ),

    backstory=(
        "Você é um agente especialista em endocrinologia "
        "responsável por realizar análises clínicas relacionadas "
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
        "Analisar o paciente sob a perspectiva cardiovascular, "
        "considerando doenças cardiovasculares, exames e medicamentos."
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
        "Analisar o paciente sob a perspectiva renal, "
        "considerando função renal, exames e medicamentos."
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
        "Analisar o paciente sob a perspectiva nutricional, "
        "considerando condições clínicas, alimentação e terapias."
    ),

    backstory=(
        "Você é um agente especialista em nutrição clínica "
        "responsável por analisar aspectos nutricionais "
        "relacionados ao tratamento do paciente."
    ),

    llm=llm,
    verbose=False
)