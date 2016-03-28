#!/usr/bin/env python
#-*- coding:utf-8 -*-

from gi.repository import Gtk

import convertidores


class VentanaPrincipal(Gtk.Window):


	def __init__(self):
		Gtk.Window.__init__(self)
		self.set_title("Convetidor 100% real no fake!")
		self.connect("delete-event", Gtk.main_quit)

		self.unidad_inicial = ""
		self.unidad_final = ""
		self.convertidor = convertidores.ConvertidorUniversal()

		self.entrada_texto = Gtk.Entry()
		self.cbt_magnitud = Gtk.ComboBoxText()
		self.cbt_unidad_inicial = Gtk.ComboBoxText()
		self.cbt_unidad_final = Gtk.ComboBoxText()

		vb = Gtk.VBox(True, 5)
		hb1 = Gtk.HBox()
		hb2 = Gtk.HBox()
		hb3 = Gtk.HBox()


		for clave in self.convertidor.convertidores:
			self.cbt_magnitud.append_text(clave)
		self.cbt_magnitud.connect("changed", self._actualizar_unidades)
		hb1.add(Gtk.Label("Escoja un magnitud para convertir: "))
		hb1.add(self.cbt_magnitud)

		self.cbt_unidad_inicial.append_text("")
		hb2.add(Gtk.Label("Convertir de: "))
		hb2.add(self.cbt_unidad_inicial)

		self.cbt_unidad_final.append_text("")
		hb3.add(Gtk.Label("Convertir a:"))
		hb3.add(self.cbt_unidad_final)

		vb.add(self.entrada_texto)
		vb.add(hb1)
		vb.add(hb2)
		vb.add(hb3)
		vb.add(BotonConvertir(self, "Convertir!"))

		self.add(vb)
		self.show_all()

	def _actualizar_unidades(self, nose_xD):
		self.cbt_unidad_final.remove_all()
		self.cbt_unidad_inicial.remove_all()
		convertidor_a_usar = self.cbt_magnitud.get_active_text()
		conv = self.convertidor.convertidores[convertidor_a_usar]
		self.actualizar_unidades_iniciales(conv)
		self.actualizar_unidades_finales(conv)

	def actualizar_unidades_iniciales(self, conv):
		for clave in conv.factores_conversion:
			self.cbt_unidad_inicial.append_text(clave)

	def actualizar_unidades_finales(self, conv):
		for clave in conv.factores_conversion:
			self.cbt_unidad_final.append_text(clave)


class BotonConvertir(Gtk.Button):

	def __init__(self, widget_padre, titulo):
		Gtk.Button.__init__(self)
		self.set_label(titulo)
		self.widget_padre = widget_padre
		self.connect("clicked", self.on_button_clicked)
		self.diccionario_convertidores = self.widget_padre.convertidor.convertidores

	def on_button_clicked(self, boton):

		string_valor = self.widget_padre.entrada_texto.get_text()
		if string_valor == "":
			self.widget_padre.entrada_texto.set_text("Que vas a convertir si dejas esto en blanco?")
			return
		try:
			valor = float(string_valor)
		except ValueError:
			self.widget_padre.entrada_texto.set_text("Señor, eso no es un número.")
			return
		unidad_inicial = self.widget_padre.cbt_unidad_inicial.get_active_text()
		unidad_final = self.widget_padre.cbt_unidad_final.get_active_text()

		convertidor_a_usar = self.widget_padre.cbt_magnitud.get_active_text()
		try:
			conv = self.diccionario_convertidores[convertidor_a_usar]
		except KeyError:
			self.widget_padre.entrada_texto.set_text("Ni siquiera has escogido una magnitud a convertir...")
			return
		resultado = conv.convertir(valor, unidad_inicial, unidad_final)
		if resultado is None:
			self.widget_padre.entrada_texto.set_text("Tienes que especificar las unidades (ambas).")
			return
		self.widget_padre.entrada_texto.set_text(str(resultado))
