#!/bin/bash

# Este servidor local, es para la descarga del archivo de 1 byte
qterminal -e "python -m http.server 4445" &

# Esperar un momento antes de abrir la segunda ventana
sleep 1

# Este servidor local es para el portal de descargas del chrome falso o la web que elijas
qterminal -e "cd downloadserver; python -m http.server 4446" &
