import tkinter as tk

produits = {
    "Pizza": 40,
    "Tacos": 49,
    "Sandwich": 30,
    "Burger": 32,
    "Frites": 15,
    "Nuggets": 35,
    "soda": 15,
    "Limonade": 18,
}

class snackApp:
    def __init__(self, fenetre_principale):
        self.fenetre = fenetre_principale
        self.fenetre.title("SnackApp")
        self.fenetre.configure(bg="#faedcd")
        self.commande = {produit: 0 for produit in produits}
        self.affichages_quantites = {}  
        self.afficher_interface()

    def afficher_interface(self):
        tk.Label(
            self.fenetre,
            text="Bienvenue dans notre snack !",
            font=("Georgia", 24, "bold"),
            bg="#d8e2dc",
            fg="black",
            padx=10,
            pady=10,
        ).pack(fill=tk.X)

        cadre_principal = tk.Frame(self.fenetre, bg="#ffffff")
        cadre_principal.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        for produit, prix in produits.items():
            ligne = tk.Frame(cadre_principal, bg="#ffffff", pady=10)
            ligne.pack(fill=tk.X)

            tk.Label(
                ligne,
                text=f"{produit} - {prix} dhs",
                font=("Arial", 14),
                bg="#ffffff",
            ).pack(side=tk.LEFT, padx=20)

            cadre_boutons = tk.Frame(ligne, bg="#ffffff")
            cadre_boutons.pack(side=tk.RIGHT, padx=10)

            btn_moins = tk.Button(
                cadre_boutons,
                text="-",
                bg="#f07167",
                fg="white",
                font=("Arial", 14, "bold"),
                width=4,
                height=1,
                command=self.reduire_quantite(produit),
            )
            btn_moins.grid(row=0, column=0, padx=5)

            affichage_quantite = tk.Label(  
                cadre_boutons,
                text="0",
                font=("Arial", 14),
                bg="#f9f9f9",
                width=5,
                height=1,
            )
            affichage_quantite.grid(row=0, column=1, padx=5)
            self.affichages_quantites[produit] = affichage_quantite

            btn_plus = tk.Button(
                cadre_boutons,
                text="+",
                bg="#99d98c",
                fg="white",
                font=("Arial", 14, "bold"),
                width=4,
                height=1,
                command=self.augmenter_quantite(produit),
            )
            btn_plus.grid(row=0, column=2, padx=5)

        btn_reinitialiser = tk.Button(
            self.fenetre,
            text="Réinitialiser",
            bg="#e74c3c",
            fg="white",
            font=("Arial", 16, "bold"),
            width=12,
            command=self.reinitialiser,
        )
        btn_reinitialiser.pack(side=tk.BOTTOM, pady=15)

        self.affichage_total = tk.Label(  
            self.fenetre,
            text="Total : 0 dhs",
            font=("Arial", 16, "bold"),
            bg="#f0f8f8",
            fg="#27ae60",
            padx=10,
            pady=10,
        )
        self.affichage_total.pack(side=tk.BOTTOM, pady=10)

    def reduire_quantite(self, produit):
        def fonction():
            self.modifier_commande(produit, -1)
        return fonction

    def augmenter_quantite(self, produit):
        def fonction():
            self.modifier_commande(produit, 1)
        return fonction

    def modifier_commande(self, produit, valeur):
        self.commande[produit] = max(0, self.commande[produit] + valeur)
        self.affichages_quantites[produit]['text']=str(self.commande[produit])
        self.mettre_a_jour_total()

    def reinitialiser(self):
        for produit in self.commande:
            self.commande[produit] = 0
            self.affichages_quantites[produit]['text']="0"
        self.mettre_a_jour_total()

    def mettre_a_jour_total(self):
        total = sum(quantite * produits[produit] for produit, quantite in self.commande.items())
        self.affichage_total['text'] = f"Total : {total} dhs"


root = tk.Tk()
application = snackApp(root)
root.mainloop()
