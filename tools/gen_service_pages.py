#!/usr/bin/env python3
"""Genera las 10 páginas de servicio con estructura SEO on-page.

Uso: python3 tools/gen_service_pages.py  (desde la raíz del proyecto)
Escribe <slug>.html en la raíz. El contenido editorial vive en PAGES.
"""
import json
import os
import urllib.parse

DOMAIN = "https://aquapeluqueriasantfeliu.com"
TEL_WA = "34692039950"

# (slug, nombre corto para menús)
MENU = [
    ("corte-peinado", "Corte y Peinado"),
    ("color-mechas", "Color y Mechas"),
    ("tratamientos-capilares", "Tratamientos Capilares"),
    ("depilacion-laser", "Depilación Láser"),
    ("higiene-facial", "Higiene Facial"),
    ("punta-de-diamante", "Punta de Diamante"),
    ("maderoterapia", "Maderoterapia"),
    ("masaje-linfatico-drenante", "Masaje Linfático Drenante"),
    ("presoterapia", "Presoterapia"),
    ("hifemsculpt", "HifemSculpt"),
]
NAME = dict(MENU)

# img: (ruta_base, srcset_extra, ancho_orig, alto_orig)
PAGES = {
 "depilacion-laser": dict(
  title="Depilación Láser en Sant Feliu | Aqua Perruquers",
  meta="Depilación láser en Sant Feliu de Llobregat. Piel suave y resultados duraderos en pocas sesiones. Primera consulta gratuita: reserva por WhatsApp.",
  h1="Depilación Láser en Sant Feliu de Llobregat",
  intro="¿Buscas depilación láser en Sant Feliu de Llobregat? En Aqua trabajamos con tecnología láser avanzada y segura. Olvídate de la cera y consigue una piel suave de forma duradera.",
  img=("depilacion-laser-sant-feliu", [("400",400),("800",800)], 1080, 1344),
  alt="Sesión de depilación láser en Aqua Perruquers, Sant Feliu",
  secciones=[
   ("Cómo funciona la depilación láser",
    "<p>El láser emite una luz que llega a la raíz del vello. El folículo se debilita en cada sesión. Con el tiempo, el vello deja de crecer.</p>"
    "<p>El tratamiento es prácticamente indoloro. Antes de empezar valoramos tu tipo de piel y de vello. Así ajustamos la potencia para un resultado seguro y eficaz.</p>"),
   ("Zonas que tratamos",
    "<p>Tratamos todas las zonas corporales y faciales: piernas, axilas, ingles, brazos, espalda, pecho y labio superior, entre otras.</p>"
    "<p>Cada zona tiene su tarifa y existen bonos con descuento al combinar varias. Pídenos el listado de precios por WhatsApp sin compromiso.</p>"),
   ("¿Cuántas sesiones necesitas?",
    "<p>Depende de la zona, del tipo de vello y de tu piel. La mayoría de clientas notan una reducción clara a partir de la tercera sesión.</p>"
    "<p>Lo habitual son entre 6 y 10 sesiones, espaciadas varias semanas. En tu primera visita te daremos una estimación personalizada gratuita.</p>"),
   ("Ventajas frente a la cera y la cuchilla",
    "<p>La cera y la cuchilla obligan a repetir cada pocas semanas. El láser actúa sobre la raíz y reduce el vello de forma progresiva y duradera.</p>"
    "<p>Además evita los problemas habituales de otros métodos: foliculitis, vello enquistado, irritación y manchas por roce. La piel queda uniforme y suave.</p>"
    "<p>A medio plazo también sale a cuenta: cada sesión te acerca a olvidarte de la depilación, en lugar de volver a empezar cada mes.</p>"),
   ("Antes y después de cada sesión: cuidados",
    "<ul><li>Evita el sol y los autobronceadores los días previos.</li>"
    "<li>Acude con la zona rasurada, no con cera ni pinzas.</li>"
    "<li>Después, hidrata la piel y usa protección solar.</li>"
    "<li>Evita saunas y ejercicio intenso durante 24 horas.</li></ul>"),
  ],
  faqs=[
   ("¿La depilación láser duele?",
    "No. La sensación es un leve calor puntual. Nuestro equipo incorpora refrigeración para que la sesión sea cómoda."),
   ("¿Es apta para todo tipo de piel?",
    "Valoramos cada caso en la consulta previa gratuita. La tecnología actual permite tratar la mayoría de fototipos con seguridad."),
   ("¿Puedo hacerme láser en verano?",
    "Sí, con precauciones. Hay que evitar la exposición solar directa en la zona tratada antes y después de cada sesión."),
   ("¿El resultado de la depilación láser es para siempre?",
    "La reducción del vello es duradera y muy notable. Algún vello fino puede reaparecer con el tiempo por cambios hormonales; se mantiene con sesiones puntuales de recuerdo."),
   ("¿Qué beneficios tiene frente a la fotodepilación IPL?",
    "El láser concentra la energía en una sola longitud de onda. Llega mejor a la raíz del vello, necesita menos sesiones y trata más tipos de piel con seguridad."),
  ],
  rel=["higiene-facial", "presoterapia", "maderoterapia"],
 ),
 "hifemsculpt": dict(
  title="HifemSculpt en Sant Feliu de Llobregat | Aqua Perruquers",
  meta="HifemSculpt en Sant Feliu: tonifica el abdomen, glúteos y piernas con ondas electromagnéticas. Equivale a miles de contracciones por sesión. Infórmate.",
  h1="HifemSculpt en Sant Feliu de Llobregat: tonifica y reduce grasa",
  intro="HifemSculpt es nuestro tratamiento corporal más avanzado. Usa ondas electromagnéticas de alta intensidad para tonificar el músculo y reducir grasa localizada. Sin cirugía y sin esfuerzo.",
  img=("hifem-sculpt-abdomen", [("400",400),("800",800)], 980, 653),
  alt="Tratamiento HifemSculpt en abdomen en Aqua Perruquers, Sant Feliu",
  secciones=[
   ("Qué es HifemSculpt y cómo funciona",
    "<p>El equipo emite ondas electromagnéticas focalizadas de alta intensidad. Provocan contracciones musculares profundas, imposibles de lograr entrenando.</p>"
    "<p>Una sesión de 30 minutos equivale a unas 30.000 contracciones. El músculo se fortalece y el cuerpo consume la grasa de la zona.</p>"
    "<p>Durante la sesión solo tienes que tumbarte. Colocamos el aplicador sobre la zona y regulamos la intensidad contigo, de menos a más. Al terminar puedes seguir con tu día con normalidad.</p>"),
   ("Zonas tratables: abdomen, glúteos y piernas",
    "<p>Las zonas más demandadas son el abdomen y los glúteos. También tratamos muslos y otras zonas con grasa localizada.</p>"
    "<p>En la primera consulta definimos contigo el objetivo: definir, tonificar o reducir volumen.</p>"),
   ("Resultados: qué esperar y en cuánto tiempo",
    "<p>Muchas personas notan firmeza desde las primeras sesiones. El ritmo de los resultados varía según cada cuerpo, la zona tratada y los hábitos de cada persona.</p>"
    "<p>En la primera consulta te orientamos de forma realista sobre qué esperar en tu caso concreto y diseñamos el ciclo de sesiones adecuado.</p>"
    "<p>No requiere tiempo de recuperación. Puedes hacer vida normal inmediatamente después.</p>"),
   ("¿Para quién está indicado (y para quién no)?",
    "<p>Está indicado para quien quiere tonificar y perder grasa localizada sin pasar por quirófano. Es un excelente complemento al ejercicio.</p>"
    "<p>No se recomienda en embarazo ni con dispositivos metálicos o electrónicos implantados. Ante cualquier duda médica, consúltanos antes de reservar.</p>"),
   ("Precio y bonos de sesiones",
    "<p>Trabajamos con sesiones sueltas y bonos de varias sesiones con descuento. Escríbenos por WhatsApp y te pasamos las tarifas vigentes y la primera consulta gratuita.</p>"),
  ],
  faqs=[
   ("¿HifemSculpt sustituye al gimnasio?",
    "No lo sustituye, lo complementa. Logra contracciones más intensas que el ejercicio voluntario, pero unos hábitos activos mejoran y mantienen el resultado."),
   ("¿Cuánto dura una sesión?",
    "Unos 30 minutos por zona. Llegas, te tumbas y el equipo trabaja. Sin dolor y sin recuperación posterior."),
   ("¿Qué se siente durante la sesión?",
    "Notarás contracciones musculares intensas pero indoloras, como un entrenamiento muy concentrado. No deja agujetas incapacitantes ni marcas."),
   ("¿Qué beneficios aporta frente a otros tratamientos corporales?",
    "Es el único que trabaja músculo y grasa a la vez. Tonifica en profundidad mientras reduce volumen, sin agujas, sin cirugía y sin parar tu rutina."),
  ],
  rel=["maderoterapia", "presoterapia", "masaje-linfatico-drenante"],
 ),
 "higiene-facial": dict(
  title="Higiene Facial en Sant Feliu de Llobregat | Aqua Perruquers",
  meta="Higiene facial profunda en Sant Feliu de Llobregat: limpieza, extracción, hidratación y mascarilla adaptada a tu piel. Reserva por WhatsApp.",
  h1="Higiene Facial Profunda en Sant Feliu de Llobregat",
  intro="Una higiene facial profesional devuelve a tu piel la limpieza y la luminosidad que el día a día le quita. En Aqua adaptamos cada paso a tu tipo de piel.",
  img=("higiene-facial-sant-feliu", [("400",400),("800",800)], 1079, 1313),
  alt="Higiene facial profunda en Aqua Perruquers, Sant Feliu",
  secciones=[
   ("En qué consiste nuestra higiene facial (paso a paso)",
    "<ol><li>Diagnóstico de la piel y desmaquillado.</li>"
    "<li>Limpieza profunda y exfoliación.</li>"
    "<li>Extracción de puntos negros e impurezas.</li>"
    "<li>Mascarilla específica para tu piel.</li>"
    "<li>Hidratación final y protección.</li></ol>"
    "<p>La sesión completa dura entre 60 y 75 minutos. Cada paso usa productos profesionales elegidos según tu diagnóstico: no aplicamos el mismo protocolo a todo el mundo.</p>"
    "<p>La extracción se realiza tras ablandar el poro con vapor ozono, de forma controlada y sin agredir la piel.</p>"),
   ("Beneficios para cada tipo de piel",
    "<p>En pieles grasas reduce brillos y poros obstruidos. En pieles secas aporta hidratación profunda. En pieles apagadas devuelve la luminosidad.</p>"
    "<p>También prepara la piel para otros tratamientos, que penetran mejor tras una buena limpieza.</p>"),
   ("Cada cuánto conviene hacerse una limpieza facial",
    "<p>Como norma general, cada 4 a 8 semanas. Depende de tu tipo de piel, tu rutina y la época del año.</p>"
    "<p>Te recomendaremos la frecuencia ideal en tu primera visita.</p>"),
   ("Qué notarás después de la sesión",
    "<p>La piel queda limpia, jugosa y descongestionada desde el primer día. El tono se ve más uniforme y el maquillaje, cuando vuelvas a usarlo, asienta mucho mejor.</p>"
    "<p>Con sesiones regulares se reducen los puntos negros recurrentes y los brotes leves, y la piel mantiene un aspecto cuidado de forma estable.</p>"),
   ("Combínala con punta de diamante",
    "<p>La microdermoabrasión con <a href=\"/punta-de-diamante\">punta de diamante</a> multiplica el efecto renovador. Elimina células muertas y atenúa marcas y manchas. Pregúntanos por el tratamiento combinado.</p>"),
  ],
  faqs=[
   ("¿Cuánto dura una higiene facial?",
    "Entre 60 y 75 minutos, según las necesidades de tu piel."),
   ("¿Es adecuada para pieles sensibles?",
    "Sí. Ajustamos los productos y la intensidad de cada paso. Avísanos si tienes alguna alergia o tratamiento dermatológico activo."),
   ("¿Qué beneficios notaré desde la primera sesión?",
    "Piel más limpia, suave y luminosa al instante, y poros visiblemente descongestionados. Con constancia, el efecto se mantiene y mejora."),
   ("¿Elimina los puntos negros?",
    "Sí, la extracción profesional retira los puntos negros existentes. Las sesiones periódicas evitan que vuelvan a acumularse."),
   ("¿Puedo maquillarme después?",
    "Mejor espera unas horas. La piel queda limpia y receptiva; déjala respirar el resto del día."),
  ],
  rel=["punta-de-diamante", "depilacion-laser"],
 ),
 "color-mechas": dict(
  title="Color, Mechas y Balayage en Sant Feliu | Aqua Perruquers",
  meta="Color, mechas, balayage y babylights en Sant Feliu de Llobregat. Coloración personalizada que cuida tu cabello. Pide cita por WhatsApp con Aqua.",
  h1="Color y Mechas en Sant Feliu de Llobregat",
  intro="¿Quieres un cambio de color que parezca tuyo de toda la vida? En Aqua estudiamos tu tono de piel y tu estilo. Después elegimos juntas la técnica perfecta.",
  img=("color-mechas-cabello", [("400",400)], 800, 534),
  alt="Coloración y mechas balayage en Aqua Perruquers, Sant Feliu",
  secciones=[
   ("Técnicas: mechas, balayage, babylights y más",
    "<p>Trabajamos mechas clásicas, balayage, babylights y coloraciones completas. Cada técnica aporta un efecto distinto.</p>"
    "<ul><li><strong>Mechas clásicas:</strong> contraste definido y luminosidad uniforme.</li>"
    "<li><strong>Balayage:</strong> degradado natural pintado a mano, de mantenimiento cómodo.</li>"
    "<li><strong>Babylights:</strong> reflejos muy finos, efecto sol de aspecto juvenil.</li>"
    "<li><strong>Color completo:</strong> cobertura total, ideal para canas o cambios de tono.</li></ul>"
    "<p>Te asesoramos sin compromiso sobre cuál encaja mejor con tu cabello y tu mantenimiento.</p>"),
   ("Coloración que respeta tu cabello",
    "<p>Usamos productos profesionales con tratamientos protectores. El objetivo es un color bonito y un cabello sano.</p>"
    "<p>Si tu melena está sensibilizada, combinamos el color con un <a href=\"/tratamientos-capilares\">tratamiento capilar</a> reparador.</p>"),
   ("Nuestros trabajos",
    "<p>En la <a href=\"/#galeria\">galería de la web</a> y en nuestro <a href=\"https://www.instagram.com/aqua_perruquers/\" target=\"_blank\" rel=\"noopener noreferrer\">Instagram</a> puedes ver coloraciones reales hechas en el salón.</p>"),
   ("Cómo mantener el color en casa",
    "<ul><li>Champú específico para cabello teñido.</li>"
    "<li>Agua templada, no muy caliente.</li>"
    "<li>Protector térmico antes de plancha o secador.</li>"
    "<li>Mascarilla nutritiva una vez por semana.</li></ul>"),
   ("Precios orientativos",
    "<p>El precio varía según el largo, la técnica y el estado del cabello. Escríbenos por WhatsApp con una foto y te damos un presupuesto orientativo al momento.</p>"),
  ],
  faqs=[
   ("¿Cuál es la diferencia entre balayage y mechas?",
    "Las mechas se trabajan con un patrón definido. El balayage se pinta a mano alzada para un degradado más natural y un mantenimiento más cómodo."),
   ("¿El color daña el cabello?",
    "Con productos profesionales y protección adecuada, el daño es mínimo. Valoramos siempre el estado de tu cabello antes de proponerte una técnica."),
   ("¿Cada cuánto se retoca un balayage?",
    "Es su gran ventaja: al no tener raíz marcada, aguanta de 3 a 6 meses con buen aspecto. Las mechas clásicas suelen retocarse antes."),
   ("¿Podéis corregir un color que no me gusta?",
    "Sí. Analizamos el color actual y el estado del cabello, y planificamos la corrección en una o varias fases para lograrlo sin estropearlo."),
  ],
  rel=["corte-peinado", "tratamientos-capilares"],
 ),
 "corte-peinado": dict(
  title="Corte y Peinado en Sant Feliu | Aqua Perruquers",
  meta="Corte y peinado para mujer y hombre en Sant Feliu de Llobregat. Asesoramiento de imagen y acabados para el día a día o eventos. Pide cita.",
  h1="Corte y Peinado en Sant Feliu de Llobregat",
  intro="Un buen corte te simplifica la vida cada mañana. En Aqua escuchamos lo que buscas y lo adaptamos a tu rostro, tu cabello y tu rutina.",
  img=("corte-peinado-peluqueria", [("400",400)], 800, 534),
  alt="Corte y peinado profesional en Aqua Perruquers, Sant Feliu",
  secciones=[
   ("Corte personalizado: estudiamos tu rostro y estilo",
    "<p>Antes de coger las tijeras, te asesoramos. Valoramos la forma de tu rostro, la textura de tu cabello y el tiempo que dedicas a peinarte.</p>"
    "<p>El resultado: un corte que funciona en el salón y también en casa.</p>"
    "<p>Trabajamos todo tipo de cabello: liso, ondulado, rizado, fino o con mucha densidad. Cada textura pide una técnica distinta, y elegirla bien marca la diferencia entre un corte que crece bonito y uno que pierde la forma en dos semanas.</p>"),
   ("Peinados para eventos y ocasiones especiales",
    "<p>Bodas, celebraciones y eventos. Recogidos, semirrecogidos y ondas con acabado duradero.</p>"
    "<p>Si lo necesitas, hacemos una prueba previa para llegar al día señalado sin sorpresas.</p>"
    "<p>El acabado se adapta al momento: ondas suaves para un look natural, pulido espejo para un evento formal o textura despeinada con efecto duradero.</p>"),
   ("Nuestros trabajos",
    "<p>Mira ejemplos reales en la <a href=\"/#galeria\">galería</a> y en nuestro <a href=\"https://www.instagram.com/aqua_perruquers/\" target=\"_blank\" rel=\"noopener noreferrer\">Instagram</a>.</p>"),
   ("Precios",
    "<p>Las tarifas dependen del servicio: corte, corte y peinado, o peinado de evento. Pídenos precios por WhatsApp y reserva tu hora en un minuto.</p>"),
  ],
  faqs=[
   ("¿Cómo sé qué corte me favorece?",
    "Lo estudiamos contigo antes de empezar. Valoramos la forma de tu rostro, la textura del cabello y tu estilo de vida, y te proponemos opciones realistas."),
   ("¿Cuánto dura un peinado de evento?",
    "Trabajamos con técnicas y productos de fijación profesional para que el peinado aguante toda la celebración en perfecto estado."),
   ("¿Qué beneficio tiene el asesoramiento de imagen?",
    "Evitas cortes que no van contigo. Sales con un estilo que podrás reproducir en casa con facilidad y que realza tus facciones."),
  ],
  rel=["color-mechas", "tratamientos-capilares"],
 ),
 "tratamientos-capilares": dict(
  title="Tratamientos Capilares en Sant Feliu | Aqua Perruquers",
  meta="Tratamientos capilares en Sant Feliu de Llobregat: hidratación profunda, reparación y anticaída. Recupera la salud de tu cabello. Reserva tu diagnóstico.",
  h1="Tratamientos Capilares en Sant Feliu de Llobregat",
  intro="¿Cabello seco, castigado o sin fuerza? Nuestros tratamientos capilares devuelven la salud a tu melena desde la raíz hasta las puntas.",
  img=("tratamiento-capilar-hidratacion", [("400",400)], 800, 1200),
  alt="Tratamiento capilar de hidratación profunda en Aqua Perruquers, Sant Feliu",
  secciones=[
   ("Diagnóstico capilar: el primer paso",
    "<p>Cada cabello es distinto. Analizamos el estado de tu cuero cabelludo y de tu fibra capilar antes de recomendarte nada.</p>"
    "<p>Con el diagnóstico claro, elegimos el tratamiento y la pauta adecuados.</p>"
    "<p>Este paso evita gastar en productos que no necesitas. Un cabello deshidratado y uno dañado por química se ven parecidos, pero se tratan de forma distinta.</p>"),
   ("Hidratación y nutrición profunda",
    "<p>Para cabellos secos o apagados. Aportamos agua y nutrientes a la fibra capilar. El resultado es un cabello suave, elástico y con brillo.</p>"),
   ("Tratamientos reparadores y anticaída",
    "<p>La keratina y los reconstructores reparan el cabello dañado por decoloraciones o calor. Para la caída estacional trabajamos con tratamientos que fortalecen y estimulan el cuero cabelludo.</p>"),
   ("Resultados y mantenimiento en casa",
    "<p>Notarás el cambio desde la primera sesión. Para mantenerlo, te recomendamos la rutina de casa: champú, mascarilla y protector adecuados a tu caso.</p>"),
  ],
  faqs=[
   ("¿Cada cuánto se repite un tratamiento capilar?",
    "Depende del tratamiento y del estado del cabello. Lo habitual es una pauta inicial de choque y luego mantenimiento mensual."),
   ("¿Sirven si me tiño el pelo?",
    "Sí, y son muy recomendables. Reparan la fibra y ayudan a que el color dure más bonito."),
   ("¿Qué beneficios notaré tras la primera sesión?",
    "Cabello más suave, manejable y con brillo desde el primer lavado. Los tratamientos de fondo, como el anticaída, muestran su efecto con la constancia."),
   ("¿Cómo sé qué tratamiento necesita mi cabello?",
    "Con el diagnóstico capilar que hacemos en el salón. Distingue entre falta de hidratación, falta de nutrición o daño estructural, que se tratan de forma diferente."),
  ],
  rel=["color-mechas", "corte-peinado"],
 ),
 "maderoterapia": dict(
  title="Maderoterapia en Sant Feliu de Llobregat | Aqua Perruquers",
  meta="Maderoterapia en Sant Feliu de Llobregat: masaje con utensilios de madera para reducir celulitis, moldear y activar la circulación. Pide tu sesión.",
  h1="Maderoterapia en Sant Feliu de Llobregat",
  intro="La maderoterapia es un masaje intensivo con utensilios de madera. Moldea la figura, combate la celulitis y activa la circulación de forma natural.",
  img=("maderoterapia-sant-feliu", [("400",400),("800",800)], 951, 632),
  alt="Sesión de maderoterapia corporal en Aqua Perruquers, Sant Feliu",
  secciones=[
   ("Qué es la maderoterapia y qué beneficios tiene",
    "<p>Se trabaja el cuerpo con rodillos, copas y tablas de madera. La presión estimula el tejido y el sistema linfático.</p>"
    "<ul><li>Reduce la apariencia de la celulitis.</li><li>Ayuda a moldear cintura, piernas y glúteos.</li><li>Activa la circulación y el drenaje.</li><li>Relaja la musculatura.</li></ul>"),
   ("Cómo es una sesión en Aqua",
    "<p>La sesión dura unos 45-60 minutos. Adaptamos la intensidad a tu sensibilidad y a la zona tratada.</p>"
    "<p>Es un masaje vigoroso pero agradable. Saldrás con sensación de ligereza.</p>"
    "<p>Empezamos siempre con movimientos de calentamiento y drenaje. Después trabajamos cada zona con el utensilio adecuado: rodillo para activar, copa sueca para moldear y tabla para alisar el tejido.</p>"),
   ("¿Cuántas sesiones se recomiendan?",
    "<p>Para notar cambios visibles se recomienda un ciclo de 8 a 10 sesiones, una o dos por semana. Después, mantenimiento mensual.</p>"),
   ("Combínala con presoterapia o masaje drenante",
    "<p>La <a href=\"/presoterapia\">presoterapia</a> y el <a href=\"/masaje-linfatico-drenante\">masaje linfático drenante</a> potencian el drenaje y aceleran los resultados. Pregúntanos por los bonos combinados.</p>"),
  ],
  faqs=[
   ("¿La maderoterapia duele?",
    "Es un masaje intenso, pero regulamos la presión contigo. No debe resultar doloroso."),
   ("¿Cuándo se notan los resultados?",
    "La piel mejora desde las primeras sesiones. El efecto moldeador se aprecia al completar el ciclo recomendado."),
   ("¿Qué beneficios tiene frente a un masaje anticelulítico manual?",
    "Los utensilios de madera permiten trabajar el tejido con más profundidad y precisión que las manos, intensificando el efecto drenante y moldeador."),
   ("¿En qué zonas se puede aplicar?",
    "Principalmente piernas, glúteos, abdomen y brazos. Adaptamos los utensilios y la presión a cada zona del cuerpo."),
  ],
  rel=["presoterapia", "masaje-linfatico-drenante", "hifemsculpt"],
 ),
 "presoterapia": dict(
  title="Presoterapia en Sant Feliu de Llobregat | Aqua Perruquers",
  meta="Presoterapia en Sant Feliu de Llobregat: mejora la circulación, reduce la retención de líquidos y alivia piernas cansadas. Reserva tu sesión en Aqua.",
  h1="Presoterapia en Sant Feliu de Llobregat",
  intro="La presoterapia aplica presión de aire controlada sobre piernas y abdomen. Activa la circulación, drena líquidos y deja una sensación inmediata de ligereza.",
  img=("presoterapia-sant-feliu", [("400",400)], 759, 609),
  alt="Tratamiento de presoterapia en Aqua Perruquers, Sant Feliu",
  secciones=[
   ("Cómo funciona la presoterapia",
    "<p>Te colocamos unas botas y una faja neumáticas. El equipo infla y desinfla las cámaras de aire en oleadas, de los pies hacia arriba.</p>"
    "<p>Este movimiento empuja el líquido retenido hacia el sistema linfático, que lo elimina de forma natural.</p>"
    "<p>Es un tratamiento totalmente pasivo y muy relajante. Muchas clientas lo describen como un masaje de piernas continuo que deja una ligereza inmediata al levantarse de la camilla.</p>"),
   ("Beneficios: piernas cansadas, retención y recuperación",
    "<ul><li>Alivia las piernas cansadas e hinchadas.</li>"
    "<li>Reduce la retención de líquidos.</li>"
    "<li>Mejora la circulación de retorno.</li>"
    "<li>Complementa los tratamientos anticelulíticos.</li></ul>"),
   ("Duración y frecuencia recomendada",
    "<p>Cada sesión dura entre 30 y 45 minutos. Para retención de líquidos se recomiendan una o dos sesiones semanales durante el primer mes.</p>"),
   ("Bonos de sesiones",
    "<p>Tenemos bonos de presoterapia y combinados con <a href=\"/maderoterapia\">maderoterapia</a> o <a href=\"/masaje-linfatico-drenante\">drenaje linfático</a>. Pídenos precios por WhatsApp.</p>"),
  ],
  faqs=[
   ("¿Qué se siente durante la sesión?",
    "Una presión agradable que sube por las piernas, como un masaje continuo. Muchas clientas se relajan hasta dormirse."),
   ("¿Hay contraindicaciones?",
    "No se recomienda en embarazo, trombosis o insuficiencias graves. Si tienes dudas médicas, consúltanos antes de reservar."),
   ("¿Qué beneficios notaré tras la primera sesión?",
    "Piernas visiblemente menos hinchadas y una sensación inmediata de ligereza. Con sesiones regulares mejora también la circulación de retorno."),
   ("¿Se puede combinar con otros tratamientos corporales?",
    "Sí, y es lo más eficaz. Combinada con maderoterapia o drenaje linfático, potencia la eliminación de líquidos y el efecto anticelulítico."),
  ],
  rel=["maderoterapia", "masaje-linfatico-drenante", "hifemsculpt"],
 ),
 "masaje-linfatico-drenante": dict(
  title="Masaje Linfático Drenante en Sant Feliu | Aqua Perruquers",
  meta="Masaje linfático drenante en Sant Feliu de Llobregat. Reduce la retención de líquidos, activa la circulación y deshincha de forma natural. Pide cita.",
  h1="Masaje Linfático Drenante en Sant Feliu de Llobregat",
  intro="El drenaje linfático manual es un masaje suave y rítmico. Ayuda a tu cuerpo a eliminar líquidos y toxinas, y deshincha de forma natural.",
  img=("masaje-linfatico-drenante", [("400",400),("800",800)], 1080, 1050),
  alt="Masaje linfático drenante manual en Aqua Perruquers, Sant Feliu",
  secciones=[
   ("Qué es el drenaje linfático manual",
    "<p>Es una técnica de masaje con movimientos suaves y precisos. Sigue el recorrido del sistema linfático para estimular la eliminación de líquidos.</p>"
    "<p>A diferencia de otros masajes, no busca presionar el músculo sino movilizar la linfa.</p>"
    "<p>El sistema linfático no tiene bomba propia, como sí la tiene la sangre con el corazón. Por eso, cuando se satura, aparecen hinchazón y pesadez. El drenaje manual lo ayuda a circular de nuevo.</p>"),
   ("Beneficios y para quién está indicado",
    "<ul><li>Reduce la hinchazón y la retención de líquidos.</li>"
    "<li>Activa la circulación y mejora la piel de naranja.</li>"
    "<li>Aporta una profunda sensación de descanso.</li></ul>"
    "<p>Está indicado para piernas hinchadas, retención por calor o sedentarismo y como complemento de otros tratamientos corporales.</p>"),
   ("¿Cuántas sesiones necesito?",
    "<p>Para un efecto puntual, una sesión ya deshincha. Para resultados mantenidos se recomienda un ciclo semanal el primer mes y luego mantenimiento.</p>"),
  ],
  faqs=[
   ("¿El drenaje linfático duele?",
    "No. Es un masaje muy suave. La presión es ligera y el ritmo, lento y constante."),
   ("¿Cada cuánto puedo repetirlo?",
    "Puede realizarse semanalmente sin problema. Te recomendaremos la pauta según tu objetivo."),
   ("¿Hacéis drenaje post-operatorio?",
    "Consúltanos tu caso concreto por WhatsApp. Valoramos cada situación de forma individual y siempre con indicación de tu médico."),
   ("¿Qué beneficios notaré tras la primera sesión?",
    "Menos hinchazón, piernas y abdomen más ligeros y una relajación profunda. Es habitual notar también un descanso nocturno mejor."),
  ],
  rel=["presoterapia", "maderoterapia"],
 ),
 "punta-de-diamante": dict(
  title="Punta de Diamante en Sant Feliu | Aqua Perruquers",
  meta="Microdermoabrasión con punta de diamante en Sant Feliu de Llobregat: renueva la piel, atenúa manchas y marcas, y aporta luminosidad. Reserva tu sesión.",
  h1="Microdermoabrasión con Punta de Diamante en Sant Feliu",
  intro="La punta de diamante exfolia la piel de forma mecánica y controlada. Elimina células muertas, afina la textura y devuelve la luminosidad al rostro.",
  img=("microdermoabrasion-punta-diamante", [("400",400),("800",800)], 1080, 1141),
  alt="Microdermoabrasión con punta de diamante en Aqua Perruquers, Sant Feliu",
  secciones=[
   ("Qué es la microdermoabrasión con punta de diamante",
    "<p>Es una exfoliación profunda realizada con un cabezal de diamante. Pule la capa superficial de la piel mientras aspira las células muertas.</p>"
    "<p>Es un tratamiento progresivo, indoloro y apto para la mayoría de pieles.</p>"),
   ("Beneficios: manchas, marcas y luminosidad",
    "<ul><li>Atenúa manchas superficiales y marcas leves.</li>"
    "<li>Afina la textura y reduce poros.</li>"
    "<li>Suaviza líneas finas.</li>"
    "<li>Aporta luminosidad inmediata.</li></ul>"),
   ("Cómo es la sesión y cuidados posteriores",
    "<p>La sesión dura unos 45 minutos. Después, la piel puede quedar levemente rosada unas horas.</p>"
    "<p>Es imprescindible usar protección solar los días posteriores e hidratar bien la piel.</p>"
    "<p>Trabajamos con cabezales de distinto grano según la zona y la sensibilidad. La exfoliación es gradual: controlamos la profundidad en todo momento para renovar sin irritar.</p>"),
   ("Combínala con higiene facial",
    "<p>El combo perfecto: una <a href=\"/higiene-facial\">higiene facial profunda</a> seguida de punta de diamante. Limpieza, renovación y luminosidad en una sola visita.</p>"),
  ],
  faqs=[
   ("¿Cuántas sesiones se recomiendan?",
    "Para luminosidad puntual, una sesión ya se nota. Para renovar la piel en profundidad te propondremos un ciclo personalizado según su estado."),
   ("¿Puedo hacerla si tengo acné activo?",
    "Con brotes activos importantes no se recomienda. Valoramos tu piel antes y te proponemos la alternativa adecuada."),
   ("¿Duele la microdermoabrasión?",
    "No. Se nota un ligero arrastre sobre la piel, similar a una exfoliación intensa. No requiere anestesia ni deja la piel dañada."),
   ("¿Qué beneficios tiene frente a un peeling químico?",
    "Es mecánica y progresiva: controlamos la intensidad al momento y la piel se recupera antes. Es una buena opción para quien prefiere evitar ácidos."),
  ],
  rel=["higiene-facial", "depilacion-laser"],
 ),
}


