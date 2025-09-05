"""
Middleware para fallback automático MySQL -> SQLite
Detecta erros de conexão MySQL e troca automaticamente para SQLite
"""
import logging
from django.db import connections
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

logger = logging.getLogger(__name__)

class DatabaseFallbackMiddleware:
    """
    Middleware que detecta erros de conexão MySQL e troca para SQLite automaticamente
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        self.fallback_activated = False
        
    def __call__(self, request):
        # Verifica se o fallback já foi ativado
        if not self.fallback_activated:
            self._check_mysql_connection()
        
        response = self.get_response(request)
        return response
    
    def _check_mysql_connection(self):
        """
        Verifica se a conexão MySQL está funcionando
        Se não estiver, ativa o fallback para SQLite
        """
        try:
            # Tenta conectar no MySQL
            connection = connections['default']
            connection.ensure_connection()
            logger.info("Conexão MySQL estabelecida com sucesso")
            
        except Exception as e:
            logger.warning(f"Erro na conexão MySQL: {e}")
            logger.info("Ativando fallback para SQLite...")
            
            # Ativa o fallback para SQLite
            self._activate_sqlite_fallback()
    
    def _activate_sqlite_fallback(self):
        """
        Ativa o fallback para SQLite alterando a configuração do banco
        """
        try:
            # Altera a configuração do banco para SQLite
            settings.DATABASES['default'] = settings.DATABASES['sqlite_fallback']
            
            # Força a recriação da conexão
            connections['default'].close()
            del connections['default']
            
            # Cria nova conexão com SQLite
            from django.db import connection
            connection.ensure_connection()
            
            self.fallback_activated = True
            logger.info("Fallback para SQLite ativado com sucesso")
            
            # Executa as migrações no SQLite se necessário
            self._run_migrations_if_needed()
            
        except Exception as e:
            logger.error(f"Erro ao ativar fallback SQLite: {e}")
    
    def _run_migrations_if_needed(self):
        """
        Executa as migrações no SQLite se necessário
        """
        try:
            from django.core.management import execute_from_command_line
            from django.core.management.commands.migrate import Command as MigrateCommand
            
            # Verifica se as tabelas existem
            from django.db import connection
            with connection.cursor() as cursor:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='django_migrations'")
                if not cursor.fetchone():
                    logger.info("Executando migrações no SQLite...")
                    # Executa as migrações
                    migrate_command = MigrateCommand()
                    migrate_command.handle(verbosity=0)
                    logger.info("Migrações executadas com sucesso no SQLite")
                    
        except Exception as e:
            logger.error(f"Erro ao executar migrações no SQLite: {e}")
