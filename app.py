import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="CV | Francisco Javier García Santos",
    layout="wide",
    page_icon="🧬",
    initial_sidebar_state="expanded"
)

# --- 2. ESTILOS CSS (DISEÑO INTOCABLE) ---
st.markdown("""
    <style>
    /* --- VARIABLES DE COLOR --- */
    :root {
        --primary-color: #0A2463; /* Azul Corporativo */
    }

    /* --- TIPOGRAFÍA Y ENCABEZADOS --- */
    h1, h2, h3, h4 { color: var(--primary-color) !important; }
    .big-font { font-size:20px !important; }
    
    /* --- FOTO DE PERFIL (ÓVALO VERTICAL) --- */
    [data-testid="stSidebar"] img {
        width: 160px !important;   
        height: 210px !important;  
        border-radius: 50%;        
        border: 4px solid #0A2463;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        display: block;
        margin-left: auto;
        margin-right: auto;
        object-fit: cover; 
        margin-bottom: 20px;
    }

    /* --- BARRAS DE PROGRESO --- */
    .stProgress > div > div > div > div { background-color: var(--primary-color); }

    /* --- TARJETAS (Expanders) --- */
    .stExpander { 
        border: 1px solid #E6E9EF;
        border-radius: 12px; 
        box-shadow: 0 2px 6px rgba(0,0,0,0.05); 
        background-color: white;
        margin-bottom: 15px;
    }
    
    /* --- MÉTRICAS --- */
    div[data-testid="stMetricValue"] { font-size: 26px; color: var(--primary-color); }
    div[data-testid="stMetricLabel"] { font-size: 14px; }
    
    /* --- PROYECTO ESTRELLA --- */
    .crown-project {
        border-left: 5px solid #FFD700 !important;
        background-color: #FFFDF5 !important;
    }
    
    /* --- BOTÓN DE ENLACE DE DRIVE --- */
    .stLinkButton > a {
        background-color: #ffffff;
        color: #0A2463;
        border: 2px solid #0A2463;
        font-weight: bold;
        display: block;
        text-align: center;
        border-radius: 5px;
    }
    .stLinkButton > a:hover {
        background-color: #0A2463;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (IDENTIDAD + DOSSIER CLOUD) ---
with st.sidebar:
    try:
        image = Image.open('foto_perfil.jpg')
        st.image(image) 
    except FileNotFoundError:
        st.warning("⚠️ Sube tu foto como 'foto_perfil.jpg'")
        st.markdown('<div style="text-align: center;">👨‍🔬 (Sin Foto)</div>', unsafe_allow_html=True)

    st.title("Francisco Javier García Santos")
    st.caption("**Químico Clínico | Lead de Calidad & DevOps**")
    st.markdown("---")
    
    st.markdown("#### 🆔 Credenciales")
    st.info("**Cédula Prof:** 6731505")
    st.markdown("""
    <div style="background-color: #E6F4EA; padding: 10px; border-radius: 5px; border-left: 5px solid #1E8E3E;">
        <strong>✅ Certificación Vigente:</strong><br>
        Toma de Muestra<br>
        <small>(2022 - 2025)</small>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # --- ESTRATEGIA: ACTUALIZACIÓN SILENCIOSA (CLOUD LINK) ---
    st.markdown("#### 📂 Evidencia Documental")
    
    # ENLACE INTEGRADO (REAL)
    url_dossier = "https://drive.google.com/file/d/1UPKlftUKFoMNc_kImouIyvFsHPwkXapN/view?usp=drive_link" 
    
    st.link_button(
        label="📥 Ver Dossier Integral Certificaciones", 
        url=url_dossier, 
        use_container_width=True
    )
    st.caption("*Acceso directo a archivo controlado en la nube.*")

    st.markdown("---")
    st.markdown("#### 📬 Contacto")
    st.write("📍 **Base:** Oaxaca, México")
    st.write("📞 **Tel:** 951 396 9365")
    st.write("📧 **Email:** qbfranciscojavier@gmail.com")
    
    # --- FIN DEL SIDEBAR (Botón rojo eliminado) ---

# --- 4. CUERPO PRINCIPAL ---
st.title("🧬 Arquitectura de Sistemas de Calidad & Laboratorio Clínico")
st.markdown("""
<div style="background-color: #F4F7F9; padding: 20px; border-radius: 10px; border-left: 5px solid #0A2463; font-style: italic; font-size: 18px; color: #333;">
"Transformación Digital Integral: De la operación manual a un ecosistema de <b>Alta Disponibilidad, Trazabilidad Total y Soberanía de Datos</b>."
</div>
<br>
""", unsafe_allow_html=True)

# --- 5. ESTRUCTURA DE PESTAÑAS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "👑 La Joya de la Corona", 
    "🚀 Casos de Éxito (Operativos)", 
    "⚙️ Infraestructura DevOps", 
    "🛠️ Stack & Bitácora",
    "🧠 Liderazgo & Soft Skills"
])

