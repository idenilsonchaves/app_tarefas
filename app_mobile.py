from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.utils import platform
from kivy.clock import Clock
from datetime import datetime
import sqlite3
import os

# Configuração da janela
Window.clearcolor = (0.9, 0.9, 0.9, 1)  # Cor de fundo cinza claro

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Título
        title = Label(
            text='TaskMaster',
            font_size=40,
            size_hint_y=None,
            height=100
        )
        layout.add_widget(title)
        
        # Campo de email
        self.email_input = TextInput(
            hint_text='Email',
            multiline=False,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.email_input)
        
        # Campo de senha
        self.password_input = TextInput(
            hint_text='Senha',
            password=True,
            multiline=False,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.password_input)
        
        # Botão de login
        login_button = Button(
            text='Entrar',
            size_hint_y=None,
            height=50,
            background_color=(0.2, 0.6, 1, 1)
        )
        login_button.bind(on_press=self.login)
        layout.add_widget(login_button)
        
        self.add_widget(layout)
    
    def login(self, instance):
        email = self.email_input.text
        password = self.password_input.text
        
        # Aqui você implementaria a lógica de autenticação
        # Por enquanto, vamos apenas mudar para a tela principal
        self.manager.current = 'dashboard'

class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Cabeçalho
        header = BoxLayout(size_hint_y=None, height=50)
        title = Label(text='Minhas Tarefas', font_size=24)
        header.add_widget(title)
        
        # Botão de nova tarefa
        new_task_btn = Button(
            text='Nova Tarefa',
            size_hint_x=None,
            width=120,
            background_color=(0.2, 0.6, 1, 1)
        )
        new_task_btn.bind(on_press=self.show_new_task)
        header.add_widget(new_task_btn)
        
        layout.add_widget(header)
        
        # Lista de tarefas
        self.tasks_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.tasks_layout.bind(minimum_height=self.tasks_layout.setter('height'))
        
        scroll = ScrollView()
        scroll.add_widget(self.tasks_layout)
        layout.add_widget(scroll)
        
        self.add_widget(layout)
    
    def show_new_task(self, instance):
        self.manager.current = 'new_task'
    
    def on_enter(self):
        self.load_tasks()
    
    def load_tasks(self):
        self.tasks_layout.clear_widgets()
        # Aqui você carregaria as tarefas do banco de dados
        # Por enquanto, vamos adicionar algumas tarefas de exemplo
        tasks = [
            {'title': 'Reunião de Equipe', 'description': 'Discussão do projeto', 'due_date': '2024-03-20'},
            {'title': 'Relatório Mensal', 'description': 'Preparar relatório de vendas', 'due_date': '2024-03-25'}
        ]
        
        for task in tasks:
            task_card = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                height=150,
                padding=10,
                spacing=5
            )
            
            title = Label(
                text=task['title'],
                font_size=18,
                size_hint_y=None,
                height=30
            )
            task_card.add_widget(title)
            
            description = Label(
                text=task['description'],
                size_hint_y=None,
                height=30
            )
            task_card.add_widget(description)
            
            due_date = Label(
                text=f'Vencimento: {task["due_date"]}',
                size_hint_y=None,
                height=30
            )
            task_card.add_widget(due_date)
            
            buttons = BoxLayout(size_hint_y=None, height=40, spacing=10)
            
            complete_btn = Button(
                text='Concluir',
                background_color=(0.2, 0.8, 0.2, 1)
            )
            buttons.add_widget(complete_btn)
            
            delete_btn = Button(
                text='Excluir',
                background_color=(0.8, 0.2, 0.2, 1)
            )
            buttons.add_widget(delete_btn)
            
            task_card.add_widget(buttons)
            self.tasks_layout.add_widget(task_card)

class NewTaskScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Título
        title = Label(
            text='Nova Tarefa',
            font_size=24,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(title)
        
        # Campos do formulário
        self.title_input = TextInput(
            hint_text='Título',
            multiline=False,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.title_input)
        
        self.description_input = TextInput(
            hint_text='Descrição',
            multiline=True,
            size_hint_y=None,
            height=100
        )
        layout.add_widget(self.description_input)
        
        self.due_date_input = TextInput(
            hint_text='Data de Vencimento (YYYY-MM-DD)',
            multiline=False,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.due_date_input)
        
        # Botões
        buttons = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        save_btn = Button(
            text='Salvar',
            background_color=(0.2, 0.6, 1, 1)
        )
        save_btn.bind(on_press=self.save_task)
        buttons.add_widget(save_btn)
        
        cancel_btn = Button(
            text='Cancelar',
            background_color=(0.8, 0.2, 0.2, 1)
        )
        cancel_btn.bind(on_press=self.cancel)
        buttons.add_widget(cancel_btn)
        
        layout.add_widget(buttons)
        self.add_widget(layout)
    
    def save_task(self, instance):
        # Aqui você implementaria a lógica para salvar a tarefa
        self.manager.current = 'dashboard'
    
    def cancel(self, instance):
        self.manager.current = 'dashboard'

class TaskMasterApp(App):
    def build(self):
        # Configuração do gerenciador de telas
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(NewTaskScreen(name='new_task'))
        return sm

if __name__ == '__main__':
    TaskMasterApp().run() 