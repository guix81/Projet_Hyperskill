from abc import ABC

class Shell(ABC):
    list_user = []  # une liste de liste des données utilisateur sous forme de [name, pass, status, autority] venant du fichier data_user.csv
    list_username = []
    list_obj_user = []
    list_posts = []
    list_obj_post = []
    list_threads = []
    list_obj_thread = []
    head_user = ["name", "mdp", "status", "id", "autority"]
    head_thread = ["title_thread", "username_thread", "date_trhead", "id", "liste_id_post"]
    head_post = ["content_post", "username_post", "date_post", 'id']
    path_data = ""