# --- PESTAÑA 1: SGC INTEGRAL ---
with tab1:
    st.subheader("🏛️ Ecosistema SGC: Evolución y Futuro")
    st.markdown("Trayectoria completa de transformación digital: Del control documental estricto a la Inteligencia Artificial.")
    
    # FASE 1
    with st.expander("🏗️ Fase 1: Arquitectura de la Verdad Única (Implementado)", expanded=True):
        c1, c2 = st.columns([1, 2])
        with c1:
            st.metric("Volumen Controlado", "119 Docs", "Activos Vivos")
            st.code("Google Drive API\nAirtable Relational DB\nApps Script Automation")
        with c2:
            st.markdown("""
            **Ingeniería Documental Avanzada:**
            * **Separación de Entornos (Dev vs Prod):** Gestión dual de archivos: *Fuente Maestra* (Editable) vs *Documento Controlado* (PDF Final).
            * **Trazabilidad Criptográfica:** Implementación de **Códigos de Autorización Únicos** (ej. `20251210e`) para tokenizar aprobaciones.
            * **Base de Datos Relacional (Airtable):** Control automático de vigencia, obsolescencia y refactorización documental.
            """)

    # FASE 2
    with st.expander("🧠 Fase 2: SGC V4.0 - Arquitectura Híbrida & IA (Roadmap)", expanded=True):
        st.info("💡 **Proyecto Estratégico:** Diseño de arquitectura para eliminar dependencias locales y potenciar el análisis cognitivo.")
        
        c3, c4 = st.columns([1, 2])
        with c3:
            st.markdown("**Stack Avanzado (Next-Gen):**")
            st.code("Supabase (PostgreSQL)\nGemini 3 Pro (IA Agent)\nFirebase + Streamlit")
        with c4:
            st.markdown("""
            **Ingeniería de Software Aplicada:**
            * **Persistencia Cloud (Supabase):** PostgreSQL para eliminar conflictos de "archivo en uso" y permitir colaboración real-time.
            * **Agente Cognitivo (Gemini 3 Pro):** Integración de IA entrenada vía *Prompt Engineering* como "Master Black Belt" para análisis de Causa Raíz (Ishikawa) automatizado.
            * **Arquitectura Híbrida:** Frontend veloz en Firebase + Backend de procesamiento en Streamlit.
            """)

