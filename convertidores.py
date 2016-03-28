#!/usr/bin/env python
#-*- coding:utf-8 -*-

class ConvertidorUniversal():

	def __init__(self):
		self.convertidores = {"Presión": ConvertidorPresion(),
								"Longitud": ConvertidorLongitud(),
								"Temperatura": ConvertidorTemperatura(),
								"Masa": ConvertidorMasa(),
								"Volumen": ConvertidorVolumen(),
								"Tiempo": ConvertidorTiempo(),
								"Tamaño de datos": ConvertidorInformacion()}


class ConvertidorPadre():

	def __init__(self):
		pass

	def convertir(self, valor, unidad_inicial, unidad_final):
		try:
			resultado = valor * self.factores_conversion[unidad_inicial] / float (self.factores_conversion[unidad_final])
			return resultado
		except KeyError:
			return None


class ConvertidorPresion(ConvertidorPadre):

	def __init__(self):
		self.factores_conversion = {"pascal (Pa)": 1,
									"milimetro de mercurio (mmHg)": 133.3223684211,
									"atmósfera (atm)": 101325,
									"torricelli (Torr)": 133.3223684211,
									"hectopascal (hPa)": 100,
									"kilopascal (kPa)": 1000,
									"bar": 100000}


class ConvertidorLongitud(ConvertidorPadre):

	def __init__(self):
		self.factores_conversion = {"metro (m)": 1,
									"unidad astronómica (au)": 149597870691,
									"centimetro (cm)": 0.01,
									"decimetro (dm)": 0.1,
									"pie (ft)": 0.3048,
									"pulgada (in)": 0.0254,
									"kilometro (km)": 1000,
									"año-luz": 9460730472581000,
									"milla (mi)": 1609.344,
									"milimetro (mm)": 0.001,
									"micrometro (μm)": 1.0e-6,
									"nanometro (nm)": 1.0e-12,
									"yarda (yd)": 0.9144}


class ConvertidorMasa(ConvertidorPadre):

	def __init__(self):
		self.factores_conversion = {"kilogramo (kg)": 1,
									"gramo (g)": 0.01,
									"microgramo (μg)": 1.0e-9,
									"miligramo (mg)": 1.0e-6,
									"onza (oz)": 0.028349523125,
									"libra (lb)": 0.45359237,
									"tonelada (t)": 1000}


class ConvertidorVolumen(ConvertidorPadre):

	def __init__(self):
		self.factores_conversion = {"metro cúbico (m³)": 1,
									"centilitro (cl)": 0.00001,
									"centimetro cúbico (cc, cm³)": 0.000001,
									"decimetro cúbico (dm³)": 0.001,
									"pie cúbico (ft³, cu ft)": 0.028316846592,
									"pulgada cúbica (in³, cc in)": 0.000016387064,
									"milimetro cúbico (mm³)": 1e-9,
									"yarda cúbica (yd³)": 0.764554857984,
									"decalitro (dal)": 0.01,
									"hectolitro (hl)": 0.1,
									"kilolitro (kl)": 1,
									"litro (l)": 0.001,
									"microlitro (μl)": 1e-9,
									"mililitro (ml)": 0.000001}



class ConvertidorTiempo(ConvertidorPadre):

	def __init__(self):
		self.factores_conversion = {"segundo": 1,
									"milenio": 31536000000,
									"siglo": 3153600000,
									"década": 315360000,
									"año": 31536000,
									"mes": 2629822.96584,
									"semana": 604800,
									"día": 86400,
									"hora": 3600,
									"minuto": 60,
									"milisegundo": 0.001,
									"microsegundo": 1.0e-6,
									"nanosegundo": 1.0e-9}


class ConvertidorTemperatura(ConvertidorPadre):

	def __init__(self):
		self.factores_conversion = {"Kelvin (K)": 1,
									"Celcius (°C)": -272.15,
									"Fahrenheit (°F)": -457.87}

	def convertir(self, valor, unidad_inicial, unidad_final):
		if unidad_inicial == "Kelvin (K)":
			return self._convertirDeKelvin(valor, unidad_final)
		elif unidad_inicial == "Celcius (°C)":
			return self._convertirDeCelsius(valor, unidad_final)
		elif unidad_inicial == "Fahrenheit (°F)":
			return self._convertirDeFahrenheit(valor, unidad_final)
		else: # No debería suceder xD
			return None

	def _convertirDeKelvin(self, valor, unidad_final):
		if unidad_final == "Celcius (°C)":
			return valor - 273.15
		elif unidad_final == "Fahrenheit (°F)":
			return 1.8*(valor - 273.15) + 32
		else:
			return valor

	def _convertirDeCelsius(self, valor, unidad_final):
		if unidad_final == "Kelvin (K)":
			return valor + 273.15
		elif unidad_final == "Fahrenheit (°F)":
			return 1.8*valor + 32
		else:
			return valor

	def _convertirDeFahrenheit(self, valor, unidad_final):
		if unidad_final == "Kelvin (K)":
			return 5.0*(valor - 32) / 9.0 + 273.15
		elif unidad_final == "Celcius (°C)":
			return 5.0*(valor - 32) / 9.0
		else:
			return valor


class ConvertidorInformacion(ConvertidorPadre):

	def __init__(self):
		self.factores_conversion = {"bit (b)": 1,
									"kilobit (kb)": 10e3,
									"megabit (Mb)": 10e6,
									"gigabit (Gb)": 10e9,
									"terabit (Tb)": 10e12,
									"kibibit (kib)": 2e10,
									"mebibit (Mib)": 2e20,
									"gibibit (Gib)": 2e30,
									"tebibit (Tib)": 2e40,
									"byte (B)": 8,
									"kilobyte (kB)": 8*10e3,
									"megabyte (MB)": 8*10e6,
									"gigabyte (GB)": 8*10e9,
									"terabyte (TB)": 8*10e12,
									"kibibyte (KiB)": 8*2e10,
									"mebibyte (MiB)": 8*2e20,
									"gibibyte (GiB)": 8*2e30,
									"tebibyte (TiB)": 8*2e40}