def seccion_por_que_aqua(nombre):
    return (
        f"Por qué elegir Aqua para tu {nombre.lower()} en Sant Feliu",
        "<p>Llevamos más de 20 años cuidando a clientas y clientes de Sant Feliu de Llobregat y alrededores. "
        "Nuestro salón de la Rambla Marquesa de Castellbell combina un trato cercano con tecnología actual.</p>"
        "<p>Más de 5.000 personas han confiado en nosotros. Nuestra valoración media es de 4,8 sobre 5. "
        "Cada tratamiento empieza con una valoración personalizada y sin compromiso.</p>"
        "<p>Si tienes dudas, escríbenos por WhatsApp. Te respondemos rápido y te aconsejamos "
        "el tratamiento que de verdad necesitas, sin venderte nada que no te aporte.</p>",
    )


def wa_link(servicio):
    msg = f"Hola, me gustaría reservar una cita para {servicio} en Aqua Perruquers"
    return f"https://wa.me/{TEL_WA}?text={urllib.parse.quote(msg)}"


def srcset(base, variants, orig_w):
    parts = [f"/img/{base}-{s}.webp {w}w" for s, w in variants]
    parts.append(f"/img/{base}.webp {orig_w}w")
    return ", ".join(parts)


def jsonld_business():
    return {
        "@context": "https://schema.org",
        "@type": ["HairSalon", "BeautySalon"],
        "@id": f"{DOMAIN}/#negocio",
        "name": "Aqua Perruquers",
        "url": f"{DOMAIN}/",
        "image": f"{DOMAIN}/img/salon-peluqueria-sant-feliu.webp",
        "telephone": "+34692039950",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Rambla Marquesa de Castellbell, 63",
            "addressLocality": "Sant Feliu de Llobregat",
            "addressRegion": "Barcelona",
            "postalCode": "08980",
            "addressCountry": "ES",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": 41.384568, "longitude": 2.045679},
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification",
             "dayOfWeek": ["Tuesday", "Wednesday", "Thursday", "Friday"],
             "opens": "10:00", "closes": "19:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday",
             "opens": "10:00", "closes": "14:00"},
        ],
        "sameAs": ["https://www.instagram.com/aqua_perruquers/"],
    }


