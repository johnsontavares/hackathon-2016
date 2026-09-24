from crewai import Crew

from agents import (
    endocrino,
    cardiologista,
    nefrologista,
    nutricionista
)

from tasks import criar_tasks


# ============================================================
# EXECUÇÃO DA ANÁLISE
# ============================================================

def executar_analise(text):

    # Cria as tarefas utilizando o contexto recebido
    tasks = criar_tasks(text)


    # ========================================================
    # CREW
    # ========================================================

    crew = Crew(

        agents=[
            endocrino,
            cardiologista,
            nefrologista,
            nutricionista
        ],

        tasks=tasks,

        verbose=False
    )


    # ========================================================
    # EXECUÇÃO
    # ========================================================

    print(">>> INICIANDO CREW...")

    resultado = crew.kickoff()

    print(">>> CREW FINALIZOU.")


    return str(resultado)