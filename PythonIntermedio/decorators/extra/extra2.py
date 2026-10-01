user_logged_in = True

def requires_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise PermissionError("Usuario no autenticado")
        return func(*args,**kwargs)
    return wrapper

@requires_login
def view_profile():
    print("Mostrando perfil del usuario")

view_profile()