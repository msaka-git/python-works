#! /usr/bin/env python
# -*- coding: utf-8 -*-


import os
import subprocess
import shutil



class find():

    print("*************"
          "PROGAMME POUR TRAITEMENT DES FICHIERS"
          "*************")

    def file_move(self):
        self.date_debut = input("Entrez la date de deubut (ex. 20180101): ")
        self.heure_debut = input("Entrez l'heure de debut (ex.0000.00):")
        self.date_fin = input("Entrez la date de fin (ex.20181231): ")
        self.heure_fin = input("Entrez l'heure de fin (ex.2359.59): ")
        os.system("touch -t '{}''{}' start-'{}'.debut".format(self.date_debut, self.heure_debut, self.date_debut))
        os.system("touch -t '{}''{}' stop-'{}'.fin".format(self.date_fin, self.heure_fin, self.date_fin))

        os.system("mv start-{0}.debut /tmp".format(self.date_debut))
        os.system("mv stop-{0}.fin /tmp".format(self.date_fin))

    def recherce_par_nom(self):
        self.nom = input("Nom du fichier: ")
        self.repertoire = input("Repertoire: ")
        while True:
            print("\n***\nChoisir type de l'operation:\n***\n")
            print("\n1) Lister les fichiers\n")
            print("\n2) Compresser les fichiers\n")
            print("\n3) Supprimer les fichiers\n")
            print("\n4) Archiver les fichiers\n")
            print("\nAppuyez sur 'q' pour quitter")

            choice=input("Votre choix: (ex.5): ")


            if (choice == "1"):
                print("\n***FICHIERS***\n")
                os.system("sudo find {} -maxdepth 1 -iname '{}' -type f -ls".format(self.repertoire, self.nom))

            elif (choice == "2"):
                print("\n***Fichiers compresses***\n")
                os.system("sudo find {} -maxdepth 1 -iname '{}' -type f -exec gzip -9 {{}} \;".format(self.repertoire, self.nom))

            elif (choice == "3"):
                print("\n***Fichiers Supprimes***\n")
                os.system("sudo find {} -maxdepth 1 -iname '{}' -type f -delete".format(self.repertoire, self.nom))

            elif (choice == "4"):
                print("\n***Archivage des Fichiers***\n")
                nom_archive=input("Nom de l'archive: ")
                self.deplacer=input("Deplacer a (par defaut {}): ".format(self.repertoire))
                os.chdir("{}".format(self.repertoire))
                os.system("sudo find . -maxdepth 1 -iname '{}' -type f -print0 | sudo tar czvf {}.tar.gz --null -T -"
                          .format(self.nom,nom_archive))
                if (self.deplacer == ""):
                    pass
                else:
                    os.system("sudo mv {}.tar.gz {}".format(nom_archive, self.deplacer))

            elif (choice == "q"):
                break

            else:
                print("Operation non valide")


    def recherche_par_date(self):
        self.repertoire = input("Repertoire: ")

        while True:
            print("\n***\nChoisir type de l'operation:\n***\n")
            print("\n1) Lister les fichiers\n")
            print("\n2) Compresser les fichiers\n")
            print("\n3) Supprimer les fichiers\n")
            print("\n4) Archiver les fichiers\n")
            print("\nAppuyez sur 'q' pour quitter")

            choice = input("Votre choix: (ex.5): ")


            if (choice == "1"):

                opt1=input("Recherchez par nom? (o/n): ")
                if (opt1 == "o"):
                    self.nom = input("Nom du fichier: ")
                    find.file_move()
                    print("\n***FICHIERS***\n")
                    os.system("sudo find {} -maxdepth 1 -type f -iname '{}' -newer /tmp/start-{}.debut -a ! -newer /tmp/stop-{}.fin -ls".format(
                        self.repertoire, self.nom, self.date_debut, self.date_fin))
                elif (opt1 == "n"):
                    find.file_move()
                    print("\n***FICHIERS***\n")
                    os.system("sudo find {} -maxdepth 1 -type f -newer /tmp/start-{}.debut -a ! -newer /tmp/stop-{}.fin -ls".format(
                            self.repertoire, self.date_debut, self.date_fin))
                else:
                    print("Choix invalid")

            elif (choice == "2"):

                opt1 = input("Recherchez par nom? (o/n): ")
                if (opt1 == "o"):
                    self.nom = input("Nom du fichier: ")
                    find.file_move()
                    print("\n***Fichiers compresses***\n")
                    os.system(
                        "sudo find {} -maxdepth 1 -type f -iname {} -newer /tmp/start-{}.debut -a ! -newer /tmp/stop-{}.fin -exec gzip -9 {{}} \;".format(
                            self.repertoire, self.nom, self.date_debut, self.date_fin))
                elif (opt1 == "n"):
                    find.file_move()
                    print("\n***Fichiers compresses***\n")
                    os.system(
                        "sudo find {} -maxdepth 1 -type f -newer /tmp/start-{}.debut -a ! -newer /tmp/stop-{}.fin -gzip -9".format(
                            self.repertoire, self.date_debut, self.date_fin))
                else:
                    print("Choix invalid")

            elif (choice == "3"):

                opt1 = input("Recherchez par nom? (o/n): ")
                if (opt1 == "o"):
                    self.nom = input("Nom du fichier: ")
                    find.file_move()
                    print("\n***Fichiers Supprimes***\n")
                    os.system(
                        "sudo find {} -maxdepth 1 -type f -iname '{}' -newer /tmp/start-{}.debut -a ! -newer /tmp/stop-{}.fin -delete".format(
                            self.repertoire, self.nom, self.date_debut, self.date_fin))
                elif (opt1 == "n"):
                    find.file_move()
                    print("\n***Fichiers Supprimes***\n")
                    os.system(
                        "sudo find {} -maxdepth 1 -type f -newer /tmp/start-{}.debut -a ! -newer /tmp/stop-{}.fin -delete".format(
                            self.repertoire, self.date_debut, self.date_fin))
                else:
                    print("Choix invalid")

            elif (choice == "4"):
                opt1 = input("Recherchez par nom? (o/n): ")
                if (opt1 == "o"):
                    self.nom = input("Nom du fichier: ")
                    find.file_move()
                    print("\n***Archivage des Fichiers***\n")
                    nom_archive = input("Nom de l'archive: ")
                    self.deplacer = input("Deplacer a (par defaut {}): ".format(self.repertoire))
                    os.chdir("{}".format(self.repertoire))
                    os.system("sudo find . -maxdepth 1 -iname '{}' -type f -newer /tmp/start-{}.debut -a ! -newer /tmp/stop-{}.fin -print0 | sudo tar czvf {}.tar.gz --null -T -"
                              .format(self.nom, self.date_debut, self.date_fin, nom_archive))
                    if (self.deplacer == ""):
                        pass
                    else:
                        os.system("sudo mv {}.tar.gz {}".format(nom_archive, self.deplacer))
                elif (opt1 == "n"):

                    find.file_move()
                    print("\n***Archivage des Fichiers***\n")
                    nom_archive = input("Nom de l'archive: ")
                    self.deplacer = input("Deplacer a (par defaut {}): ".format(self.repertoire))
                    os.chdir("{}".format(self.repertoire))
                    os.system(
                        "sudo find . -maxdepth 1 -type f -newer /tmp/start-{}.debut -a ! -newer /tmp/stop-{}.fin -print0 | sudo tar czvf {}.tar.gz --null -T -"
                        .format(self.date_debut, self.date_fin, nom_archive))
                    if (self.deplacer == ""):
                        pass
                    else:
                        os.system("sudo mv {}.tar.gz {}".format(nom_archive, self.deplacer))

            elif (choice == "q"):
                break
            else:
                print("Choix invalid")
            os.system("sudo rm -f /tmp/start-{}.debut /tmp/stop-{}.fin".format(self.date_debut, self.date_fin))



find = find()
while True:
    print("""

La commande find

1.Rechercher par nom

2.Rechercher par date

Appuyez sur 'q' pour quitter.


""")


    op = input("Choissez l'operation: ")
    if (op == "q"):
        print("Vous avez quitter")
        break
    elif (op == "1"):
        print("Traitement des fichiers...")
        find.recherce_par_nom()
    elif (op == "2"):
        print("Traitement des fichiers...")
        find.recherche_par_date()


    else:
        print("Operation invalide.")



