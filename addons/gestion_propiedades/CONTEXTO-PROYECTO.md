# 🎓 PROYECTO FINAL DAW — Ilerna Online

## 👋 Contexto del proyecto (IMPORTANTE - LÉELO)

**Estás trabajando en el PROYECTO INTERMODULAR de la asignatura final del ciclo DAW** (CFGS Desarrollo de Aplicaciones Web — Ilerna Online). Este módulo Odoo es **la aplicación web** que se entrega como Proyecto Fin de Ciclo.

- **Título del proyecto:** Sistema de gestión de propiedades y mantenimiento para inmobiliaria
- **Propuesta de tema:** ✅ APTA (13/13 puntos en el campus)
- **Autor:** Diego Leyes Mijas
- **Environment:** Odoo 18, Docker. Una inmobiliaria real de la Costa del Sol necesita gestionar su cartera: sustituir Excel, agenda física y WhatsApp por un sistema centralizado.

## 📅 FECHAS QUE NO SE PUEDEN PISAR

| Hito                         | Fecha       |
|------------------------------|-------------|
| Feedback voluntario (memoria draft) | 03/11/2026 |
| **ENTREGA FINAL** (todo)          | **11/12/2026** |

## 📦 Entrega final (11/12)

1. Memoria escrita .docx + .pdf (30-60 pág, Arial 11, interlineado 1.5, justificado)
2. Vídeo de defensa .mp4 (15-25 min, sin cortes, demo en vivo)
3. Presentación .pptx (20-25 diapositivas, letra 24-28)
4. Código fuente .zip (sin subcarpetas)
5. En campus: PDF de la memoria + enlace Drive en portada

## ⚠️ REGLAS CRÍTICAS (suspensión directa)

- ❌ Memoria redactada por IA → SUSPENSO (el alumno redacta)
- ❌ Código autogenerado en exceso → penalización
- ❌ Repositorio PÚBLICO del código → riesgo (usar GitHub PRIVADO si se sube)
- ❌ BD no relacional / <3 tablas → SUSPENSO
- ❌ Falta de Estado del Arte o Bibliografía → SUSPENSO directo
- ✅ Odoo justificado (tutor aprobó + prácticas en empresa partner)

## 🎯 QUÉ CONSTRUYE ESTE MÓDULO

### Funcionalidades obligatorias (propuesta aprobada)

1. **Login personalizado** (HTML/CSS/JS) — user/password + roles
2. **CRUD de propiedades** con estado de alquiler (disponible/alquilada)
3. **CRUD de tareas** con workflow de estados: pendiente → en curso → completada (botones)
4. **Asignación responsable ↔ propiedad ↔ tarea**
5. **Roles + permisos por registro:** admin ve todo / responsable ve SOLO sus tareas
6. **Filtros y búsqueda** (estado, prioridad, responsable, propiedades)
7. **Vista de calendario** de tareas
8. **Informe PDF** de parte de trabajo (QWeb)
9. **Despliegue Docker** (Odoo + PostgreSQL + pgAdmin)
10. **Notificaciones por email** (chatter y/O mail del módulo mail)

### Roles

| Rol | Permisos |
|-----|----------|
| **Administrador** (inmobiliaria) | Todo: propiedades, responsables, tareas, informes, vista global |
| **Responsable** (encargado de finca) | Ver SOLO sus tareas, cambiar estado, registrar horas, generar parte PDF |

### Tablas (BD relacional — mínimo 3: llevamos 4)

1. **propiedades**   → nombre (`Char, required`), direccion, tipo (`piso/casa/local`), estado_alquiler (`disponible/alquilada`), responsable_id (`FK responsables`), notas
2. **responsables** → nombre (`Char, required`), email, telefono, tipo (`llaves/limpieza/arreglos`), usuario_id (`FK res.users` para login)
3. **tareas**          → titulo (`Char, required`), descripcion, tipo, estado (`pendiente/en_curso/completada`), prioridad, fecha_programada, fecha_limite, horas, propiedad_id (`FK`), responsable_id (`FK`)
4. **historial**       → tarea_id (`FK`), fecha, descripcion, horas (ampliación, si sobra tiempo)

## 🗺️ PLAN DE CONSTRUCCIÓN — SPRINT ACTUAL (seguimiento)

- [x] **Sprint 0:** Propuesta APTA ✅ + entrenamiento previo completado (aprendizaje de Odoo; módulos de práctica eliminados del repo y BD — trazas documentadas en NOTAS-DEFENSA §7)
- [x] **Sprint 1 (✅ COMPLETADO 29/10/2026):** Estructura base + modelos + instalación
  - [x] Carpetas creadas (`models/`, `views/`, `security/`)
  - [x] `__init__.py` raíz y en models (conectados: `from . import`)
  - [x] Tarea 2: `__manifest__.py` (deps `['base','mail']`, `application:True`, license LGPL-3, version 18.0.1.0.0)
  - [x] Modelo `models/propiedades.py` (gp.propiedades: valores exactos de la propuesta + default disponible)
  - [x] Modelo `models/responsables.py` (gp.responsables: tipo llaves/limpieza/arreglos + usuario_id → res.users)
  - [x] Modelo `models/tareas.py` (gp.tareas: estado pendiente/en_curso/completada, prioridad 4 niveles, ondelete restrict en propiedad_id)
  - [x] Instalar módulo en Odoo (**verificado: state=installed** en BD `mantenimiento_id`)
  - [x] Validar tablas en PG: `gp_propiedades`, `gp_responsables`, `gp_tareas` ✔ (psql + pgAdmin)
  - Notas: `gp_historial` queda para Sprint 4+ junto a `@api.constrains` (ampliación de la propuesta). Errores típicos corregidos en el camino: (coma de dict, cierre de Selection) → anotados en NOTAS-DEFENSA.md
