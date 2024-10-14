

# Calculadora Vectorial en Python

¡Bienvenido a la **Calculadora Vectorial**! 📐🚀

Esta aplicación permite realizar operaciones básicas y avanzadas con vectores en Python, incluyendo suma, resta, producto escalar, magnitud, normalización y más.

## Características

- Suma y resta de vectores.
- Producto escalar y vectorial.
- Cálculo de la magnitud de un vector.
- Normalización de vectores.
- Determinación del ángulo entre dos vectores.
- Proyección de un vector sobre otro.

## Instalación

Para utilizar la calculadora vectorial, primero asegúrate de tener Python instalado en tu sistema. Luego, clona este repositorio y navega al directorio del proyecto:

```bash
git clone https://github.com/https://github.com/Jona163/Calculadora_Vectorial.git
cd Calculadora_Vectorial
```

Si el proyecto tiene dependencias adicionales, instálalas utilizando:

```bash
pip install -r requirements.txt
```

## Uso

Puedes ejecutar la calculadora desde la línea de comandos:

```bash
python Calculadora_Vectorial.py
```

### Ejemplos de uso

Aquí hay algunos ejemplos de cómo usar la calculadora en el código:

```python
from calculadora_vectorial import Vector

# Definir vectores
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

# Sumar vectores
suma = v1 + v2
print(f"Suma: {suma}")

# Calcular el producto escalar
producto_escalar = v1.dot(v2)
print(f"Producto escalar: {producto_escalar}")

# Calcular la magnitud
magnitud_v1 = v1.magnitude()
print(f"Magnitud de v1: {magnitud_v1}")
```

## Pruebas

Las pruebas unitarias están disponibles para verificar la funcionalidad de la calculadora. Para ejecutar las pruebas:

```bash
python -m unittest discover tests
```

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar la calculadora vectorial, sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin nueva-funcionalidad`).
5. Abre un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

## Contacto

Para más información o sugerencias, no dudes en contactar a **Jonathan Hernández**.

---
