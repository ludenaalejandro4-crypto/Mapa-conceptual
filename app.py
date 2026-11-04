import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Perífrasis Verbales", layout="wide")

st.markdown("""
    <style>
        .block-container { padding: 0rem; max-width: 100%; }
        header { display: none; }
        iframe { border: none; }
    </style>
""", unsafe_allow_html=True)

canva_html = """
<!doctype html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/lucide@0.577.0/dist/umd/lucide.min.js"></script>
  <style>
    :root { --base:#0c1429;--panel:#141e36;--panel2:#1a2540;--line:#788cae;--ink:#eef3ff;--muted:#9baac7;--border:#293752; }
    * { box-sizing:border-box }
    body { margin:0; width:100%; min-height:100vh; color:var(--ink); font-family:'DM Sans',sans-serif; background:var(--base) }
    body.light { --base:#eaf0f8;--panel:#fff;--panel2:#f3f6fc;--line:#788ba6;--ink:#17243a;--muted:#53647e;--border:#cdd8e8 }
    
    .app-shell { width:100%; min-height:100vh;display:flex;flex-direction:column }
    .topbar { height:54px;flex:none;background:var(--panel);border-bottom:1px solid var(--border);display:flex;align-items:center;padding:0 18px;gap:12px }
    .brand-mark { width:34px;height:34px;border-radius:9px;background:#20375f;color:#9dd8ff;display:grid;place-items:center;box-shadow:inset 0 0 0 1px #426392 }
    .workarea { display:grid;grid-template-columns:150px minmax(0,1fr);flex:1;min-height:0 }
    
    .rail { border-right:1px solid var(--border);display:flex;flex-direction:column;gap:9px;background:var(--panel);padding:17px 12px }
    .rail-button { width:100%;display:flex;align-items:center;gap:9px;padding:10px 11px;border-radius:9px;color:var(--ink);text-align:left;transition:background .2s;cursor:pointer;border:none;background:transparent;font-weight:600 }
    .rail-button:hover { background:var(--panel2) }
    .rail-button.primary { background:#5546df;color:white;box-shadow:0 5px 16px #453ac055 }
    .rail-button svg { width:17px;height:17px;flex:none }
    .rail-caption { font-size:10px;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);margin:17px 9px 4px;font-weight:bold }
    
    .canvas { min-width:0;overflow:auto;background-color:var(--base);background-image:radial-gradient(circle, #8090b029 1px, transparent 1px);background-size:18px 18px;padding:26px 20px 48px;display:flex;flex-direction:column;align-items:center }
    .canvas-inner { width:100%;max-width:1040px;min-width:670px;text-align:center }
    
    .eyebrow-btn { display:inline-block; font-family:'Space Mono',monospace; letter-spacing:.21em; font-size:11px; color:var(--muted); margin-bottom:22px; }
    
    .root-wrap { display:flex;justify-content:center;position:relative;padding-bottom:39px }
    .root-wrap:after { content:"";position:absolute;bottom:0;left:50%;height:39px;border-left:2px solid var(--line) }
    .branch-grid { display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;position:relative;padding-top:28px }
    .branch-grid:before { content:"";position:absolute;top:0;left:16.666%;right:16.666%;border-top:2px solid var(--line) }
    .branch { position:relative;min-width:0 }
    .branch:before { content:"";position:absolute;top:-28px;left:50%;height:28px;border-left:2px solid var(--line) }
    .category-wrap { display:flex;justify-content:center;position:relative;padding-bottom:33px }
    .category-wrap:after { content:"";position:absolute;bottom:0;left:50%;height:33px;border-left:2px solid var(--line) }
    .leaves { display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:7px;position:relative;padding-top:23px }
    .leaves.two { grid-template-columns:repeat(2,minmax(0,1fr)) }
    .leaves:before { content:"";position:absolute;top:0;left:16.666%;right:16.666%;border-top:2px solid var(--line) }
    .leaves.two:before { left:25%;right:25% }
    .leaf { position:relative;min-width:0 }
    .leaf:before { content:"";position:absolute;top:-23px;left:50%;height:23px;border-left:2px solid var(--line) }
    
    .node { position:relative;display:flex;align-items:center;justify-content:center;gap:10px;width:100%;min-height:70px;padding:13px;border:1px solid #ffffff75;border-radius:13px;color:#fff;text-align:center;box-shadow:0 12px 23px #0003,0 0 22px 5px color-mix(in srgb, currentColor 32%, transparent);transition:transform .18s;cursor:pointer;background:transparent }
    .node:hover { transform:translateY(-3px);box-shadow:0 17px 26px #0005,0 0 30px 8px color-mix(in srgb, currentColor 42%, transparent) }
    .node.root { width:278px;min-height:80px;background:linear-gradient(140deg,#6360f4,#3547ad);border-color:#94a9ff }
    .node.category { max-width:240px }
    .node.leaf-node { flex-direction:column;justify-content:center;gap:8px;min-height:95px;padding:10px 5px;text-align:center;border-color:#bad5e4 }
    
    .node-icon { width:31px;height:31px;flex:none;stroke-width:2.3 }
    .root .node-icon { width:42px;height:42px }
    .leaf-node .node-icon { width:26px;height:26px }
    
    .node-title { display:block;font-weight:800;font-size:16px;line-height:1.15;color:#fff;text-shadow:0 2px 10px #071329aa; }
    .root .node-title { font-size:22px }
    .leaf-node .node-title { font-size:13px; }
    
    .bibliography { width:100%; max-width:1040px; margin:40px auto 0; padding:16px 20px; border:1px solid #52658c; border-radius:14px; background:linear-gradient(135deg,#182544,#101a31); box-shadow:0 10px 24px #0003; text-align:left; cursor:pointer; transition:transform .2s, box-shadow .2s; }
    .bibliography:hover { transform:translateY(-2px); box-shadow:0 15px 30px #0005, 0 0 15px #52658c; }
    .bibliography h2 { margin:0 0 6px; color:#ffd166; font-size:14px; font-weight:800; }
    .bibliography p { margin:0; color:#b8c8ed; font-size:12px; line-height: 1.5; }
    body.light .bibliography { background:#fff; border-color:#cdd8e8; }
    body.light .bibliography h2 { color:#d97706; }
    body.light .bibliography p { color:#475569; }

    .detail { position:fixed;inset:0;z-index:10;display:flex;flex-direction:column;overflow:auto;background:var(--base);padding:30px;opacity:0;visibility:hidden;pointer-events:none;transition:opacity .22s ease }
    .detail.open { opacity:1;visibility:visible;pointer-events:auto; }
    .detail-toolbar { display:flex;justify-content:space-between;max-width:1200px;width:100%;margin:0 auto; flex-shrink: 0; }
    .detail-back { display:flex;align-items:center;gap:10px;padding:12px 20px;border-radius:12px;background:linear-gradient(135deg,#ff4f9a,#7c5cff);color:#fff;font-size:15px;font-weight:800;cursor:pointer;border:none; }
    
    .detail-layout { width:100%;max-width:1000px;margin:20px auto;display:flex; flex-grow: 1; }
    .detail-card { width: 100%; border-radius:25px;padding:50px;color:white;display:flex;flex-direction:column;justify-content:center; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
    .detail-title { font-size:48px;font-weight:800;margin:0 0 20px 0; line-height: 1.1; }
    .detail-description { font-size:19px;line-height:1.7; opacity: 0.95; }
    
    .hint-box { margin-top:20px; border:1px solid var(--border); border-radius:11px; padding:12px; font-size:12px; color:var(--muted); line-height:1.4; }

    /* Reglas para celular */
    @media (max-width: 768px) {
        .workarea { display: flex; flex-direction: column; }
        .rail { flex-direction: row; justify-content: space-around; border-right: none; border-bottom: 1px solid var(--border); padding: 10px; }
        .rail-button { width: auto; padding: 8px 12px; font-size: 12px; }
        .rail-caption, .hint-box { display: none; }
        .canvas { padding: 15px 5px; }
        .canvas-inner { min-width: 100%; overflow-x: auto; }
        .branch-grid { gap: 5px; }
        .node.root { width: 200px; min-height: 60px; padding: 5px; }
        .node.category { min-height: 60px; padding: 5px; }
        .node.leaf-node { min-height: 80px; padding: 5px; }
        .node-title { font-size: 12px; }
        .root .node-title { font-size: 16px; }
        .leaf-node .node-title { font-size: 11px; }
        .node-icon { width: 24px; height: 24px; }
        .detail-card { padding: 25px; }
        .detail-title { font-size: 32px; }
        .detail-description { font-size: 16px; }
    }
  </style>
</head>
<body>
  <div class="app-shell">
   <header class="topbar">
    <div class="brand-mark"><i data-lucide="network"></i></div>
    <div>
     <h1 style="font-size: 15px; margin: 0;">Perífrasis Verbales</h1>
     <p style="font-size: 10px; margin: 0; color: var(--muted);">Organizador gráfico interactivo</p>
    </div>
   </header>
   
   <main class="workarea">
    <nav class="rail">
     <button type="button" id="home-button" class="rail-button primary"><i data-lucide="layout-dashboard"></i><span>Inicio</span></button>
     <p class="rail-caption">Apariencia</p>
     <button type="button" id="theme-button" class="rail-button"><i data-lucide="moon"></i><span class="dark-label">Modo claro</span><span class="light-label" style="display:none;">Modo oscuro</span></button>
     <div class="hint-box">Haz clic en cualquier cuadro para leer la información completa.</div>
    </nav>
    
    <section class="canvas" id="main-canvas">
     <div class="canvas-inner">
      
      <div class="eyebrow-btn">MAPA CONCEPTUAL · PERÍFRASIS VERBALES</div>
      
      <div class="root-wrap">
        <button type="button" class="node root" data-node="root">
          <i data-lucide="languages" class="node-icon"></i>
          <span class="node-copy"><span class="node-title"></span></span>
        </button>
      </div>
      
      <div class="branch-grid">
       <div class="branch">
        <div class="category-wrap"><button type="button" class="node category" data-node="concept"><i data-lucide="book-open" class="node-icon"></i><span class="node-copy"><span class="node-title"></span></span></button></div>
        <div class="leaves two">
         <div class="leaf"><button type="button" class="node leaf-node" data-node="process"><i data-lucide="book-a" class="node-icon"></i><span class="node-copy"><span class="node-title"></span></span></button></div>
         <div class="leaf"><button type="button" class="node leaf-node" data-node="training"><i data-lucide="blocks" class="node-icon"></i><span class="node-copy"><span class="node-title"></span></span></button></div>
        </div>
       </div>
       <div class="branch">
        <div class="category-wrap"><button type="button" class="node category" data-node="elements"><i data-lucide="settings" class="node-icon"></i><span class="node-copy"><span class="node-title"></span></span></button></div>
        <div class="leaves">
         <div class="leaf"><button type="button" class="node leaf-node" data-node="teacher"><i data-lucide="wrench" class="node-icon"></i><span class="node-copy"><span class="node-title"></span></span></button></div>
         <div class="leaf"><button type="button" class="node leaf-node" data-node="student"><i data-lucide="link" class="node-icon"></i><span class="node-copy"><span class="node-title"></span></span></button></div>
         <div class="leaf"><button type="button" class="node leaf-node" data-node="curriculum"><i data-lucide="type" class="node-icon"></i><span class="node-copy"><span class="node-title"></span></span></button></div>
        </div>
       </div>
       <div class="branch">
        <div class="category-wrap"><button type="button" class="node category" data-node="purpose"><i data-lucide="target" class="node-icon"></i><span class="node-copy"><span class="node-title"></span></span></button></div>
        <div class="leaves">
         <div class="leaf"><button type="button" class="node leaf-node" data-node="development"><i data-lucide="scale" class="node-icon"></i><span class="node-copy"><span class="node-title"></span></span></button></div>
         <div class="leaf"><button type="button" class="node leaf-node" data-node="learning"><i data-lucide="hourglass" class="node-icon"></i><span class="node-copy"><span class="node-title"></span></span></button></div>
         <div class="leaf"><button type="button" class="node leaf-node" data-node="growth"><i data-lucide="calendar-clock" class="node-icon"></i><span class="node-copy"><span class="node-title"></span></span></button></div>
        </div>
       </div>
      </div>
      
      <section class="bibliography" data-node="bibliography">
        <h2 id="bib-title">Bibliografía</h2>
        <p id="bib-desc"></p>
      </section>
      
     </div>
    </section>
   </main>
  </div>

  <section id="detail" class="detail">
   <div class="detail-toolbar">
    <button id="back-button" type="button" class="detail-back"><i data-lucide="arrow-left"></i><span>Volver al organizador</span></button>
   </div>
   <div class="detail-layout">
    <article id="detail-card" class="detail-card">
     <h2 id="detail-title" class="detail-title"></h2>
     <div id="detail-description" class="detail-description"></div>
    </article>
   </div>
  </section>

  <script>
    const defaults = {
      root:{title:"Perífrasis verbales",description:"Son combinaciones de dos verbos que funcionan como uno solo: el primero (auxiliar) se conjuga y el segundo (auxiliado) va en infinitivo, gerundio o participio. Juntos expresan una sola acción con un matiz especial.<br><br><b>Ejemplos:</b><br>• <i>Voy a estudiar esta noche.</i><br>• <i>Estamos leyendo el libro.</i>",color:"#514de1", icon:"languages"},
      concept:{title:"Concepto",description:"<b>¿Qué es una perífrasis verbal y cómo se forma?</b><br>Es la unión de un verbo auxiliar conjugado con un verbo en infinitivo, gerundio o participio, que juntos funcionan como un solo verbo. Se forma así: auxiliar conjugado + (nexo) + forma no personal.<br><br><b>Ejemplos:</b><br>• <i>Debo salir.</i><br>• <i>Estás mintiendo.</i>",color:"#168bd4", icon:"book-open"},
      elements:{title:"Elementos",description:"<b>¿Cuáles son las tres piezas que componen toda perífrasis?</b><br>El verbo auxiliar, el nexo y el verbo auxiliado.<br><br><b>Ejemplos:</b><br>• <i>Tengo</i> (auxiliar) <i>que</i> (nexo) <i>trabajar</i> (auxiliado).<br>• <i>Vamos</i> (auxiliar) <i>a</i> (nexo) <i>cenar</i> (auxiliado).",color:"#25a25f", icon:"settings"},
      purpose:{title:"Finalidad",description:"<b>¿Para qué las usamos?</b><br>Para expresar obligación o posibilidad y dar énfasis (modales y enfáticas), para mostrar en qué fase está la acción (aspectuales) y para ubicarla en el tiempo (temporales).<br><br><b>Ejemplos:</b><br>• <i>Has de estudiar.</i> (obligación)<br>• <i>Se echó a reír.</i> (inicio de la acción)",color:"#e8a32a", icon:"target"},
      process:{title:"Definición",description:"Una perífrasis une un verbo auxiliar conjugado con un verbo en forma no personal, a veces mediante un nexo.<br><br>• El auxiliar pierde, total o parcialmente, su significado propio; por ejemplo, en <i>voy a cantar</i>, el verbo <i>ir</i> ya no indica movimiento.<br>• Todo el conjunto equivale a un solo predicado; es decir, a una sola acción.<br><br><b>Ejemplos:</b><br>• <i>Debes estudiar más.</i><br>• <i>Ella está preparando la clase.</i><br>• <i>Mi hermano acaba de salir.</i>",color:"#0f4c81", icon:"book-a"},
      training:{title:"Formación",description:"<b>Fórmula:</b> auxiliar conjugado + (nexo) + forma no personal.<br><br><b>Ejemplos de la fórmula:</b><br>• <i>tener que</i> + infinitivo (Tengo que madrugar).<br>• <i>estar</i> + gerundio (Estoy escribiendo).<br>• <i>volver a</i> + infinitivo (Volvió a intentarlo).<br><br>Según la forma no personal, las perífrasis son:<br>• De infinitivo: <i>Debemos partir.</i><br>• De gerundio: <i>Vamos mejorando.</i><br>• De participio: <i>Dejó anotada la fecha.</i><br><br><b>Cómo reconocerla:</b><br>El segundo verbo no se puede reemplazar por un pronombre, y ambos verbos comparten el mismo sujeto. Por ejemplo, en <i>Voy a cantar</i>, el sujeto (yo) es el mismo tanto para el verbo <i>ir</i> como para <i>cantar</i>. Además, el segundo verbo no se puede sustituir por un pronombre (<i>Lo voy</i> es incorrecto).<br><br><b>Nota:</b> Los tiempos compuestos no son perífrasis, porque forman parte de la conjugación (<i>he cantado, habían llegado</i>).",color:"#0f4c81", icon:"blocks"},
      teacher:{title:"Verbo auxiliar",description:"Va conjugado y aporta persona, número, tiempo y modo.<br><br>• Su significado propio se debilita y funciona como apoyo gramatical.<br><br><b>Ejemplos:</b><br>• <i>Estamos hablando</i> (primera persona del plural, presente).<br>• <i>Debían entregar el trabajo</i> (tercera persona del plural, pretérito imperfecto).<br><br><b>Otros auxiliares frecuentes:</b> ir, tener, empezar, volver, acabar.",color:"#116239", icon:"wrench"},
      student:{title:"Nexo",description:"Es la palabra que une los dos verbos: una preposición (a, de, por), una conjunción (que, y) o ninguna.<br><br><b>Casos:</b><br>• <b>Con preposición:</b> <i>ir a comer; empezar a llover.</i><br>• <b>Con conjunción:</b> <i>tener que estudiar; haber que esperar.</i><br>• <b>Sin nexo:</b> <i>poder salir; seguir lloviendo.</i>",color:"#116239", icon:"link"},
      curriculum:{title:"Verbo auxiliado",description:"Va siempre en forma no personal y aporta el significado principal de la acción.<br><br><b>Formas:</b><br>• <b>Infinitivo:</b> <i>soler madrugar; deber estudiar.</i><br>• <b>Gerundio:</b> <i>estar comiendo; seguir leyendo.</i><br>• <b>Participio:</b> <i>tener hechos los deberes; llevar vendidas mil copias.</i>",color:"#116239", icon:"type"},
      development:{title:"Modales y enfáticas",description:"Muestran la actitud del hablante hacia la acción: obligación, posibilidad o énfasis.<br><br><b>Modales de obligación:</b> <i>tener que, haber que, haber de, deber</i> + infinitivo.<br>• <i>Tienes que entregar el informe.</i><br>• <i>Hay que revisar el texto.</i><br>• <i>He de confesarlo.</i><br>• <i>Debes respetar las normas.</i><br><br><b>Modales de posibilidad o probabilidad:</b> <i>poder, deber de</i> + infinitivo.<br>• <i>Puede llover esta tarde.</i><br>• <i>Debe de estar en casa.</i><br><br><b>Enfáticas o discursivas:</b> dan fuerza expresiva mediante <i>verbo + y + verbo</i> (coger y, ir y, agarrar y).<br>• <i>Cogió y se fue.</i><br>• <i>Fue y lo dijo.</i><br>• <i>Agarró y renunció.</i>",color:"#b87013", icon:"scale"},
      learning:{title:"Aspectuales",description:"Muestran cómo se desarrolla la acción; es decir, en qué fase se encuentra.<br><br>• <b>Ingresiva</b> (a punto de empezar): <i>estar a punto de</i> + infinitivo.<br><i>Ejemplos: Estoy a punto de salir. / El tren está a punto de partir.</i><br><br>• <b>Incoativa</b> (empieza): <i>empezar a, ponerse a, echar a</i> + infinitivo.<br><i>Ejemplos: Empezó a llover. / Se puso a estudiar. / Echó a correr.</i><br><br>• <b>Durativa</b> (continúa): <i>estar, seguir, andar</i> + gerundio.<br><i>Ejemplos: Sigue trabajando. / Anda buscando empleo.</i><br><br>• <b>Reiterativa</b> (se repite): <i>volver a</i> + infinitivo.<br><i>Ejemplos: Volvió a llamar. / Vuelvo a leer el capítulo.</i><br><br>• <b>Habitual</b> (se hace con frecuencia): <i>soler</i> + infinitivo.<br><i>Ejemplos: Suele llegar tarde. / Solemos cenar temprano.</i><br><br>• <b>Terminativa</b> (acaba): <i>dejar de, terminar de</i> + infinitivo.<br><i>Ejemplos: Dejó de fumar. / Terminé de escribir el ensayo.</i><br><br>• <b>Resultativa</b> (estado resultante): <i>tener, llevar</i> + participio.<br><i>Ejemplos: Tengo escrita la carta. / Llevo leídas tres páginas.</i>",color:"#b87013", icon:"hourglass"},
      growth:{title:"Temporales",description:"Ubican la acción en el tiempo.<br><br>• <b>Futuro próximo:</b> <i>ir a</i> + infinitivo.<br><i>Ejemplos: Voy a viajar mañana. / Vamos a estrenar la obra el viernes.</i><br><br>• <b>Pasado reciente:</b> <i>acabar de</i> + infinitivo.<br><i>Ejemplos: Acabo de llegar. / Acaban de anunciar los resultados.</i>",color:"#b87013", icon:"calendar-clock"},
      bibliography:{title:"Bibliografía",description:"• Gómez Torrego, L. (1988). <i>Perífrasis verbales: Sintaxis, semántica y estilística</i>. Arco/Libros.<br><br>• Real Academia Española y Asociación de Academias de la Lengua Española. (2009). <i>Nueva gramática de la lengua española: Sintaxis II</i> (cap. 28). Espasa.",color:"#182544", icon:""}
    };

    let selected = "root";
    const $ = id => document.getElementById(id);
    function data(id){ return defaults[id]; }
    
    function paint(){
      document.querySelectorAll("[data-node]").forEach(element => {
        const d = data(element.dataset.node);
        
        if (element.dataset.node === 'bibliography') {
            element.querySelector("h2").textContent = d.title;
            element.querySelector("p").innerHTML = d.description;
            element.style.background = d.color;
        } else {
            element.querySelector(".node-title").textContent = d.title;
            
            const iconEl = element.querySelector(".node-icon");
            if (iconEl && d.icon) {
                const newIcon = document.createElement("i");
                newIcon.setAttribute("data-lucide", d.icon);
                newIcon.className = "node-icon";
                iconEl.replaceWith(newIcon);
            }
            
            element.style.background = d.color;
        }
      });
      lucide.createIcons();
    }

    function select(id){
      selected = id;
      const d = data(selected);
      
      $("detail-title").textContent = d.title;
      $("detail-description").innerHTML = d.description;
      $("detail-card").style.background = d.color;
      
      $("detail").classList.add("open");
    }

    function goHome(){
      $("detail").classList.remove("open");
    }

    document.querySelectorAll("[data-node]").forEach(b=>b.addEventListener("click",()=>select(b.dataset.node)));
    $("back-button").addEventListener("click",goHome);
    $("home-button").addEventListener("click",goHome);

    $("theme-button").addEventListener("click",()=>{
      const light = document.body.classList.toggle("light");
      document.querySelector(".dark-label").style.display = light ? "none" : "block";
      document.querySelector(".light-label").style.display = light ? "block" : "none";
    });

    paint();
  </script>
</body>
</html>
"""

components.html(canva_html, height=950, scrolling=True)