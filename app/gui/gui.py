import tkinter as tk
from tkinter import ttk, messagebox
import json
import uuid

class VinotecaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Vinoteca")
        
        
        with open('vinoteca.json', 'r', encoding='utf-8') as file:
            self.data = json.load(file)
        
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True)
        
        
        self.bodegas_frame = ttk.Frame(self.notebook)
        self.cepas_frame = ttk.Frame(self.notebook)
        self.vinos_frame = ttk.Frame(self.notebook)
        
     
        self.notebook.add(self.bodegas_frame, text="Bodegas")
        self.notebook.add(self.cepas_frame, text="Cepas")
        self.notebook.add(self.vinos_frame, text="Vinos")
        
        
        self.setup_bodegas_tab()
        self.setup_cepas_tab()
        self.setup_vinos_tab()

    def setup_bodegas_tab(self):
        
        form_frame = ttk.LabelFrame(self.bodegas_frame, text='Datos de la Bodega')
        form_frame.pack(padx=10, pady=5, fill='x')

        
        ttk.Label(form_frame, text='Nombre:').grid(row=0, column=0, padx=5, pady=5)
        self.nombre_bodega_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.nombre_bodega_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text='País:').grid(row=1, column=0, padx=5, pady=5)
        self.pais_bodega_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.pais_bodega_var).grid(row=1, column=1, padx=5, pady=5)

        
        button_frame = ttk.Frame(self.bodegas_frame)
        button_frame.pack(pady=5)

        ttk.Button(button_frame, text='Agregar', command=self.agregar_bodega).pack(side='left', padx=5)
        ttk.Button(button_frame, text='Modificar', command=self.modificar_bodega).pack(side='left', padx=5)
        ttk.Button(button_frame, text='Eliminar', command=self.eliminar_bodega).pack(side='left', padx=5)

        
        columns = ('ID', 'Nombre', 'País')
        self.tabla_bodegas = ttk.Treeview(self.bodegas_frame, columns=columns, show='headings')
        
        for col in columns:
            self.tabla_bodegas.heading(col, text=col)
            self.tabla_bodegas.column(col, width=100)
        
        self.tabla_bodegas.pack(padx=10, pady=5, fill='both', expand=True)

        
        scrollbar = ttk.Scrollbar(self.bodegas_frame, orient='vertical', command=self.tabla_bodegas.yview)
        scrollbar.pack(side='right', fill='y')
        self.tabla_bodegas.configure(yscrollcommand=scrollbar.set)

        
        self.tabla_bodegas.bind('<<TreeviewSelect>>', self.seleccionar_bodega)

        
        self.actualizar_tabla_bodegas()

    def setup_cepas_tab(self):
        
        form_frame = ttk.LabelFrame(self.cepas_frame, text='Datos de la Cepa')
        form_frame.pack(padx=10, pady=5, fill='x')

        
        ttk.Label(form_frame, text='Nombre:').grid(row=0, column=0, padx=5, pady=5)
        self.nombre_cepa_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.nombre_cepa_var).grid(row=0, column=1, padx=5, pady=5)

        
        button_frame = ttk.Frame(self.cepas_frame)
        button_frame.pack(pady=5)

        ttk.Button(button_frame, text='Agregar', command=self.agregar_cepa).pack(side='left', padx=5)
        ttk.Button(button_frame, text='Modificar', command=self.modificar_cepa).pack(side='left', padx=5)
        ttk.Button(button_frame, text='Eliminar', command=self.eliminar_cepa).pack(side='left', padx=5)

        
        columns = ('ID', 'Nombre')
        self.tabla_cepas = ttk.Treeview(self.cepas_frame, columns=columns, show='headings')
        
        for col in columns:
            self.tabla_cepas.heading(col, text=col)
            self.tabla_cepas.column(col, width=100)
        
        self.tabla_cepas.pack(padx=10, pady=5, fill='both', expand=True)

        
        scrollbar = ttk.Scrollbar(self.cepas_frame, orient='vertical', command=self.tabla_cepas.yview)
        scrollbar.pack(side='right', fill='y')
        self.tabla_cepas.configure(yscrollcommand=scrollbar.set)

        
        self.tabla_cepas.bind('<<TreeviewSelect>>', self.seleccionar_cepa)

        
        self.actualizar_tabla_cepas()

    def setup_vinos_tab(self):
        
        form_frame = ttk.LabelFrame(self.vinos_frame, text='Datos del Vino')
        form_frame.pack(padx=10, pady=5, fill='x')

        
        ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.vino_nombre = ttk.Entry(form_frame)
        self.vino_nombre.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Partidas (años):").grid(row=1, column=0, padx=5, pady=5)
        self.vino_partidas = ttk.Entry(form_frame)
        self.vino_partidas.grid(row=1, column=1, padx=5, pady=5)

        
        ttk.Label(form_frame, text="Bodega:").grid(row=2, column=0, padx=5, pady=5)
        self.bodega_combo = ttk.Combobox(form_frame)
        self.bodega_combo.grid(row=2, column=1, padx=5, pady=5)

        
        ttk.Label(form_frame, text="Cepa:").grid(row=3, column=0, padx=5, pady=5)
        self.cepa_combo = ttk.Combobox(form_frame)
        self.cepa_combo.grid(row=3, column=1, padx=5, pady=5)

        
        button_frame = ttk.Frame(self.vinos_frame)
        button_frame.pack(pady=5)

        ttk.Button(button_frame, text='Agregar', command=self.agregar_vino).pack(side='left', padx=5)
        ttk.Button(button_frame, text='Modificar', command=self.modificar_vino).pack(side='left', padx=5)
        ttk.Button(button_frame, text='Eliminar', command=self.eliminar_vino).pack(side='left', padx=5)

        
        columns = ('ID', 'Nombre', 'Partidas', 'Bodega', 'Cepas')
        self.tabla_vinos = ttk.Treeview(self.vinos_frame, columns=columns, show='headings')
        
        for col in columns:
            self.tabla_vinos.heading(col, text=col)
            self.tabla_vinos.column(col, width=100)
        
        self.tabla_vinos.pack(padx=10, pady=5, fill='both', expand=True)

        
        scrollbar = ttk.Scrollbar(self.vinos_frame, orient='vertical', command=self.tabla_vinos.yview)
        scrollbar.pack(side='right', fill='y')
        self.tabla_vinos.configure(yscrollcommand=scrollbar.set)

        
        self.tabla_vinos.bind('<<TreeviewSelect>>', self.seleccionar_vino)

        
        self.actualizar_comboboxes()
        
        
        self.actualizar_tabla_vinos()

    def actualizar_comboboxes(self):
        """Actualiza los comboboxes de bodegas y cepas"""
        self.bodega_combo['values'] = [bodega['nombre'] for bodega in self.data['bodegas']]
        self.cepa_combo['values'] = [cepa['nombre'] for cepa in self.data['cepas']]

    
    def agregar_bodega(self):
        nombre = self.nombre_bodega_var.get()
        pais = self.pais_bodega_var.get()
        
        if nombre and pais:
            nueva_bodega = {
                'id': str(uuid.uuid4()),
                'nombre': nombre,
                'pais': pais
            }
            
            self.data['bodegas'].append(nueva_bodega)
            self.guardar_json()
            self.actualizar_tabla_bodegas()
            self.actualizar_comboboxes()
            self.limpiar_campos_bodega()
            messagebox.showinfo("Éxito", "Bodega agregada correctamente")
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos")

    def modificar_bodega(self):
        seleccion = self.tabla_bodegas.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione una bodega")
            return

        nombre = self.nombre_bodega_var.get()
        pais = self.pais_bodega_var.get()

        if nombre and pais:
            id_bodega = self.tabla_bodegas.item(seleccion[0])['values'][0]
            for bodega in self.data['bodegas']:
                if bodega['id'] == id_bodega:
                    bodega['nombre'] = nombre
                    bodega['pais'] = pais
                    break

            self.guardar_json()
            self.actualizar_tabla_bodegas()
            self.actualizar_comboboxes()
            self.limpiar_campos_bodega()
            messagebox.showinfo("Éxito", "Bodega modificada correctamente")
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos")

    def eliminar_bodega(self):
        seleccion = self.tabla_bodegas.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione una bodega")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar esta bodega?"):
            id_bodega = self.tabla_bodegas.item(seleccion[0])['values'][0]
            self.data['bodegas'] = [b for b in self.data['bodegas'] if b['id'] != id_bodega]
            self.guardar_json()
            self.actualizar_tabla_bodegas()
            self.actualizar_comboboxes()
            self.limpiar_campos_bodega()
            messagebox.showinfo("Éxito", "Bodega eliminada correctamente")

    def actualizar_tabla_bodegas(self):
        for item in self.tabla_bodegas.get_children():
            self.tabla_bodegas.delete(item)
        
        for bodega in self.data['bodegas']:
            self.tabla_bodegas.insert('', 'end', values=(
                bodega['id'],
                bodega['nombre'],
                bodega.get('pais', 'No especificado')
            ))

    def seleccionar_bodega(self, event):
        seleccion = self.tabla_bodegas.selection()
        if seleccion:
            valores = self.tabla_bodegas.item(seleccion[0])['values']
            self.nombre_bodega_var.set(valores[1])
            self.pais_bodega_var.set(valores[2])

    def limpiar_campos_bodega(self):
        self.nombre_bodega_var.set('')
        self.pais_bodega_var.set('')

    
    def agregar_cepa(self):
        nombre = self.nombre_cepa_var.get()
        
        if nombre:
            nueva_cepa = {
                'id': str(uuid.uuid4()),
                'nombre': nombre
            }
            
            self.data['cepas'].append(nueva_cepa)
            self.guardar_json()
            self.actualizar_tabla_cepas()
            self.actualizar_comboboxes()
            self.limpiar_campos_cepa()
            messagebox.showinfo("Éxito", "Cepa agregada correctamente")
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos")

    def modificar_cepa(self):
        seleccion = self.tabla_cepas.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione una cepa")
            return

        nombre = self.nombre_cepa_var.get()

        if nombre:
            id_cepa = self.tabla_cepas.item(seleccion[0])['values'][0]
            for cepa in self.data['cepas']:
                if cepa['id'] == id_cepa:
                    cepa['nombre'] = nombre
                    break

            self.guardar_json()
            self.actualizar_tabla_cepas()
            self.actualizar_comboboxes()
            self.limpiar_campos_cepa()
            messagebox.showinfo("Éxito", "Cepa modificada correctamente")
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos")

    def eliminar_cepa(self):
        seleccion = self.tabla_cepas.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione una cepa")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar esta cepa?"):
            id_cepa = self.tabla_cepas.item(seleccion[0])['values'][0]
            self.data['cepas'] = [c for c in self.data['cepas'] if c['id'] != id_cepa]
            self.guardar_json()
            self.actualizar_tabla_cepas()
            self.actualizar_comboboxes()
            self.limpiar_campos_cepa()
            messagebox.showinfo("Éxito", "Cepa eliminada correctamente")

    def actualizar_tabla_cepas(self):
        for item in self.tabla_cepas.get_children():
            self.tabla_cepas.delete(item)
        
        for cepa in self.data['cepas']:
            self.tabla_cepas.insert('', 'end', values=(
                cepa['id'],
                cepa['nombre']
            ))

    def seleccionar_cepa(self, event):
        seleccion = self.tabla_cepas.selection()
        if seleccion:
            valores = self.tabla_cepas.item(seleccion[0])['values']
            self.nombre_cepa_var.set(valores[1])

    def limpiar_campos_cepa(self):
        self.nombre_cepa_var.set('')

    
    def agregar_vino(self):
        nombre = self.vino_nombre.get()
        partidas_str = self.vino_partidas.get()
        bodega_nombre = self.bodega_combo.get()
        cepa_nombre = self.cepa_combo.get()

        if nombre and partidas_str and bodega_nombre and cepa_nombre:
            try:
                partidas = [int(año.strip()) for año in partidas_str.split(',')]
                
                
                bodega_id = next(b['id'] for b in self.data['bodegas'] if b['nombre'] == bodega_nombre)
                
                
                cepa_id = next(c['id'] for c in self.data['cepas'] if c['nombre'] == cepa_nombre)

                nuevo_vino = {
                    'id': str(uuid.uuid4()),
                    'nombre': nombre,
                    'bodega': bodega_id,
                    'cepas': [cepa_id],
                    'partidas': partidas
                }
                
                self.data['vinos'].append(nuevo_vino)
                self.guardar_json()
                self.actualizar_tabla_vinos()
                self.limpiar_campos_vino()
                messagebox.showinfo("Éxito", "Vino agregado correctamente")
            except ValueError:
                messagebox.showerror("Error", "Las partidas deben ser años válidos separados por comas")
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos")

    def modificar_vino(self):
        seleccion = self.tabla_vinos.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione un vino")
            return

        nombre = self.vino_nombre.get()
        partidas_str = self.vino_partidas.get()
        bodega_nombre = self.bodega_combo.get()
        cepa_nombre = self.cepa_combo.get()

        if nombre and partidas_str and bodega_nombre and cepa_nombre:
            try:
                partidas = [int(año.strip()) for año in partidas_str.split(',')]
                
                
                bodega_id = next(b['id'] for b in self.data['bodegas'] if b['nombre'] == bodega_nombre)
                
                
                cepa_id = next(c['id'] for c in self.data['cepas'] if c['nombre'] == cepa_nombre)

                id_vino = self.tabla_vinos.item(seleccion[0])['values'][0]
                for vino in self.data['vinos']:
                    if vino['id'] == id_vino:
                        vino['nombre'] = nombre
                        vino['bodega'] = bodega_id
                        vino['cepas'] = [cepa_id]
                        vino['partidas'] = partidas
                        break

                self.guardar_json()
                self.actualizar_tabla_vinos()
                self.limpiar_campos_vino()
                messagebox.showinfo("Éxito", "Vino modificado correctamente")
            except ValueError:
                messagebox.showerror("Error", "Las partidas deben ser años válidos separados por comas")
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos")

    def eliminar_vino(self):
        seleccion = self.tabla_vinos.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione un vino")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este vino?"):
            id_vino = self.tabla_vinos.item(seleccion[0])['values'][0]
            self.data['vinos'] = [v for v in self.data['vinos'] if v['id'] != id_vino]
            self.guardar_json()
            self.actualizar_tabla_vinos()
            self.limpiar_campos_vino()
            messagebox.showinfo("Éxito", "Vino eliminado correctamente")

    def actualizar_tabla_vinos(self):
        for item in self.tabla_vinos.get_children():
            self.tabla_vinos.delete(item)
        
        for vino in self.data['vinos']:
            
            bodega_nombre = next(b['nombre'] for b in self.data['bodegas'] if b['id'] == vino['bodega'])
            
            
            cepas_nombres = [c['nombre'] for c in self.data['cepas'] if c['id'] in vino['cepas']]
            
            self.tabla_vinos.insert('', 'end', values=(
                vino['id'],
                vino['nombre'],
                ', '.join(map(str, vino['partidas'])),
                bodega_nombre,
                ', '.join(cepas_nombres)
            ))

    def seleccionar_vino(self, event):
        seleccion = self.tabla_vinos.selection()
        if seleccion:
            valores = self.tabla_vinos.item(seleccion[0])['values']
            self.vino_nombre.delete(0, tk.END)
            self.vino_nombre.insert(0, valores[1])
            self.vino_partidas.delete(0, tk.END)
            self.vino_partidas.insert(0, valores[2])
            self.bodega_combo.set(valores[3])
            self.cepa_combo.set(valores[4].split(', ')[0])  

    def limpiar_campos_vino(self):
        self.vino_nombre.delete(0, tk.END)
        self.vino_partidas.delete(0, tk.END)
        self.bodega_combo.set('')
        self.cepa_combo.set('')

    def guardar_json(self):
        """Guarda los datos en el archivo JSON"""
        with open('vinoteca.json', 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=2, ensure_ascii=False)