def render(slug, p):
    nombre = NAME[slug]
    wa = wa_link(nombre)
    drop_items = "\n          ".join(
        f'<a href="/{s}">{n}</a>' for s, n in MENU)
    mobile_items = "\n      ".join(
        f'<a href="/{s}">{n}</a>' for s, n in MENU)

    secciones = list(p["secciones"]) + [seccion_por_que_aqua(nombre)]
    secciones_html = "\n".join(
        f'        <section>\n          <h2>{h2}</h2>\n          {cuerpo}\n        </section>'
        for h2, cuerpo in secciones)

    faqs = list(p["faqs"])
    faqs_html = "\n".join(
        f'        <details class="faq-item">\n          <summary>{q}</summary>\n          <p>{a}</p>\n        </details>'
        for q, a in faqs)

    rel_html = "\n          ".join(
        f'<a href="/{s}">{NAME[s]} →</a>' for s in p["rel"])

    base, variants, ow, oh = p["img"]
    img_srcset = srcset(base, variants, ow)
    fallback = f"/img/{base}-{variants[-1][0]}.webp"

    ld_service = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": nombre,
        "description": p["meta"],
        "url": f"{DOMAIN}/{slug}",
        "areaServed": "Sant Feliu de Llobregat",
        "provider": {"@id": f"{DOMAIN}/#negocio"},
    }
    ld_faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }
    ld_crumbs = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": f"{DOMAIN}/"},
            {"@type": "ListItem", "position": 2, "name": nombre, "item": f"{DOMAIN}/{slug}"},
        ],
    }

    def ld(obj):
        return json.dumps(obj, ensure_ascii=False, indent=2)

    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{p['title']}</title>
  <meta name="description" content="{p['meta']}">
  <link rel="canonical" href="{DOMAIN}/{slug}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="#06b6d4">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_ES">
  <meta property="og:site_name" content="Aqua Perruquers">
  <meta property="og:title" content="{p['title']}">
  <meta property="og:description" content="{p['meta']}">
  <meta property="og:url" content="{DOMAIN}/{slug}">
  <meta property="og:image" content="{DOMAIN}/img/{base}.webp">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{p['title']}">
  <meta name="twitter:description" content="{p['meta']}">
  <meta name="twitter:image" content="{DOMAIN}/img/{base}.webp">
  <link rel="icon" type="image/webp" href="/img/logo-aqua-perruquers.webp">
  <link rel="stylesheet" href="/css/styles.css">
  <script type="application/ld+json">
{ld(jsonld_business())}
  </script>
  <script type="application/ld+json">
{ld(ld_service)}
  </script>
  <script type="application/ld+json">
{ld(ld_faq)}
  </script>
  <script type="application/ld+json">
{ld(ld_crumbs)}
  </script>