- [x] **Sprint 2 escalón 1 (✅ 05/11/2026):** vistas de propiedades + desbloqueo de la app
  - [x] `views/propiedades_views.xml`: acción + list (decoration success/warning) + form (2 groups + notas a ancho) + search (filtros Disponibles/Alquiladas + Agrupar por Estado/Responsable)
  - [x] Menús: `menu_gp_root` (raíz, sale en la rejilla de apps) + `menu_gp_propiedades` (hijo con acción)
  - [x] fix: marcador `<título...>` en línea 6 (XML inválido) y limpieza de plantilla
  - [x] `config/odoo.conf` + `db_host/db_port/db_user/db_password` → CLI `docker compose exec odoo odoo -d ...` ya conecta (el exec NO pasa por el entrypoint que traduce HOST=db)
  - [x] **ACL mínima (ADELANTADA de Sprint 3):** `security/ir.model.access.csv` con CRUD completo para `base.group_user` en los 4 modelos → el webclient oculta menús cuyo modelo no es accesible; sin ACL la app existía en BD pero no se pintaba en la rejilla
  - [x] Verificado por dentro: XML cargó (`loading data/views/propiedades_views.xml`), 2 menús en `ir_ui_menu`, 4 ACL activas
  - Pendiente: confirmación visual del icono en rejilla tras `docker compose restart odoo` + F5
- [ ] **Sprint 2 escalón 2 (ACTUAL):** vista de TAREAS — list + form + search + **calendario** (`date_start="fecha_programada"`) + menús bajo el root; opcional: One2many tareas en el form de propiedades
- [ ] **Sprint 3:** grupos de seguridad `group_admin_gp`/`group_responsable_gp` + ACL diferenciada por grupo + `ir.rule` (responsable ve SOLO sus tareas) — se parte del CSV mínimo ya existente
- [ ] **Sprint 4:** Workflow de tareas (botones de estado + `@api.constrains` de horas); `gp_historial` entra aquí si sobra tiempo
- [ ] **Sprint 5:** Login personalizado HTML/CSS/JS (plantilla web hereda login)
- [ ] **Sprint 6:** Informe QWeb (PDF) de parte de trabajo
- [ ] **Sprint 7:** Notificaciones por email + chatter en tareas
- [ ] **Sprint 8:** Despliegue Docker documentado (anexo memoria: manual instalación)
- [ ] **Sprint 9:** Memoria: Análisis (ER, CU, clases) y Diseño (mockups)
- [ ] **Sprint 10:** Memoria: válido (Estado del arte, metodología, planificación, Gantt, DAFO)
- [ ] **Sprint 11:** Defensa: PPTX + guion + demo en vivo

## 🐳 ENTORNO (arrancar/parar)

```bash
cd ~/odoo-mantenimiento
docker compose start                # arrancar
docker compose stop                 # parar
docker compose restart              # reiniciar tras cambios
docker compose logs -f odoo         # ver errores en vivo

# ACCESOS
# Odoo:    http://localhost:8069        (admin@practica.com / admin)
# pgAdmin: http://localhost:5050        (admin@practica.com / admin)
#          conexión: host=db, puerto=5432, user=odoo, pass=odoo
```

## 📚 Documentación completa del proyecto

La memoria, normativa, planificación y estado del proyecto vive en:

```
~/Ilerna/proyecto intermodular daw/
├── TEMA-PROYECTO.md          ← detalle de tablas, objetivos, demo video
├── ESTADO-PROYECTO.md        ← dónde estamos (actualizado tras cada sesión)
├── PLAN-DE-TRABAJO.md        ← plan completo hasta el 11/12
└── feedback-2026-11-03/      ← material del feedback (diagramas Mermaid... PlantUML)
```

## 💡 Recordatorios de trabajo (patrones del addon)

- **Todo el código nuevo se construye aquí, desde 0** (el proyecto no reutiliza código ajeno ni de entrenamiento).
- Estructura y patrones: manifest → `models/` → `security/ir.model.access.csv` → `views/`.
- Cada fichero nuevo sida añadirlo en el `__manifest__.py → data:[...]` **en orden** (seguridad antes que vistas).
- Tras cada cambio de código → `docker compose restart`; luego upgrade `docker compose exec odoo odoo -d mantenimiento_id -u gestion_propiedades --stop-after-init`.
- Al desinstalar un módulo pueden quedárso tableyx físicas en PG: verificar con `\dt` y limpiarlas explícitamente si sobran (lección del 06/11).