# --- PESTAÑA 2: CASOS OPERATIVOS ---
with tab2:
    st.subheader("📌 Soluciones de Impacto Inmediato")
    st.markdown("Implementaciones que resolvieron dolores diarios de operación, finanzas y seguridad.")
    st.divider()

    st.markdown("#### 🚑 Área: Operaciones & Logística")
    col_a, col_b = st.columns(2)
    with col_a:
        with st.expander("🔹 1. Logística Inversa: Control de Envíos (AppSheet)", expanded=True):
            st.metric("KPI: Reclamos", "< 3%", "Reducción Drástica")
            st.markdown("""
            **Dolor:** Incertidumbre en tiempos de entrega de laboratorios de referencia. Pacientes acudían sin resultados listos.
            **Solución:** App móvil de **Trazabilidad de Cadena de Custodia**.
            * Monitorización estricta (Enviado / En Proceso / Liberado).
            * **Protocolo Proactivo:** Obliga al recepcionista a notificar retrasos antes de llegada del paciente.
            * **Evidencia:** Foto obligatoria de guías de envío.
            """)
    with col_b:
        with st.expander("🔹 2. Gestión del Conocimiento: Catálogo Digital (AppSheet)", expanded=True):
            st.metric("KPI: Abandono de Área", "0 Eventos", "Autonomía Total")
            st.markdown("""
            **Dolor:** "Cuellos de botella" por personal nuevo interrumpiendo a Seniors. Recepción quedaba vacía constantemente.
            **Solución:** Base de Conocimiento Centralizada en App.
            * Digitalización del *Know-How* (Precios, Muestras, Tiempos).
            * **Impacto:** Profesionalización inmediata del personal junior y eliminación de la curva de aprendizaje.
            """)

    st.divider()

    st.markdown("#### 🛡️ Seguridad & Finanzas")
    col_c, col_d = st.columns(2)
    with col_c:
        with st.expander("🔹 3. Protocolo 'Muralla China' & Soberanía de Datos", expanded=True):
            st.metric("Activos Blindados", "104 Docs", "Propiedad Intelectual")
            st.markdown("""
            **Contexto:** Falla crítica de proveedor externo validó la estrategia de **Soberanía de Datos**.
            **Estrategia 'Actualización Silenciosa':**
            * Despliegue de enlaces directos (no archivos físicos) para control de versiones.
            * **Seguridad (DLP):** Configuración masiva de permisos: *Lectura OK / Descarga e Impresión BLOQUEADAS*.
            * **QA:** Pruebas de penetración para garantizar blindaje.
            """)
    with col_d:
        with st.expander("🔹 4. Monitoreo Financiero Event-Driven (Make)", expanded=True):
            st.markdown("""
            **Automatización:** Escucha eventos de "Vencimiento" en Trello y dispara alertas vía Webhook.
            * **Optimización:** Filtros JSON para evitar consumo innecesario de APIs (Cost Efficiency).
            * **Resultado:** Vigilancia financiera 24/7 sin intervención humana.
            """)

    st.divider()
    
    st.markdown("#### 🏆 Dirección")
    with st.expander("🔹 5. Auditoría Flash & Scoring (Checkbuster)", expanded=True):
        st.markdown("""
        **Metodología Directiva:** Solución a la "microgestión" y subjetividad.
        * **Estrategia:** Recorridos de 20 minutos generando un **Scoring Numérico (0-10)**.
        * **Impacto:** Transforma una discusión subjetiva ("está sucio") en un dato objetivo ("sacaste 7.2"). Desactiva conflictos y enfoca la mejora.
        """)

# --- PESTAÑA 3: INFRAESTRUCTURA ---
with tab3:
    st.subheader("⚙️ Infraestructura & Código (Hard Skills)")
    st.markdown("Capacidad técnica para el despliegue de **Servidores Propios (Self-Hosted)** y desarrollo a medida.")
    
    c_hard1, c_hard2 = st.columns(2)
    with c_hard1:
        st.markdown("### 🐧 Administración de Servidores (Linux)")
        st.markdown("Gestión de entornos de producción en **Ubuntu / WSL**.")
        with st.container():
            st.markdown("**🛠️ Docker & Contenedores**")
            st.progress(85)
            st.caption("Despliegue de aplicaciones aisladas (n8n, Bases de Datos) para garantizar portabilidad y limpieza del sistema operativo.")
        with st.container():
            st.markdown("**⚡ Gestión de Procesos (PM2)**")
            st.progress(90)
            st.caption("Administración de procesos demonizados (Background Daemons) para mantener servicios activos 24/7 (Keep-alive) y monitoreo de logs.")
        with st.container():
            st.markdown("**🔒 Redes & Túneles (Ngrok / Cloudflare)**")
            st.progress(88)
            st.caption("Exposición segura de servidores locales (Localhost) a internet mediante túneles encriptados para Webhooks y acceso remoto.")

    with c_hard2:
        st.markdown("### 🐍 Desarrollo de Software (Python)")
        st.markdown("Ingeniería de software aplicada a soluciones de calidad.")
        with st.container():
            st.markdown("**📦 Entornos Virtuales (venv/pip)**")
            st.progress(95)
            st.caption("Aislamiento estricto de dependencias por proyecto para evitar conflictos de versiones y garantizar reproducibilidad.")
        with st.container():
            st.markdown("**📊 Data Science (Pandas/Streamlit)**")
            st.progress(90)
            st.caption("Transformación de datos (ETL) y creación de Dashboards interactivos para visualización de KPIs de cumplimiento normativo.")
        with st.container():
            st.markdown("**💻 IDE & Versionado (VS Code + Git)**")
            st.progress(85)
            st.caption("Configuración avanzada de entorno de desarrollo (Google Antigravity), control de versiones y flujo de trabajo CI/CD.")

