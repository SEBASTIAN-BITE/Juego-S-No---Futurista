"""
JUEGO SÍ/NO ULTRA - ¡Descubre tu Destino!
Optimizado para Visual Studio Code
Autor: Tu nombre aquí
"""

import os
import time
import random
import sys

# Configuración para Windows (para que funcionen los colores en CMD)
if sys.platform.startswith('win'):
    os.system('color')

# Colores ANSI para terminal
class Color:
    MORADO = '\033[95m'
    AZUL = '\033[94m'
    CYAN = '\033[96m'
    VERDE = '\033[92m'
    AMARILLO = '\033[93m'
    ROJO = '\033[91m'
    FIN = '\033[0m'
    NEGRITA = '\033[1m'
    SUBRAYADO = '\033[4m'

def limpiar():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def efecto_escribir(texto, velocidad=0.03):
    """Efecto de escritura letra por letra"""
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(velocidad)
    print()

def explosion_titulo():
    """Animación explosiva del título"""
    limpiar()
    frames = [
        "        .",
        "       ...",
        "      .....",
        "     .......",
        "    ✨ ✨ ✨",
        "   ✨ 🎮 ✨",
        "  ✨ JUEGO ✨",
        " ✨ SÍ/NO ✨",
        "✨ ULTRA ✨"
    ]
    for frame in frames:
        print("\n" * 10 + frame.center(50))
        time.sleep(0.15)
        limpiar()

def mostrar_banner():
    """Banner principal del juego"""
    banner = f"""
{Color.CYAN}╔══════════════════════════════════════════════════╗
║  {Color.AMARILLO}🌟 {Color.NEGRITA}JUEGO SÍ/NO ULTRA{Color.FIN}{Color.AMARILLO} 🌟{Color.CYAN}                      ║
║  {Color.VERDE}¡Descubre tu VERDADERO destino!{Color.CYAN}              ║
╚══════════════════════════════════════════════════╝{Color.FIN}
"""
    print(banner)

def barra_cargando(texto="Cargando"):
    """Barra de carga animada"""
    print(f"\n{Color.AMARILLO}{texto}", end="")
    for i in range(20):
        print("█", end="", flush=True)
        time.sleep(0.05)
    print(f" ¡LISTO!{Color.FIN}\n")

def pregunta(texto, numero):
    """Hace una pregunta con estilo"""
    print(f"\n{Color.MORADO}{'─' * 50}{Color.FIN}")
    print(f"{Color.NEGRITA}{Color.CYAN}PREGUNTA #{numero}{Color.FIN}")
    print(f"{Color.MORADO}{'─' * 50}{Color.FIN}\n")
    
    efecto_escribir(f"{Color.AMARILLO}❓ {texto}{Color.FIN}", 0.02)
    
    while True:
        respuesta = input(f"\n{Color.VERDE}👉 Respuesta (sí/no): {Color.FIN}").strip().lower()
        if respuesta in ['si', 'sí', 's', 'yes', 'y']:
            print(f"{Color.VERDE}✓ ¡Entendido!{Color.FIN}")
            return True
        elif respuesta in ['no', 'n']:
            print(f"{Color.ROJO}✗ ¡Anotado!{Color.FIN}")
            return False
        else:
            print(f"{Color.ROJO}⚠️  Solo 'sí' o 'no' por favor{Color.FIN}")