</head>
<body>
  <a class="skip-link" href="#contenido">Saltar al contenido</a>
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="brand" aria-label="Aqua Perruquers — Inicio">
        <img src="/img/logo-aqua-80.webp" alt="Logotipo de Aqua Perruquers" width="40" height="40">
        <span class="brand-name">AQUA</span>
      </a>
      <nav class="main-nav" aria-label="Navegación principal">
        <a href="/">Inicio</a>
        <div class="nav-drop">
          <a href="/#servicios" aria-haspopup="true">Tratamientos ▾</a>
          <div class="drop-menu">
          {drop_items}
          </div>
        </div>
        <a href="/#resenas">Reseñas</a>
        <a href="/#contacto">Contacto</a>
      </nav>
      <a class="btn btn-primary header-cta" href="{wa}" target="_blank" rel="noopener noreferrer">Reservar Cita</a>
      <button class="menu-toggle" aria-expanded="false" aria-controls="mobile-nav" aria-label="Abrir menú">☰</button>
    </div>
    <nav class="mobile-nav" id="mobile-nav" aria-label="Navegación móvil" hidden>
      <a href="/">Inicio</a>
      {mobile_items}
      <a href="/#contacto">Contacto</a>
      <a class="btn btn-primary" href="{wa}" target="_blank" rel="noopener noreferrer">Reservar Cita</a>
    </nav>
  </header>

  <main id="contenido" class="section service-page">
    <div class="container container-narrow">
      <nav class="breadcrumbs" aria-label="Migas de pan">
        <a href="/">Inicio</a> › <span>{nombre}</span>
      </nav>
      <article class="service-content">
        <h1>{p['h1']}</h1>
        <p class="service-intro">{p['intro']}</p>
        <p><a class="btn btn-primary" href="{wa}" target="_blank" rel="noopener noreferrer" aria-label="Reservar cita para {nombre} por WhatsApp">Reservar por WhatsApp</a></p>
        <figure class="service-hero-img">
          <img src="{fallback}" srcset="{img_srcset}" sizes="(min-width: 832px) 770px, 92vw" alt="{p['alt']}" width="{ow}" height="{oh}" loading="lazy">
        </figure>
{secciones_html}
        <section>
          <h2>Preguntas frecuentes</h2>
{faqs_html}
        </section>
        <section class="related">
          <h2>También te puede interesar</h2>
          <div class="related-grid">
          {rel_html}
          </div>
        </section>
        <div class="cta-banner">
          <h3>Reserva tu cita de {nombre}</h3>
          <p>Estamos en Rambla Marquesa de Castellbell, 63, Sant Feliu de Llobregat. Te confirmamos la hora al momento.</p>
          <a class="btn btn-light" href="{wa}" target="_blank" rel="noopener noreferrer" aria-label="Reservar cita para {nombre} por WhatsApp">Reservar por WhatsApp</a>
        </div>
      </article>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container footer-bottom">
      <p>© 2026 Aqua Perruquers · Rambla Marquesa de Castellbell, 63 · Sant Feliu de Llobregat · <a href="tel:+34692039950">692 03 99 50</a></p>
      <nav aria-label="Enlaces legales">
        <a href="/aviso-legal">Aviso Legal</a> ·
        <a href="/politica-privacidad">Política de Privacidad</a> ·
        <a href="/politica-cookies">Política de Cookies</a>
      </nav>
    </div>
  </footer>

  <a class="whatsapp-fab" href="{wa}" target="_blank" rel="noopener noreferrer" aria-label="Reservar cita por WhatsApp">
    <svg viewBox="0 0 32 32" width="28" height="28" aria-hidden="true" fill="currentColor"><path d="M16 .5C7.4.5.5 7.4.5 16c0 2.7.7 5.4 2 7.7L.5 31.5l8-2.1c2.3 1.2 4.8 1.9 7.5 1.9 8.6 0 15.5-6.9 15.5-15.5S24.6.5 16 .5zm0 28.2c-2.4 0-4.7-.6-6.7-1.8l-.5-.3-4.7 1.2 1.3-4.6-.3-.5c-1.3-2-2-4.4-2-6.8C3.1 8.9 8.9 3.1 16 3.1S28.9 8.9 28.9 16 23.1 28.7 16 28.7zm7.1-9.6c-.4-.2-2.3-1.1-2.6-1.3-.4-.1-.6-.2-.9.2-.3.4-1 1.3-1.3 1.5-.2.3-.5.3-.9.1-.4-.2-1.6-.6-3.1-1.9-1.1-1-1.9-2.3-2.1-2.6-.2-.4 0-.6.2-.8.2-.2.4-.5.6-.7.2-.2.3-.4.4-.7.1-.3.1-.5 0-.7-.1-.2-.9-2.1-1.2-2.9-.3-.8-.6-.7-.9-.7h-.8c-.3 0-.7.1-1.1.5-.4.4-1.4 1.4-1.4 3.4s1.4 3.9 1.6 4.2c.2.3 2.8 4.3 6.8 6 4 1.7 4 1.1 4.7 1.1.7-.1 2.3-.9 2.6-1.8.3-.9.3-1.7.2-1.8-.1-.2-.4-.3-.8-.5z"/></svg>
  </a>

  <script src="/js/main.js" data-cfasync="false" defer></script>
</body>
</html>
"""


def main():
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))
    for slug, page in PAGES.items():
        with open(f"{slug}.html", "w", encoding="utf-8") as f:
            f.write(render(slug, page))
        print(f"{slug}.html OK")


if __name__ == "__main__":
    main()
