# Samuel Nicola NC 0106
# Imagen pavo NL 44
import cv2

# Cargar la imagen
imagen = cv2.imread("imagenes/pavo.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(
    imagen,
    5
)

# Mostrar imágenes
cv2.imshow("Imagen original pavo 0106", imagen)
cv2.imshow("Imagen filtrada pavo 0106", imagen_filtrada)

# Guardar resultado
cv2.imwrite(
    "resultados/paisaje_mediana.jpg",
    imagen_filtrada
)

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print("resultados/paisaje_mediana.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print(" PROGRAMA REALIZADO POR Samuel Nicola 0106")