# --- PESTAÑA 4: STACK & BITÁCORA ---
with tab4:
    st.subheader("🧩 Arsenal de Herramientas de Negocio")
    col_izq, col_der = st.columns(2)
    with col_izq:
        st.markdown("#### ☁️ Google Workspace Elite")
        st.caption("Programación sobre la suite ofimática.")
        st.markdown("**Google Drive (Seguridad DLP)**")
        st.progress(100)
        st.info("Experto en permisos granulares y blindaje de información ante externos.")
        st.markdown("**Google Sheets + Apps Script**")
        st.progress(95)
        st.info("Desarrollo de scripts 'Append-Only' para bloquear celdas tras captura (Integridad de Datos).")
        st.markdown("**AppSheet (Desarrollo Móvil)**")
        st.progress(90)
    with col_der:
        st.markdown("#### 🗃️ Gestión & Automatización")
        st.markdown("**Airtable (Bases Relacionales)**")
        st.progress(90)
        st.caption("Diseño de esquemas relacionales para trazabilidad documental.")
        st.markdown("**n8n / Make (Integraciones)**")
        st.progress(92)
        st.caption("Orquestación de Webhooks y APIs sin servidor.")
        st.markdown("**Notion / ClickUp (Gestión)**")
        st.progress(85)
        
    st.divider()
    st.subheader("📈 Bitácora de Aprendizaje")
    st.caption("Historial de capacitación técnica continua (2022-2025).")
    try:
        df = pd.read_csv("base_datos_cursos.csv")
        st.dataframe(df, use_container_width=True, hide_index=True)
    except:
        st.warning("⚠️ Carga 'base_datos_cursos.csv'.")

# --- PESTAÑA 5: SOFT SKILLS ---
with tab5:
    st.subheader("🧠 Competencias Directivas & Factor Humano")
    st.markdown("Habilidades blandas (Soft Skills) cultivadas a través de la gestión de equipos y la práctica de la Bioética Clínica.")
    
    col_soft1, col_soft2 = st.columns(2)
    with col_soft1:
        st.markdown("### 🤝 Liderazgo & Gestión del Cambio")
        with st.expander("🔹 Liderazgo Transformacional (Digital)", expanded=True):
            st.markdown("""
            **Enfoque:** Facilitador de la transición tecnológica.
            * **Logro:** Gestión de la resistencia al cambio durante la migración de papel a Apps Móviles (Caso Catálogo Digital).
            * **Metodología:** Acompañamiento "codo a codo" con personal operativo hasta lograr su autonomía digital.
            """)
        with st.expander("🔹 Gestión de Crisis & Stakeholders"):
            st.markdown("""
            **Enfoque:** Resolución asertiva de conflictos bajo presión.
            * **Logro:** Negociación exitosa con proveedores externos (Caso CClab) manteniendo la operatividad durante fallos críticos.
            * **Comunicación:** Traducción de riesgos técnicos a lenguaje ejecutivo para la Dirección General.
            """)

    with col_soft2:
        st.markdown("### ⚖️ Bioética & Ética Profesional")
        with st.expander("🔹 Bioética Clínica & Privacidad", expanded=True):
            st.markdown("""
            **Enfoque:** Privacidad por Diseño (Privacy by Design).
            * **Práctica:** Implementación de protocolos DLP (Data Loss Prevention) en Google Drive para proteger datos sensibles de pacientes.
            * **Principio:** Garantía de confidencialidad en flujos automatizados.
            """)
        with st.expander("🔹 Inteligencia Emocional & Cultura Justa"):
            st.markdown("""
            **Enfoque:** Seguridad Psicológica en el trabajo.
            * **Práctica:** Uso de sistemas objetivos (Checkbuster Scoring) para eliminar sesgos personales en las auditorías.
            * **Resultado:** Transformación de la cultura de "buscar culpables" a "buscar causas raíz" (Root Cause Analysis).
            """)