def aplicar_aumento(precio):
	aumento = 5
	precio_aumentado = 0
	precio_final_aumentado = 0
	precio_aumentado = (precio * 5) / 100
	precio_final_aumentado = precio + precio_aumentado
	print(f"El precio final con aumento es: {precio_final_aumentado}")


aplicar_aumento(100)