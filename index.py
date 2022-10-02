import pandas as pd
import matplotlib.pyplot as plt
import time


def menu():
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Modificar")
    print("4. Eliminar")
    print("5. Graficar")
    print("6. Exportar")
    print("7. Salir")

    opc = int(input("Selecciona una opción: "))

    if opc == 1:
        agregar()
    elif opc == 2:
        mostrar()
    elif opc == 3:
        modificar()
    elif opc == 4:
        eliminar()
    elif opc == 5:
        graficar()
    elif opc == 6:
        exportar()
    elif opc == 7:
        print("Gracias por usar el programa")
    else:
        print("Opción no válida, intente nuevamente: ")
        menu()


def agregar():
    datos = pd.read_csv("Grupo.csv", header=0)
    print(datos)
    print("Ingrese el id del alumno: ")
    try:
        id = int(input())
    except ValueError:
        print("Ingrese solo numeros en el id")
        time.sleep(2)
        agregar()
    if id in datos["Codigo"].values:
        print("El id ya existe")
        time.sleep(2)
        agregar()
        return
    print("Ingrese el nombre del alumno: ")
    nombre = input()
    print("Ingrese la nota del taller: ")
    try:
        taller = float(input())
    except ValueError:
        print("No se pueden ingresar letras")
        time.sleep(2)
        agregar()
        return
    print("Ingrese la nota de la investigacion: ")
    try:
        investigacion = float(input())
    except ValueError:
        print("No se pueden ingresar letras")
        time.sleep(2)
        agregar()
        return
    print("Ingrese nota del parcial: ")
    try:
        parcial = float(input())
    except ValueError:
        print("No se pueden ingresar letras")
        time.sleep(2)
        agregar()
        return
    datos = datos.append(
        {
            "Codigo": id,
            "Nombre": nombre,
            "Taller": taller,
            "Investigacion": investigacion,
            "Parcial": parcial,
        },
        ignore_index=True,
    )
    datos.to_csv("Grupo.csv", index=False)

    datos["Definitiva"] = datos.iloc[:, [2, 3, 4]].mean(axis=1)
    datos["Definitiva"] = datos["Definitiva"].round(2)
    datos.loc[datos["Definitiva"] < 3.0, "Aprobado"] = "No"
    datos.loc[datos["Definitiva"] >= 3.0, "Aprobado"] = "Si"
    print("Datos agregados")
    print(datos)

    datos.to_csv("Grupo.csv", index=False)

    print("---------------------------------------------------")
    menu()


def mostrar():
    datos = pd.read_csv("Grupo.csv", header=0)
    datos["Definitiva"] = datos.iloc[:, [2, 3, 4]].mean(axis=1)
    datos["Definitiva"] = datos["Definitiva"].round(2)
    datos.loc[datos["Definitiva"] < 3.0, "Aprobado"] = "No"
    datos.loc[datos["Definitiva"] >= 3.0, "Aprobado"] = "Si"
    datos = datos.sort_values(by="Definitiva", ascending=False)
    print(datos)
    print("-----------------------------------------------------")
    print(datos.iloc[:, [1, 5, 6]].head(5))
    print("-----------------------------------------------------")
    print(datos.iloc[:, [1, 5, 6]].tail(5))
    print("-----------------------------------------------------")
    datos.to_csv("Grupo.csv", index=False)
    menu()


def modificar():
    datos = pd.read_csv("Grupo.csv", header=0)
    print(datos)
    print("Ingrese el id del alumno a modificar: ")
    id = float(input())
    if id not in datos["Codigo"].values:
        print("El id no existe")
        time.sleep(2)
        modificar()
        return
    print("Ingrese el nuevo nombre")
    nuevo_nombre = input()
    print("Ingrese la nueva nota del taller: ")
    try:
        nuevo_taller = float(input())
    except ValueError:
        print("No se pueden ingresar letras")
        time.sleep(2)
        modificar()
        return
    print("Ingrese la nueva nota del investigacion: ")
    try:
        nueva_investigacion = float(input())
    except ValueError:
        print("No se pueden ingresar letras")
        time.sleep(2)
        modificar()
        return
    print("Ingrese nuevo parcial: ")
    try:
        nuevo_parcial = float(input())
    except ValueError:
        print("No se pueden ingresar letras")
        time.sleep(2)
        modificar()
        return

    datos.loc[datos["Codigo"] == id, "Nombre"] = nuevo_nombre
    datos.loc[datos["Codigo"] == id, "Taller"] = nuevo_taller
    datos.loc[datos["Codigo"] == id, "Investigacion"] = nueva_investigacion
    datos.loc[datos["Codigo"] == id, "Parcial"] = nuevo_parcial
    datos.to_csv("Grupo.csv", index=False)

    datos["Definitiva"] = datos.iloc[:, [2, 3, 4]].mean(axis=1)
    datos["Definitiva"] = datos["Definitiva"].round(2)
    datos.loc[datos["Definitiva"] < 3.0, "Aprobado"] = "No"
    datos.loc[datos["Definitiva"] >= 3.0, "Aprobado"] = "Si"
    print("Datos modificados")
    print(datos)
    print("---------------------------------------------------")

    datos.to_csv("Grupo.csv", index=False)
    menu()


def eliminar():
    datos = pd.read_csv("Grupo.csv", header=0)
    print(datos)
    print("Ingrese el id del alumno a eliminar: ")
    id = float(input())
    if id not in datos["Codigo"].values:
        print("El id no existe")
        time.sleep(2)
        eliminar()
        return
    datos = datos[datos.Codigo != id]
    datos.to_csv("Grupo.csv", index=False)
    print("Datos eliminados")
    print(datos)

    print("---------------------------------------------------")

    datos.to_csv("Grupo.csv", index=False)
    menu()


def graficar():
    datos = pd.read_csv("Grupo.csv", header=0)
    datos["Taller"].value_counts().plot(kind="pie", autopct="%0.1f %%")
    plt.title("Taller")
    plt.show()
    print("---------------------------------------------------")
    datos["Investigacion"].value_counts().plot(kind="pie", autopct="%0.1f %%")
    plt.title("Investigacion")
    plt.show()
    print("---------------------------------------------------")
    datos["Parcial"].value_counts().plot(kind="pie", autopct="%0.1f %%")
    plt.title("Parcial")
    plt.show()
    print("---------------------------------------------------")
    datos["Aprobado"].value_counts().plot(kind="pie", autopct="%0.1f %%")
    plt.title("Aprobado")
    plt.show()
    print("---------------------------------------------------")
    menu()


def exportar():
    datos = pd.read_csv("Grupo.csv", header=0)
    datos.to_excel("Grupo.xlsx", index=False)
    print("Datos exportados")
    print("---------------------------------------------------")
    menu()


if __name__ == "__main__":
    menu()
