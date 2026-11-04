#!/bin/bash
dnf install -y nodejs
mkdir -p /opt/api

cat > /opt/api/server.js <<'FIN'
const http = require('http');
const notas = [4.5, 3.5, 2.5, 4.0];

function calcularPromedio(arrayNotas) {
    let sumaTotal = 0;
    for (let i = 0; i < arrayNotas.length; i++) {
        sumaTotal = sumaTotal + arrayNotas[i];
    }
    return sumaTotal / arrayNotas.length;
}

function responder(res, codigo, datos) {
    res.writeHead(codigo, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify(datos));
}

const servidor = http.createServer((req, res) => {
    if (req.url === '/salud') {
        responder(res, 200, { estado: 'ok' });
        return;
    }
    if (req.url === '/equipo') {
        responder(res, 200, { 
            equipo: 'Equipo 25493',
            integrantes: ['Eissan Charris'] 
        });
        return;
    }
    if (req.url === '/notas') {
        const promedio = calcularPromedio(notas);
        responder(res, 200, { promedio: promedio, aprobado: promedio >= 3.0 });
        return;
    }
    responder(res, 404, { error: 'Ruta no encontrada' });
});

servidor.listen(80);
FIN

cat > /etc/systemd/system/api.service <<'FIN'
[Unit]
Description=API del equipo
After=network.target

[Service]
ExecStart=/usr/bin/node /opt/api/server.js
Restart=always

[Install]
WantedBy=multi-user.target
FIN

systemctl daemon-reload
systemctl enable --now api