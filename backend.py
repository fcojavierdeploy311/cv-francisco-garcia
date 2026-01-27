import streamlit as st
from supabase import create_client, Client
import cloudinary
import cloudinary.uploader
from datetime import datetime

# --- 1. CONFIGURACIÓN DE CONEXIONES ---

@st.cache_resource
def init_supabase():
    """Inicializa la conexión a Supabase usando st.secrets."""
    try:
        url = st.secrets["supabase"]["url"]
        key = st.secrets["supabase"]["key"]
        return create_client(url, key)
    except Exception as e:
        st.error(f"❌ Error crítico conectando a Supabase: {e}")
        return None

def init_cloudinary():
    """Configura el servicio de Cloudinary."""
    try:
        cloudinary.config( 
            cloud_name = st.secrets["cloudinary"]["cloud_name"], 
            api_key = st.secrets["cloudinary"]["api_key"], 
            api_secret = st.secrets["cloudinary"]["api_secret"],
            secure = True
        )
    except Exception as e:
        st.error(f"❌ Error configurando Cloudinary: {e}")

# --- 2. FUNCIONES DE GESTIÓN (CRUD) ---

def obtener_cursos():
    """Descarga la lista de cursos desde Supabase ordenados por fecha."""
    supabase = init_supabase()
    if not supabase: return []
    
    try:
        # Selecciona todo (*) y ordena descendente por fecha
        response = supabase.table("portafolio_cursos")\
            .select("*")\
            .order("fecha_emision", desc=True)\
            .execute()
        return response.data
    except Exception as e:
        # Fail-safe: Si falla la BD, retorna lista vacía para no romper la UI
        st.warning(f"⚠️ Error de lectura en BD: {e}")
        return []

def subir_curso(titulo, institucion, fecha, categoria, archivo_evidencia):
    """Sube evidencia a Cloudinary y registra el curso en Supabase."""
    supabase = init_supabase()
    init_cloudinary()
    
    if not supabase: return False

    try:
        url_evidencia = None
        
        # 1. Subida de Archivo (Si existe)
        if archivo_evidencia:
            respuesta_cloud = cloudinary.uploader.upload(
                archivo_evidencia, 
                folder="cv_paco_evidencias",
                resource_type="auto"
            )
            url_evidencia = respuesta_cloud.get("secure_url")
        
        # 2. Registro en Base de Datos
        datos = {
            "titulo": titulo,
            "institucion": institucion,
            "fecha_emision": str(fecha),
            "categoria": categoria,
            "evidencia_url": url_evidencia
        }
        
        supabase.table("portafolio_cursos").insert(datos).execute()
        return True
        
    except Exception as e:
        st.error(f"❌ Error en transacción de guardado: {e}")
        return False
