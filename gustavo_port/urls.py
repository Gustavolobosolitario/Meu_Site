"""
URL configuration for gustavo_port project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gu_port import views
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='index'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
]


# Se você estiver recebendo erros relacionados ao diretório de arquivos estáticos (STATICFILES_DIRS) no Django, pode ser necessário verificar alguns pontos. Aqui estão algumas soluções comuns para resolver esses erros:

# Certifique-se de que o diretório estático está corretamente configurado:
# Verifique se você definiu corretamente o STATICFILES_DIRS no arquivo settings.py do seu projeto. Ele deve apontar para o diretório onde você criou os diretórios css e js dentro do diretório portfolio/static/. Por exemplo:
# python
# Copy code
# settings.py


# Verifique a estrutura do projeto:
# Verifique se a estrutura do projeto está correta e se os diretórios e arquivos estão nos locais corretos. A estrutura deve ser semelhante à que mencionei anteriormente.

# Reinicie o servidor:
# Após fazer alterações no arquivo settings.py, é importante reiniciar o servidor de desenvolvimento para que as alterações entrem em vigor. Pare o servidor (pressionando CTRL-C no terminal) e execute novamente python manage.py runserver.

# Certifique-se de que o servidor está servindo arquivos estáticos:
# O Django não serve automaticamente arquivos estáticos durante o desenvolvimento. Para servir arquivos estáticos, adicione o seguinte código ao arquivo urls.py do projeto:

# python
# Copy code
# urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Suas URLs aqui
]

# Adicione a seguinte linha para servir arquivos estáticos durante o desenvolvimento
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