def animacion_calculando():
    """Animación épica mientras calcula"""
    print(f"\n{Color.CYAN}╔══════════════════════════════════════════════════╗{Color.FIN}")
    print(f"{Color.CYAN}║{Color.AMARILLO}  🔮 ANALIZANDO TUS RESPUESTAS 🔮{Color.CYAN}                ║{Color.FIN}")
    print(f"{Color.CYAN}╚══════════════════════════════════════════════════╝{Color.FIN}\n")
    
    mensajes = [
        "🧠 Procesando datos cerebrales...",
        "🌌 Consultando el cosmos...",
        "🔥 Midiendo tu nivel de épico...",
        "✨ Conectando con tu destino...",
        "🎯 Calculando resultado final..."
    ]
    
    for msg in mensajes:
        print(f"{Color.MORADO}{msg}{Color.FIN}", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print(f" {Color.VERDE}✓{Color.FIN}")
        time.sleep(0.3)
    
    barra_cargando("🎆 REVELANDO TU DESTINO")

def resultado_epico(titulo, emoji, descripcion, poderes, frase_epica):
    """Muestra el resultado de forma ÉPICA"""
    limpiar()
    
    # Explosión de estrellas
    for _ in range(3):
        print("\n" * 10 + "✨ " * 25)
        time.sleep(0.1)
        limpiar()
    
    # Marco del resultado
    print(f"\n{Color.AMARILLO}{'★' * 50}{Color.FIN}")
    print(f"{Color.CYAN}{'═' * 50}{Color.FIN}")
    print(f"\n{Color.NEGRITA}{Color.VERDE}{emoji}  {titulo}  {emoji}{Color.FIN}".center(70))
    print(f"\n{Color.CYAN}{'═' * 50}{Color.FIN}")
    print(f"{Color.AMARILLO}{'★' * 50}{Color.FIN}\n")
    
    time.sleep(0.5)
    
    # Descripción
    print(f"{Color.MORADO}📜 TU ESENCIA:{Color.FIN}")
    efecto_escribir(f"{Color.FIN}{descripcion}{Color.FIN}\n", 0.02)
    
    time.sleep(0.3)
    
    # Poderes
    print(f"{Color.CYAN}⚡ TUS SUPERPODERES:{Color.FIN}")
    for i, poder in enumerate(poderes, 1):
        time.sleep(0.2)
        print(f"{Color.VERDE}   {i}. {poder}{Color.FIN}")
    
    time.sleep(0.5)
    
    # Frase épica
    print(f"\n{Color.AMARILLO}{'─' * 50}{Color.FIN}")
    print(f"{Color.NEGRITA}{Color.MORADO}💬 FRASE ÉPICA:{Color.FIN}")
    efecto_escribir(f'   "{Color.CYAN}{frase_epica}{Color.FIN}"', 0.03)
    print(f"{Color.AMARILLO}{'─' * 50}{Color.FIN}\n")
    
    # Estadísticas random (para diversión)
    print(f"{Color.AZUL}📊 ESTADÍSTICAS:{Color.FIN}")
    stats = {
        "Nivel de Poder": random.randint(85, 100),
        "Carisma": random.randint(75, 100),
        "Épico": random.randint(90, 100),
        "Rareza": random.choice(["⭐⭐⭐⭐⭐ LEGENDARIO", "⭐⭐⭐⭐ ÉPICO", "⭐⭐⭐⭐⭐ MÍTICO"])
    }
    for stat, valor in stats.items():
        if isinstance(valor, int):
            print(f"{Color.VERDE}   • {stat}: {valor}/100{Color.FIN}")
        else:
            print(f"{Color.AMARILLO}   • {stat}: {valor}{Color.FIN}")
    
    print(f"\n{Color.AMARILLO}{'★' * 50}{Color.FIN}\n")

# ÁRBOL DE DECISIONES MEJORADO
def iniciar_juego():
    """Primer nodo del árbol"""
    limpiar()
    mostrar_banner()
    
    r1 = pregunta("¿Prefieres el día soleado o la noche misteriosa?", 1)
    
    if r1:  # DÍA
        return rama_dia()
    else:  # NOCHE
        return rama_noche()

def rama_dia():
    """Rama del día"""
    r2 = pregunta("¿Te gusta estar rodeado de mucha gente?", 2)
    
    if r2:  # SOCIAL
        r3 = pregunta("¿Eres el alma de la fiesta?", 3)
        if r3:
            r4 = pregunta("¿Te gustan los retos físicos y deportes extremos?", 4)
            if r4:
                animacion_calculando()
                resultado_epico(
                    "¡ERES UN SUPERHÉROE DE ACCIÓN!",
                    "🦸‍♂️",
                    "Dinámico, carismático y lleno de energía. Salvas el día mientras\nhaces que todos se diviertan. Tu presencia ilumina cualquier lugar\ny tu valor no conoce límites.",
                    [
                        "Super Fuerza Social - Haces amigos instantáneamente",
                        "Energía Infinita - Nunca te cansas de la acción",
                        "Carisma Explosivo - Todos quieren estar contigo",
                        "Reflejos de Héroe - Siempre estás listo para la aventura"
                    ],
                    "¡Con grandes poderes viene una GRAN FIESTA!"
                )
            else:
                animacion_calculando()
                resultado_epico(
                    "¡ERES UN INFLUENCER CÓSMICO!",
                    "🌟",
                    "Tu creatividad y personalidad magnética atraen a todos. Inspiras\na las personas con tu autenticidad y sabes cómo hacer que cada\nmomento sea memorable.",
                    [
                        "Aura Magnética - La gente gravita hacia ti",
                        "Creatividad Infinita - Ideas brillantes sin parar",
                        "Empatía Suprema - Entiendes a todos profundamente",
                        "Inspiración Viral - Tus palabras cambian vidas"
                    ],
                    "Brilla tan intenso que el universo no pueda ignorarte"
                )
        else:
            r4 = pregunta("¿Prefieres ayudar a otros antes que a ti mismo?", 4)
            if r4:
                animacion_calculando()
                resultado_epico(
                    "¡ERES UN ÁNGEL GUARDIÁN!",
                    "👼",
                    "Tu bondad no conoce límites. Siempre estás ahí para quien te\nnecesita, con una sonrisa y palabras de aliento. Eres la luz\nen los días oscuros de los demás.",
                    [
                        "Empatía Divina - Sientes lo que otros sienten",
                        "Sanación Emocional - Tus palabras curan corazones",
                        "Paciencia Infinita - Nunca te rindes con nadie",
                        "Aura Protectora - Haces sentir seguro a todos"
                    ],
                    "No todos los ángeles tienen alas, algunos tienen corazones gigantes"
                )
            else:
                animacion_calculando()
                resultado_epico(
                    "¡ERES UN DIPLOMÁTICO MAESTRO!",
                    "🎭",
                    "Equilibrado y sabio, sabes navegar las complejidades sociales con\ngracia. Eres el puente entre personas, resolviendo conflictos y\nuniendo corazones.",
                    [
                        "Inteligencia Social Suprema - Lees cualquier situación",
                        "Palabra de Oro - Siempre sabes qué decir",
                        "Mediador Nato - Resuelves cualquier conflicto",
                        "Equilibrio Perfecto - Nunca pierdes la compostura"
                    ],
                    "En un mundo de caos, tú eres la armonía"
                )
    else:  # SOLITARIO
        r3 = pregunta("¿Disfrutas creando cosas con tus propias manos?", 3)
        if r3:
            r4 = pregunta("¿Te fascina la tecnología y la innovación?", 4)
            if r4:
                animacion_calculando()
                resultado_epico(
                    "¡ERES UN GENIO INVENTOR!",
                    "🔧",
                    "Tu mente brillante no para de crear maravillas. Ves posibilidades\ndonde otros ven problemas. El futuro se construye con mentes como\nla tuya.",
                    [
                        "Inteligencia Mecánica Superior - Entiendes cómo funciona todo",
                        "Visión Futurista - Ves el mañana hoy",
                        "Manos Mágicas - Creas lo imposible",
                        "Innovación Constante - Nunca dejas de mejorar"
                    ],
                    "El futuro no se predice, se INVENTA"
                )
            else:
                animacion_calculando()
                resultado_epico(
                    "¡ERES UN ARTISTA MÍSTICO!",
                    "🎨",
                    "Tu creatividad fluye como magia pura. Cada creación tuya es una\nventana a tu alma única. Transformas lo ordinario en extraordinario\ncon solo un toque.",
                    [
                        "Visión Artística Única - Ves belleza en todo",
                        "Manos de Creador - Das vida a tus ideas",
                        "Inspiración Infinita - Nunca te quedas sin ideas",
                        "Alma de Artista - Tu esencia es pura creatividad"
                    ],
                    "El arte no es lo que ves, sino lo que haces ver a otros"
                )
        else:
            r4 = pregunta("¿Te encanta aprender cosas nuevas constantemente?", 4)
            if r4:
                animacion_calculando()
                resultado_epico(
                    "¡ERES UN SABIO EXPLORADOR!",
                    "📚",
                    "Tu sed de conocimiento es insaciable. Viajas por mundos de ideas\ny descubres tesoros de sabiduría. Cada libro es una aventura y\ncada concepto, un nuevo universo.",
                    [
                        "Mente Infinita - Absorbes conocimiento como esponja",
                        "Curiosidad Legendaria - Todo te fascina",
                        "Memoria Fotográfica - Nunca olvidas lo importante",
                        "Sabiduría Antigua - Conocimiento profundo de todo"
                    ],
                    "El conocimiento es el único tesoro que crece al compartirse"
                )
            else:
                animacion_calculando()
                resultado_epico(
                    "¡ERES UN FILÓSOFO ZEN!",
                    "🧘",
                    "Encuentras paz en la simplicidad. Tu tranquilidad es contagiosa\ny tu perspectiva de la vida, inspiradora. Eres la calma en medio\nde la tormenta del mundo.",
                    [
                        "Paz Interior Absoluta - Nada te perturba",
                        "Sabiduría Zen - Entiendes lo esencial",
                        "Aura Calmante - Tranquilizas a todos",
                        "Perspectiva Profunda - Ves más allá de lo obvio"
                    ],
                    "No busques la paz afuera, ERES la paz"
                )

def rama_noche():
    """Rama de la noche"""
    r2 = pregunta("¿Te atraen los misterios y lo desconocido?", 2)
    
    if r2:  # MISTERIOSO
        r3 = pregunta("¿Crees en la magia y lo sobrenatural?", 3)
        if r3:
            r4 = pregunta("¿Te gustaría tener poderes mágicos?", 4)
            if r4:
                animacion_calculando()
                resultado_epico(
                    "¡ERES UN HECHICERO SUPREMO!",
                    "🧙‍♂️",
                    "La magia fluye por tus venas. Dominas las fuerzas arcanas del\nuniverso y puedes doblar la realidad a tu voluntad. Tu poder es\ntan grande como tu sabiduría.",
                    [
                        "Magia Primordial - Controlas energías antiguas",
                        "Visión Mística - Ves más allá del velo",
                        "Hechizos Infinitos - Tu arsenal mágico no tiene límites",
                        "Conexión Cósmica - Uno con el universo"
                    ],
                    "La magia no está en el mundo, está en cómo lo ves"
                )
            else:
                animacion_calculando()
                resultado_epico(
                    "¡ERES UN DETECTIVE PARANORMAL!",
                    "🔍",
                    "Resuelves misterios que otros ni siquiera ven. Tu intuición es\nsobrenatural y tu lógica, impecable. Nada escapa a tu percepción\naguda.",
                    [
                        "Intuición Sobrenatural - Sabes cosas sin explicación",
                        "Ojo Detective - Ves cada detalle",
                        "Mente Analítica Superior - Resuelves lo imposible",
                        "Sexto Sentido - Percibes lo invisible"
                    ],
                    "La verdad siempre está ahí, solo necesitas saber dónde mirar"
                )
        else:
            r4 = pregunta("¿Te consideras rebelde e independiente?", 4)
            if r4:
                animacion_calculando()
                resultado_epico(
                    "¡ERES UN CAZADOR NOCTURNO!",
                    "🏹",
                    "La noche es tu reino. Ágil, astuto y libre, sigues tus propias\nreglas. Eres la sombra que protege a los inocentes y el miedo\nde los malvados.",
                    [
                        "Sigilo Absoluto - Te mueves sin ser visto",
                        "Puntería Perfecta - Nunca fallas tu objetivo",
                        "Instinto de Cazador - Siempre un paso adelante",
                        "Libertad Total - No sigues reglas de nadie"
                    ],
                    "En la oscuridad, los valientes brillan más fuerte"
                )
            else:
                animacion_calculando()
                resultado_epico(
                    "¡ERES UN ESTRATEGA SOMBRA!",
                    "♟️",
                    "Tu mente es un laberinto de estrategias. Siempre estás tres pasos\nadelante, moviendo piezas invisibles en el tablero de la vida.\nTu inteligencia es tu mayor arma.",
                    [
                        "Mente Maestra - Planeas 10 movimientos adelante",
                        "Paciencia Estratégica - El tiempo juega a tu favor",
                        "Visión Táctica - Ves todas las posibilidades",
                        "Control Absoluto - Manejas cada situación"
                    ],
                    "El ajedrez se juega en la mente antes que en el tablero"
                )
    else:  # INTROSPECTIVO
        r3 = pregunta("¿Prefieres expresarte con palabras o con acciones?", 3)
        if r3:
            r4 = pregunta("¿Te gustan las historias épicas y la fantasía?", 4)
            if r4:
                animacion_calculando()
                resultado_epico(
                    "¡ERES UN BARDO LEGENDARIO!",
                    "🎵",
                    "Tus palabras tejen realidades y tus historias inspiran leyendas.\nCada palabra tuya es música para el alma. Inmortalizas momentos\ny creas magia con tu voz.",
                    [
                        "Voz Encantadora - Tus palabras hipnotizan",
                        "Narrativa Épica - Cuentas historias increíbles",
                        "Inspiración Masiva - Tus palabras mueven multitudes",
                        "Creatividad Verbal Infinita - Nunca te quedas sin palabras"
                    ],
                    "Las palabras son el pincel con el que pinto realidades"
                )
            else:
                animacion_calculando()
                resultado_epico(
                    "¡ERES UN POETA DE MEDIANOCHE!",
                    "🌙",
                    "Capturas la esencia de las emociones humanas en versos perfectos.\nTu sensibilidad es tu superpoder. Ves belleza donde otros ven\noscuridad.",
                    [
                        "Alma Poética - Todo lo conviertes en arte",
                        "Empatía Profunda - Sientes el mundo intensamente",
                        "Belleza en la Oscuridad - Encuentras luz en todo",
                        "Palabras de Poder - Tus versos transforman"
                    ],
                    "La poesía es el idioma que el alma usa cuando las palabras no bastan"
                )
        else:
            r4 = pregunta("¿Eres observador y analizas todo a tu alrededor?", 4)
            if r4:
                animacion_calculando()
                resultado_epico(
                    "¡ERES UN GUARDIÁN SILENCIOSO!",
                    "🦉",
                    "Observas desde las sombras, viendo lo que otros no ven. Tu sabiduría\nsilenciosa protege a quienes amas. Eres el héroe anónimo que nadie\nconoce pero todos necesitan.",
                    [
                        "Observación Total - No se te escapa nada",
                        "Sabiduría Silenciosa - No necesitas hablar para ser sabio",
                        "Protector Invisible - Cuidas sin que lo sepan",
                        "Paciencia Eterna - Esperas el momento perfecto"
                    ],
                    "El verdadero poder no grita, susurra"
                )
            else:
                animacion_calculando()
                resultado_epico(
                    "¡ERES UN SOÑADOR CÓSMICO!",
                    "🌌",
                    "Vives entre las estrellas de tu imaginación. Tu mundo interior es\nmás vasto que el universo. Eres un creador de realidades oníricas\ny posibilidades infinitas.",
                    [
                        "Imaginación Ilimitada - Creas universos enteros",
                        "Visión de Ensueño - Ves lo que podría ser",
                        "Conexión Astral - Tu mente viaja por dimensiones",
                        "Creatividad Dimensional - No hay límites para ti"
                    ],
                    "Los sueños no son escape de la realidad, son la creación de nuevas"
                )

def main():
    """Función principal del juego"""
    try:
        explosion_titulo()
        
        while True:
            iniciar_juego()
            
            print(f"\n{Color.MORADO}{'═' * 50}{Color.FIN}")
            rejugar = input(f"{Color.AMARILLO}🔄 ¿Jugar de nuevo? (sí/no): {Color.FIN}").strip().lower()
            
            if rejugar not in ['si', 'sí', 's', 'yes', 'y']:
                limpiar()
                print(f"\n{Color.CYAN}{'★' * 50}{Color.FIN}")
                efecto_escribir(f"{Color.AMARILLO}\n✨ ¡Gracias por jugar! ✨{Color.FIN}\n", 0.05)
                efecto_escribir(f"{Color.VERDE}Tu destino ha sido revelado...{Color.FIN}\n", 0.05)
                efecto_escribir(f"{Color.MORADO}¡Hasta la próxima aventura, héroe!{Color.FIN}\n", 0.05)
                print(f"{Color.CYAN}{'★' * 50}{Color.FIN}\n")
                break
    
    except KeyboardInterrupt:
        print(f"\n\n{Color.ROJO}⚠️  Juego interrumpido. ¡Hasta pronto!{Color.FIN}\n")
    except Exception as e:
        print(f"\n{Color.ROJO}❌ Error inesperado: {e}{Color.FIN}\n")

if __name__ == "__main__":
    main()
