class ProgrammingLanguage:
    """
    Classe représentant un langage de programmation.
    
    Attributs :
    ----------
    name : str
        Le nom du langage de programmation.
    year_created : int
        L'année de création du langage.
    paradigms : list
        Une liste des paradigmes de programmation supportés par le langage.
    """

    def __init__(self, name, year_created, paradigms):
        """
        Initialise un objet ProgrammingLanguage avec un nom, une année de création et des paradigmes.
        
        Paramètres :
        -----------
        name : str
            Le nom du langage de programmation.
        year_created : int
            L'année de création du langage.
        paradigms : list
            Une liste des paradigmes de programmation supportés par le langage.
        """
        self.name = name
        self.year_created = year_created
        self.paradigms = paradigms

    def add_paradigm(self, paradigm):
        """
        Ajoute un nouveau paradigme à la liste des paradigmes du langage.
        
        Paramètres :
        -----------
        paradigm : str
            Le paradigme à ajouter.
        """
        if paradigm not in self.paradigms:
            self.paradigms.append(paradigm)

    def display_info(self):
        """
        Affiche les informations sur le langage de programmation.
        """
        print(f"Langage : {self.name}")
        print(f"Année de création : {self.year_created}")
        print(f"Paradigmes : {', '.join(self.paradigms)}")


# Exemple d'utilisation
python = ProgrammingLanguage("Python", 1991, ["Objet", "Impératif", "Fonctionnel"])
python.display_info()

# Ajouter un nouveau paradigme
python.add_paradigm("Orienté prototype")
python.display_info()