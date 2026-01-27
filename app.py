import streamlit as st
import pandas as pd
from PIL import Image
import backend  # <--- TU CEREBRO CONECTADO

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="CV | Francisco Javier García Santos",
    layout="wide",
    page_icon="🧬",
    initial_sidebar_state="expanded"
)

# --- 2. MOTOR DE ESTILOS ---
def cargar_estilos():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    :root { --primary-color: #0A2463; --accent-color: #E63946; --success-color: #2A9D8F; }
    html, body, [class*="css"] { font-family: 'Roboto', sans-serif; }
    
    /* HEADER FIJO */
    .sticky-header {
        position: fixed; top: 0; left: 0; width: 100%;
        background-color: white; z-index: 90; 
        padding: 15px 20px; border-bottom: 3px solid #0A2463;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 90px;
        display: flex; flex-direction: column; justify-content: center;
        transition: padding-left 0.3s ease; 
    }
    section[data-testid="stSidebar"] { z-index: 100 !important; }
    header[data-testid="stHeader"] { z-index: 101 !important; background-color: transparent !important; }
    
    @media (min-width: 992px) { .sticky-header { padding-left: 22rem; } }
    @media (min-width: 576px) and (max-width: 991px) { .sticky-header { padding-left: 6rem; } }
    @media (max-width: 575px) { .sticky-header { padding-left: 1rem; height: auto; padding-top: 3.5rem; } .header-title { font-size: 18px !important; } }
    
    .block-container { padding-top: 120px !important; padding-bottom: 2rem !important; }
    
    .header-title { color: var(--primary-color) !important; font-size: 26px !important; font-weight: 700; margin: 0; }
    .header-subtitle { color: #555; font-size: 15px !important; font-weight: 300; margin: 0; }
    h1, h2, h3, h4 { color: var(--primary-color) !important; }
    
    [data-testid="stSidebar"] img { width: 160px !important; height: 210px !important; border-radius: 50%; border: 4px solid #0A2463; object-fit: cover; margin: 0 auto 20px auto; display: block; }
    .stExpander { border: 1px solid #E6E9EF; border-radius: 12px; background: white; margin-bottom: 15px; }
    .cert-box { border-left: 5px solid var(--success-color); background-color: #F1FAEE; padding: 15px; border-radius: 5px; margin-bottom: 10px; }
    .stLinkButton > a { background: white; color: #0A2463; border: 2px solid #0A2463; font-weight: bold; text-align: center; border-radius: 5px; }
    .stLinkButton > a:hover { background: #0A2463; color: white; }
    </style>
    """, unsafe_allow_html=True)

cargar_estilos()

# --- 3. SIDEBAR COMPLETO ---
with st.sidebar:
    try:
        image = Image.open('foto_perfil.jpg')
        st.image(image) 
    except FileNotFoundError:
        st.markdown('<div style="text-align: center; font-size: 50px;">👨‍🔬</div>', unsafe_allow_html=True)

    st.title("Francisco Javier García Santos")
    st.markdown("**Químico Biólogo & Técnico en Sistemas (SEP)**")
    st.caption("*Especialista en Automatización de Procesos & Calidad*")
    st.markdown("---")
    
    st.markdown("#### 🆔 Credenciales Oficiales")
    st.info("**Cédula QFB:** 6731505")
    st.success("**Dip. Téc. Sistemas:** SEP-DGTVE (421 Hrs)") 
    
    # CORRECCIÓN VIGENCIA
    st.markdown("""
    <div style="background-color: #F0F2F6; padding: 10px; border-radius: 5px; border-left: 5px solid #0A2463;">
        <strong>📜 Certificación Técnica:</strong><br>
        Toma de Muestras de Sangre Venosa<br>
        <small style="color: #555;">Periodo: 2023 - 2025</small>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### 📂 Evidencia Documental")
    url_dossier = "https://drive.google.com/file/d/1UPKlftUKFoMNc_kImouIyvFsHPwkXapN/view?usp=drive_link" 
    st.link_button(label="📥 Dossier Técnico (Versión Pública)", url=url_dossier, use_container_width=True, help="Datos sensibles protegidos.")
    st.caption("🔒 **Nota de Seguridad:**")
    st.markdown('<div style="font-size: 12px; color: #666;">Minimización de Datos aplicada.</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 📬 Contacto")
    st.write("📍 **Base:** Oaxaca, México")
    st.write("📧 **Email:** qbfranciscojavier@gmail.com")

    st.divider()

    # --- PANEL ADMIN (NUEVO) ---
    with st.expander("⚙️ Acceso Admin (Privado)"):
        password = st.text_input("Clave de Acceso", type="password")
        if password == "kaizen":
            st.success("🔓 Modo Editor Activado")
            with st.form("subir_curso_form"):
                st.markdown("### Nuevo Curso")
                f_titulo = st.text_input("Nombre del Curso")
                f_inst = st.text_input("Institución")
                f_cat = st.selectbox("Área", ["Salud", "Tecnología", "Soft Skills", "Calidad"])
                f_fecha = st.date_input("Fecha Emisión")
                f_archivo = st.file_uploader("Evidencia (Imagen/PDF)", type=["png", "jpg", "jpeg", "pdf"])
                if st.form_submit_button("⬆️ Subir a la Nube"):
                    if f_titulo and f_inst:
                        with st.spinner("Subiendo..."):
                            if backend.subir_curso(f_titulo, f_inst, f_fecha, f_cat, f_archivo):
                                st.success("✅ Guardado"); st.balloons()
                            else: st.error("❌ Error")
                    else: st.warning("Datos faltantes")

# --- 4. HEADER Y CUERPO PRINCIPAL ---
st.markdown("""
    <div class="sticky-header">
        <div class="header-title">🧬 Arquitectura de Sistemas de Calidad & Lab. Clínico</div>
        <div class="header-subtitle">Portafolio Técnico de Ingeniería de Procesos y Automatización</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background-color: #F4F7F9; padding: 20px; border-radius: 10px; border-left: 5px solid #0A2463; font-style: italic; font-size: 16px; color: #333; margin-top: 10px;">
"Gestión de Calidad 4.0: Elevando el estándar del Laboratorio Clínico mediante la <b>Automatización de Procesos, Seguridad del Paciente y Toma de Decisiones Basada en Datos</b>."
</div>
<br>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "👑 La Joya", "🚀 Casos de Éxito", "⚙️ Ing. Clínica", "📜 Formación Viva", "🧠 Liderazgo"
])

# --- TAB 1: SGC (RESTAURADO COMPLETO) ---
with tab1:
    st.subheader("🏛️ Ecosistema SGC: Evolución y Futuro")
    st.markdown("Trayectoria completa de transformación digital: Del control documental estricto a la Inteligencia Artificial.")
    
    with st.expander("🏗️ Fase 1: Arquitectura de la Verdad Única (Implementado)", expanded=True):
        c1, c2 = st.columns([1, 2])
        with c1:
            st.metric("Volumen Controlado", "119 Docs", "Activos Vivos")
            st.code("Google Drive API\nAirtable Relational DB\nApps Script Automation")
        with c2:
            st.markdown("""
            **Ingeniería Documental Avanzada:**
            * **Separación de Entornos (Dev vs Prod):** Gestión dual de archivos.
            * **Trazabilidad Criptográfica:** Implementación de tokens de aprobación (ej. `20251210e`).
            * **Base de Datos Relacional:** Control automático de vigencia y obsolescencia.
            """)

    with st.expander("🧠 Fase 2: SGC V4.0 - Arquitectura Híbrida & IA (Roadmap)", expanded=True):
        st.info("💡 **Proyecto Estratégico:** Diseño de arquitectura para eliminar dependencias locales y potenciar el análisis cognitivo.")
        c3, c4 = st.columns([1, 2])
        with c3:
            st.markdown("**Stack Avanzado (Next-Gen):**")
            st.code("Supabase (PostgreSQL)\nGemini 3 Pro (IA Agent)\nFirebase + Streamlit")
        with c4:
            st.markdown("""
            **Ingeniería de Software Aplicada:**
            * **Persistencia Cloud (Supabase):** PostgreSQL para colaboración real-time.
            * **Agente Cognitivo (Gemini):** Análisis de Causa Raíz (Ishikawa) automatizado.
            * **Arquitectura Híbrida:** Frontend veloz + Backend de procesamiento.
            """)

# --- TAB 2: CASOS (RESTAURADO COMPLETO) ---
with tab2:
    st.subheader("📌 Soluciones de Impacto Inmediato")
    st.markdown("Implementaciones que resolvieron dolores diarios de operación, finanzas y seguridad.")
    st.divider()

    with st.expander("💎 Caso Meta: Esta Plataforma (CV Interactivo)", expanded=True):
        col_meta1, col_meta2 = st.columns([1, 2])
        with col_meta1:
            st.metric("Time-to-Market", "< 8 Horas", "Prototipado Rápido")
            st.metric("Arquitectura", "Serverless", "Alta Disponibilidad") 
        with col_meta2:
            st.markdown("""
            **El Reto:** Un CV estático (PDF) dice *que* sabes programar, pero no *demuestra* cómo lo haces.
            **La Solución:** PWA (Progressive Web App) desplegada en producción.
            * **Metodología Ágil:** Enfoque MVP.
            * **Eficiencia de Costos:** Arquitectura Cloud optimizada (OPEX reducido).
            * **Stack:** Python + Streamlit.
            """)

    st.markdown("#### 🚑 Área: Operaciones & Logística")
    col_a, col_b = st.columns(2)
    with col_a:
        with st.expander("🔹 1. Logística Inversa (AppSheet)", expanded=True):
            st.metric("KPI: Reclamos", "< 3%", "Reducción Drástica")
            st.markdown("""
            **Solución:** App móvil de **Trazabilidad de Cadena de Custodia**.
            * Monitorización estricta (Enviado / En Proceso / Liberado).
            * **Protocolo Proactivo:** Notificación de retrasos antes de la llegada del paciente.
            """)
    with col_b:
        with st.expander("🔹 2. Gestión del Conocimiento (AppSheet)", expanded=True):
            st.metric("KPI: Abandono", "0 Eventos", "Autonomía Total")
            st.markdown("""
            **Solución:** Base de Conocimiento Centralizada.
            * Digitalización del *Know-How* (Precios, Muestras, Tiempos).
            * **Impacto:** Eliminación de la curva de aprendizaje para juniors.
            """)

    st.divider()
    st.markdown("#### 🛡️ Seguridad & Finanzas")
    col_c, col_d = st.columns(2)
    with col_c:
        with st.expander("🔹 3. Protocolo 'Muralla China' (DLP)", expanded=True):
            st.metric("Activos Blindados", "104 Docs", "Propiedad Intelectual")
            st.markdown("""
            **Estrategia 'Soberanía de Datos':**
            * **Seguridad (DLP):** Permisos de *Solo Lectura* masivos. Bloqueo de descargas e impresión.
            * **QA:** Pruebas de penetración internas.
            """)
    with col_d:
        with st.expander("🔹 4. Monitoreo Event-Driven (Make)", expanded=True):
            st.markdown("""
            **Automatización:** Webhooks que escuchan eventos de "Vencimiento" en Trello.
            * **Optimización:** Filtros JSON para eficiencia de costos.
            * **Resultado:** Vigilancia financiera 24/7.
            """)

# --- TAB 3: INFRAESTRUCTURA (RESTAURADO COMPLETO) ---
with tab3:
    st.subheader("⚙️ Ingeniería Clínica & Infraestructura TI")
    st.markdown("Capacidad técnica para el despliegue de **Servidores Propios (Self-Hosted)** y gestión de hardware.")
    
    c_hard1, c_hard2 = st.columns(2)
    with c_hard1:
        st.markdown("### 🐧 Administración de Servidores (Linux)")
        with st.container():
            st.markdown("**🛠️ Docker & Contenedores**")
            st.progress(85)
            st.caption("Despliegue de aplicaciones aisladas (n8n, Bases de Datos) garantizando portabilidad.")
        with st.container():
            st.markdown("**⚡ Gestión de Procesos (PM2)**")
            st.progress(90)
            st.caption("Administración de Daemons para servicios 24/7 (Keep-alive).")
        with st.container():
            st.markdown("**🔒 Redes & Túneles (Ngrok / Cloudflare)**")
            st.progress(88)
            st.caption("Exposición segura de localhost a internet (CGNAT Bypass).")

    with c_hard2:
        st.markdown("### 🐍 Desarrollo de Software")
        with st.container():
            st.markdown("**📦 Entornos Virtuales (venv)**")
            st.progress(95)
            st.caption("Aislamiento estricto de dependencias por proyecto.")
        with st.container():
            st.markdown("**📊 Data Science (Pandas)**")
            st.progress(90)
            st.caption("ETL y Dashboards interactivos para KPIs normativos.")
        with st.container():
            st.markdown("**💻 IDE & Versionado (Git)**")
            st.progress(85)
            st.caption("Flujo de trabajo CI/CD y control de versiones.")

# --- TAB 4: FORMACIÓN VIVA (HÍBRIDO: ESTÁTICO + SUPABASE) ---
with tab4:
    st.subheader("🎓 Formación & Certificaciones (Base de Datos Viva)")
    
    # 1. LA JOYA (ESTÁTICA)
    st.markdown("""
    <div class="cert-box" style="border-left-color: #0A2463; background-color: #E8F0FE;">
        <h3 style="margin:0; color:#0A2463;">🏆 Diplomado Técnico en Sistemas Informáticos</h3>
        <p style="margin:0; font-weight:bold;">Avalado por: Secretaría de Educación Pública (SEP) & DGTVE</p>
        <p style="margin:0;">📅 2020 | ⏱️ <strong>421 Horas Académicas</strong></p>
        <hr style="border-color:#0A2463;">
        <p style="font-size:0.9em;">
        Formación integral intensiva cubriendo los pilares de la informática moderna:
        <br>✅ <strong>Hardware:</strong> Mantenimiento correctivo y preventivo a nivel componente.
        <br>✅ <strong>Redes:</strong> Configuración de protocolos, cableado estructurado y Fibra Óptica.
        <br>✅ <strong>Seguridad Informática:</strong> Análisis de vulnerabilidades y gestión de riesgos digitales.
        </p>
    </div>
    <br>
    """, unsafe_allow_html=True)

    # 2. CERTIFICACIONES SOPORTE (ESTÁTICO)
    col_cert1, col_cert2 = st.columns(2)
    with col_cert1:
        st.markdown("#### 📡 Infraestructura & Redes")
        st.markdown("* **Técnico en Redes de Datos** (61 Hrs) - *Fundación Carlos Slim*\n    * *Competencia:* Arquitectura LAN/WAN, Modelo OSI, TCP/IP.\n* **Técnico Instalador de Red** (Avance Certificado)\n    * *Competencia:* Infraestructura física y cableado.")
    with col_cert2:
        st.markdown("#### 💻 Desarrollo & Web")
        st.markdown("* **Asistente Web** (59 Hrs) - *Fundación Carlos Slim*\n    * *Competencia:* Fundamentos Frontend, Servidores.\n* **Finder: Investigación Digital** (26 Hrs) - *Calif: 9.3*\n    * *Competencia:* OSINT básico.")

    st.divider()

    # 3. STACK HERRAMIENTAS
    st.subheader("🧩 Arsenal de Herramientas de Negocio")
    col_izq, col_der = st.columns(2)
    with col_izq:
        st.markdown("#### ☁️ Google Workspace & No-Code")
        st.markdown("**Google Drive (Seguridad DLP)**"); st.progress(100)
        st.markdown("**Google Sheets + Apps Script**"); st.progress(95)
        st.markdown("**AppSheet (Desarrollo Móvil)**"); st.progress(90)
    with col_der:
        st.markdown("#### 🗃️ Automatización & Datos")
        st.markdown("**Airtable (Bases Relacionales)**"); st.progress(90)
        st.markdown("**n8n / Make (Integraciones)**"); st.progress(92)
        st.markdown("**SQL & Supabase (Backend)**"); st.progress(80)

    st.divider()

    # 4. LISTADO DINÁMICO (SUPABASE)
    st.markdown("##### 📚 Historial de Capacitación (Live Data)")
    
    # LLAMADA AL BACKEND
    datos_cursos = backend.obtener_cursos()
    
    if datos_cursos:
        df = pd.DataFrame(datos_cursos)
        # Filtros
        categorias = ["Todas"] + sorted(df['categoria'].unique().tolist())
        filtro = st.selectbox("Filtrar por Área:", options=categorias)
        
        if filtro != "Todas":
            df = df[df['categoria'] == filtro]
        
        # Renderizado de Tarjetas
        for index, row in df.iterrows():
            with st.container():
                c1, c2 = st.columns([3, 1])
                with c1:
                    icono = "💊" if row['categoria'] == "Salud" else "💻" if row['categoria'] == "Tecnología" else "📘"
                    st.markdown(f"**{icono} {row['titulo']}**")
                    st.caption(f"🏫 {row['institucion']} | 📅 {row['fecha_emision']}")
                with c2:
                    if row['evidencia_url']:
                        st.link_button("📄 Ver Evidencia", row['evidencia_url'])
                    else:
                        st.caption("🚫 Sin Evidencia")
                st.divider()
    else:
        st.info("ℹ️ Cargando base de datos o sin registros. (Ejecuta el script de migración si es la primera vez).")

# --- TAB 5: SOFT SKILLS (RESTAURADO COMPLETO) ---
with tab5:
    st.subheader("🧠 Competencias Directivas & Factor Humano")
    
    col_soft1, col_soft2 = st.columns(2)
    with col_soft1:
        st.markdown("### 🤝 Liderazgo Transformacional")
        with st.expander("🔹 Gestión del Cambio Digital", expanded=True):
            st.markdown("""
            **Logro:** Migración exitosa de personal analógico a herramientas digitales (AppSheet).
            * **Metodología:** Acompañamiento "codo a codo" para vencer la resistencia tecnológica.
            """)
        with st.expander("🔹 Gestión de Crisis"):
            st.markdown("""
            **Enfoque:** Resolución asertiva bajo presión clínica.
            * **Caso:** Continuidad operativa durante fallos de proveedores críticos.
            """)

    with col_soft2:
        st.markdown("### ⚖️ Bioética & Cultura")
        with st.expander("🔹 Privacidad por Diseño (Privacy by Design)", expanded=True):
            st.markdown("""
            **Práctica:** Implementación técnica de candados éticos en el manejo de datos de pacientes (DLP).
            """)
        with st.expander("🔹 Cultura Justa (Just Culture)"):
            st.markdown("""
            **Impacto:** Transformación de auditorías punitivas a sistemas de mejora continua basados en datos (Scoring objetivo).
            """)