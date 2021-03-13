from app.forum import views
# настраиваем пути, которые будут вести к нашей странице
def setup_routes(app):
    app.router.add_get("/", views.index)
    app.router.add_view("/api/messages.list", views.ListMessageView)
    app.router.add_view("/api/messages.create", views.CreateMessageView)