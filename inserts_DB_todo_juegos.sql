describe REST_API_CATEGORIA

INSERT INTO REST_API_CATEGORIA (nombre) VALUES ('Terror');
INSERT INTO REST_API_CATEGORIA (nombre) VALUES ('Deportes');
INSERT INTO REST_API_CATEGORIA (nombre) VALUES ('Acción');
INSERT INTO REST_API_CATEGORIA (nombre) VALUES ('Supervivencia');
INSERT INTO REST_API_CATEGORIA (nombre) VALUES ('Carreras');
INSERT INTO REST_API_CATEGORIA (nombre) VALUES ('Mundo Abierto');

select * from REST_API_CATEGORIA

describe REST_API_JUEGO

TRUNCATE TABLE REST_API_JUEGO;


INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  6, 'Minecraft', 30990, 15000,
  'Crea todo lo que puedas imaginar, descubre los misterios espeluznantes y sobrevive la noche. Explora, construye y da forma bloque a bloque a tu mundo infinito.',
  'img/mineban.jpg'
);

INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  4, 'ARK Ascended', 42990, 37000,
  '¡Ark se reinventa desde cero en esta próxima generación, con gráficos y jugabilidad mejorada! Domina la cadena alimentaria, domestica criaturas colosales y sitúate en la cima de la cadena alimentaria. ¡Tu nuevo mundo te espera!',
  'img/ark2.jpg'
);

INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  3, 'Monster Hunter Wild', 59990, 49990,
  'Siente la fuerza desbocada, salvaje e imparable de las criaturas más temibles. Cumple tu deber como cazador rastreando monstruos en entornos que se transforman drásticamente de un momento a otro. Esta es una historia de monstruos y humanos, con dificultades para coexistir en armonía en un mundo de dualidades. Cumple tu deber como cazador rastreando las pistas entre la gente de las Tierras Prohibidas y las zonas que habitan.',
  'img/mh.jpg'
);

INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  5, 'Need for Speed Most Wanted', 29990, 19990,
  'Need for Speed: Most Wanted (2012), desarrollado por Criterion Games, te enfrenta a intensas persecuciones policiales y carreras de alto octanaje.',
  'img/nfsmw.jpg'
);

INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  4, 'The Forest', 24990, 14990,
  'The Forest para PC es un juego de acción y supervivencia: tras un accidente aéreo, construyes refugios, cazas recursos y, por supuesto, te defiendes de los caníbales.',
  'img/forest.jpg'
);

INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  5, 'F1®24', 35990, 24990,
  'Sé una de las 20 personas al volante con EA SPORTS F1®24. Domina los circuitos oficiales, gestiona tu estrategia y demuestra que tienes lo necesario para ganar en nuevos modos y experiencias.',
  'img/f21.jpg'
);

INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  2, 'FIFA 2022', 29990, 19990,
  'Con la integración de la captura avanzada de movimientos y gráficos realistas, FIFA 2022 ofrece una jugabilidad más realista, eficaz y fluida en la historia de FIFA.',
  'img/futb.jpg'
);

INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  2, 'NBA 2K24', 39990, 29990,
  'Experimenta la cultura del baloncesto en NBA 2K24: partidos realistas, plantillas actualizadas de la NBA y WNBA en JUGAR YA. Precio 30.000 CLP.',
  'img/nba.jpg'
);

INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  3, 'Split Fiction', 39990, 29990,
  'Disfruta de una aventura alucinante que traslada tu mente entre dos realidades. Resuelve enigmas y descubre fragmentos de una máquina diseñada para robar sus ideas creativas.',
  'img/sf.jpg'
);

INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  2, 'Captain Tsubasa', 34990, 24990,
  'Captain Tsubasa: Rise of New Champions revive la épica aventura futbolística de Oliver y sus amigos con jugadas espectaculares. Incluye el modo “Nuevo Héroe”, un modo de historial original en este juego.',
  'img/tsubasa.jpg'
);

INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  1, 'Outlast', 19990, 9990,
  'Outlast es un videojuego de terror y supervivencia en un manicomio abandonado. Investiga pasillos oscuros, graba evidencia y escapa de las atrocidades llevadas a cabo con los pacientes.',
  'img/ol.jpg'
);

INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  4, 'Rust', 29990, 19990,
  'Rust para PC es un juego independiente de supervivencia multijugador. Sobrevive recolectando recursos, construyendo bases y defendiendo tus elementos poco a poco hasta ampliar tus recursos.',
  'img/rust.jpg'
);

INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  3, 'Helldivers II', 29990, 19990,
  'Helldivers es un juego de disparos de perspectiva cenital cooperativo. Lucha en misiones intergalácticas, coordina con tu escuadrón y ten cuidado con el fuego amigo: esto conlleva sus propios riesgos.',
  'img/hd.jpg'
);

INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  1, 'Resident Evil 6', 29990, 19990,
  'Resident Evil 6, con su combinación de acción y terror, presenta campañas interconectadas con personajes emblemáticos de la saga. Comparte más de 12 horas de horror y acción intensa, más que cualquier otra entrega de la saga Resident Evil.',
  'img/rev6.jpg'
);

INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  1, 'Resident Evil Village', 34990, 24990,
  '¿Qué es Resident Evil Village? Vive el horror de supervivencia como nunca antes en el octavo episodio principal de la saga Resident Evil. Ambientado unos pocos años después de los sucesos de RE7, explora una nueva ubicación y reconstruye tu nueva vida… hasta que la tragedia vuelva a caer encima.',
  'img/rv.jpg'
);

INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  3, 'Elden Ring', 49990, 39990,
  'Álzate, Sinluz, y que la gracia te guíe para ascender y encumbrarte como señor del Círculo en las Tierras Intermedias. En las Tierras Intermedias gobernadas por el Círculo de Elden, origen del Árbol Áureo, todo ha sido destruido. Los descendientes de Márika, semidioses corrompidos por la Devastación, buscan restaurar el poder perdido.',
  'img/er.jpg'
);

INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  3, 'GTA V', 29990, 14990,
  'Experimenta Grand Theft Auto V, el juego de mundo abierto más exitoso. Tres protagonistas cuyas vidas se entrelazan en Los Santos, donde no puedes confiar en nadie; mucho menos unos en otros.',
  'img/gta.jpg'
);

INSERT INTO REST_API_JUEGO (
  categoria_id, nombre, precio_original, precio_oferta, descripcion, ruta_imagen
) VALUES (
  5, 'Need for Speed Heat', 29990, 19990,
  'En Need for Speed Heat, los límites de la ley están abiertos. Compite de día en carreras oficiales para aumentar tu REP y, de noche, arríesgalo todo en eventos clandestinos por la gloria.',
  'img/ndfs.jpg'
);

commit;

select * from REST_API_JUEGO
