from tkinter import *
from tkinter import messagebox, ttk
import statistics
import threading
import time

root = Tk()
root.title("Bombas para la Rxn")
root.geometry("180x80")


def get_grid_values1():
    global cb1f
    cb1f = []
    for rw1 in range(k-2):
        cmbbx1 = combobox_grid1[rw1][0]
        selected_value1 = cmbbx1.get()
        cb1f.append(selected_value1)
    print(cb1f)


def get_grid_values2():
    global cb2f
    cb2f = []
    for rw2 in range(k-2):
        cmbbx2 = combobox_grid2[rw2][0]
        selected_value2 = cmbbx2.get()
        cb2f.append(selected_value2)
    print(cb2f)


listpin = [13, 22, 27, 17, 19, 26, 21, 20, 16]
combobox_grid1 = []
combobox_grid2 = []


def legnd():
    legd = Tk()
    legd.title("Leyenda")
    for q in range(5):
        bomba = Canvas(legd, height=200, width=200)
        bomba.grid(row=0, column=q, columnspan=1, ipadx=20)
        pumplabel = Label(legd, text="Bomba " + str(q + 1), bg='#6AADBF', font=("Cambria", 13))
        pumplabel.grid(row=1, column=q, columnspan=1)
        pump_pinlbl = Label(legd, text="Pin " + str(listpin[q]), bg="#6AADBF", font=("Cambria", 13))
        pump_pinlbl.grid(row=2, column=q, columnspan=1)
        pump1 = bomba.create_oval(50, 10, 200, 160, fill="green", outline="black")
        c1 = bomba.create_oval(121, 80, 131, 90, fill="black", outline="")
        tube1_1 = bomba.create_rectangle(100, 155, 105, 200, fill="white", outline="black")
        tube2_1 = bomba.create_rectangle(145, 155, 150, 200, fill="white", outline="black")
    for q in range(4):
        bomba = Canvas(legd, height=200, width=200)
        bomba.grid(row=3, column=q, columnspan=1, ipadx=20)
        pumplabel = Label(legd, text="Bomba " + str(5 + q + 1), bg='#6AADBF', font=("Cambria", 13))
        pumplabel.grid(row=4, column=q, columnspan=1)
        pump_pinlbl = Label(legd, text=listpin[5 + q], bg="#6AADBF", font=("Cambria", 13))
        pump_pinlbl.grid(row=5, column=q, columnspan=1)
        pump1 = bomba.create_oval(50, 10, 200, 160, fill="green", outline="black")
        c1 = bomba.create_oval(121, 80, 131, 90, fill="black", outline="")
        tube1_1 = bomba.create_rectangle(100, 155, 105, 200, fill="white", outline="black")
        tube2_1 = bomba.create_rectangle(145, 155, 150, 200, fill="white", outline="black")

    def bttnwlgdc():
        legd.destroy()

    lgdbtn = Button(legd, text="Cerrar leyenda", command=bttnwlgdc, font=("Times New Roman", 15))
    lgdbtn.grid(row=6, column=q+1, columnspan=5, ipady=15, ipadx=50)


def createwin1():
    button1.destroy()
    global win1
    win1 = Tk()
    win1.title("Características de las bombas")
    loop1str = entry1.get()
    valuecb1 = ["Servicio", "Reactivo"]
    valuecb2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    labelwin1 = Label(win1, text="Definición de bombas")
    labelw2 = Label(win1, text="Tipo")
    labelw3 = Label(win1, text="Número")
    labelwin1.grid(row=0, column=0, columnspan=2)
    labelw2.grid(row=1, column=0)
    labelw3.grid(row=1, column=1)
    if loop1str.isdigit():
        loop1 = sum(int(digit) * 10 ** i for i, digit in enumerate(loop1str[::-1]))
        loop1 = loop1*2
        global k
        k = 2
        for i in range(0, loop1, 2):
            rcombbox1 = []
            rcombbox2 = []
            j = 0
            cb1 = ttk.Combobox(win1, value=valuecb1, width=10)
            cb1.grid(row=i+2, column=j)
            rcombbox1.append(cb1)
            combobox_grid1.append(rcombbox1)
            cb2 = ttk.Combobox(win1, value=valuecb2, width=10)
            cb2.grid(row=i+2, column=j+1, padx=10)
            rcombbox2.append(cb2)
            combobox_grid2.append(rcombbox2)
            k += 1
        buttonw1 = Button(win1, text="Aceptar", command=aceptar)
        buttonw1.grid(row=i+4, column=0, padx=10, columnspan=1, pady=10)
        buttonw1 = Button(win1, text="Salir", command=salir)
        buttonw1.grid(row=i+4, column=2, pady=10, ipadx=20)
        buttonlw1 = Button(win1, text="Abrir leyenda", command=legnd)
        buttonlw1.grid(row=i+4, column=1, pady=10)
    else:
        messagebox.showerror(message="Escribir dígitos, no palabras")
        win1.destroy()


def aceptar():
    win2 = Tk()
    win2.title("Selección de tiempos y orden de operación")
    kmin = k-2
    kmod = kmin % 3
    kd = int((k-2)/3)+1
    if kmin == 1:
        strwdthwin2 = "600"
    elif kmin == 2:
        strwdthwin2 = "1000"
    else:
        strwdthwin2 = "1400"
    if kmin <= 3:
        strlgthwin2 = "170"
    elif 3 < kmin <= 6:
        strlgthwin2 = "400"
    else:
        strlgthwin2 = "630"
    win2.geometry(strwdthwin2 + "x" + strlgthwin2)
    get_grid_values1()
    get_grid_values2()
    for ci in range(k-2):
        if cb1f[ci] == "":
            messagebox.showerror(message="Favor de completar todos los campos.")
            win2.destroy()
            return
    for bi in range(k - 2):
        if cb2f[bi] == "":
            messagebox.showerror(message="Favor de completar todos los campos.")
            win2.destroy()
            return
    mod2 = statistics.mode(cb2f)
    if cb2f.count(mod2) != 1:
        messagebox.showerror(message="Favor de no asignar un pin a más de una bomba.")
        win2.destroy()
        return
    kc = 0
    global listind
    global entrylist
    listind = []
    entrylist = []
    for ki in range(kd):
        if kmin >= 3:
            for kj in range(3):
                if cb1f[3*kc+kj] == "Servicio":
                    clrfll = ""
                    txt1 = "Bomba de Servicio"
                if cb1f[3*kc+kj] == "Reactivo":
                    clrfll = "green"
                    txt1 = "Bomba de Proceso"
                bomba = Canvas(win2, height=60, width=200)
                pumplabel = Label(win2, text=txt1, bg='#6AADBF', font=("Cambria", 13))
                pumppinlabel = Label(win2, text="Bomba " + cb2f[3*kc+kj], font=("Cambria", 13))
                pumpnolbl = Label(win2, text="Número", bg='#6AADBF', font=("Cambria", 13))
                pumpno = Label(win2, text=str(3*kc+kj+1), font=("Cambria", 13))
                entrywin2 = Entry(win2, width=10)
                entrylist.append(entrywin2)
                vollable = Label(win2, text="Veces", font=("Cambria", 13))
                pumplabel.grid(row=4*ki, column=2*kj, columnspan=1)
                pumppinlabel.grid(row=4*ki+1, column=2*kj, columnspan=1)
                bomba.grid(row=4*ki+2, column=2*kj, columnspan=1, ipadx=20)
                pumpnolbl.grid(row=4*ki, column=2*kj+1, columnspan=1)
                pumpno.grid(row=4*ki+1, column=2*kj+1, columnspan=1)
                entrywin2.grid(row=4*ki+3, column=2*kj, columnspan=1, pady=15)
                vollable.grid(row=4*ki+3, column=2*kj+1, columnspan=1)
                # (x start, y start, x finish, y finish)
                pump = bomba.create_oval(95, 10, 145, 60, fill=clrfll, outline="black")
                c1 = bomba.create_oval(115, 30, 125, 40, fill="black", outline="")
                listind.append((ki, kj))
        else:
            for kj in range(kmod):
                if cb1f[3*kc+kj] == "Servicio":
                    clrfll = ""
                    txt1 = "Bomba de Servicio"
                if cb1f[3*kc+kj] == "Reactivo":
                    clrfll = "green"
                    txt1 = "Bomba de Proceso"
                bomba = Canvas(win2, height=60, width=200)
                pumplabel = Label(win2, text=txt1, bg='#6AADBF', font=("Cambria", 13))
                pumppinlabel = Label(win2, text="Bomba " + cb2f[3*kc+kj], font=("Cambria", 13))
                pumpnolbl = Label(win2, text="Número", bg='#6AADBF', font=("Cambria", 13))
                pumpno = Label(win2, text=str(3*kc+kj+1), font=("Cambria", 13))
                entrywin2 = Entry(win2, width=10)
                entrylist.append(entrywin2)
                vollable = Label(win2, text="Veces", font=("Cambria", 13))
                pumplabel.grid(row=4*ki, column=2*kj, columnspan=1)
                pumppinlabel.grid(row=4*ki+1, column=2*kj, columnspan=1)
                bomba.grid(row=4*ki+2, column=2*kj, columnspan=1, ipadx=20)
                pumpnolbl.grid(row=4*ki, column=2*kj+1, columnspan=1)
                pumpno.grid(row=4*ki+1, column=2*kj+1, columnspan=1)
                entrywin2.grid(row=4*ki+3, column=2*kj, columnspan=1, pady=15)
                vollable.grid(row=4*ki+3, column=2*kj+1, columnspan=1)
                pump = bomba.create_oval(95, 10, 145, 60, fill=clrfll, outline="black")
                c1 = bomba.create_oval(115, 30, 125, 40, fill="black", outline="")
                listind.append((ki, kj))
        kmin = kmin-3
        kc += 1

    def cambiarnp():
        win3 = Tk()
        win3.title("Nombramiento de sustancias")
        win3lbl1 = Label(win3, text="Sustancia")
        win3lbl2 = Label(win3, text="Número de bomba")
        win3ent1 = Entry(win3)
        win3ent2 = Entry(win3)
        win3lbl1.grid(row=0, column=0)
        win3lbl2.grid(row=1, column=0)
        win3ent1.grid(row=0, column=1)
        win3ent2.grid(row=1, column=1)

        def cerrar():
            win3.destroy()

        def aplicarlbl():
            text1 = win3ent1.get()
            text2str = win3ent2.get()
            text2 = sum(int(digit) * 10 ** i for i, digit in enumerate(text2str[::-1]))
            indx = listind[text2-1][0]
            indy = listind[text2-1][1]
            sustlbl = Label(win2, text=text1, bg='#6AADBF', font=("Cambria", 13))
            sustlbl.grid(row=4*indx+2, column=2*indy+1)
        pumpcbtn = Button(win3, text="Cerrar", command=cerrar)
        pumpcbtn.grid(row=2, column=2, columnspan=1, padx=10, pady=5)
        win3btn = Button(win3, text="Agregar nombre del reactivo", command=aplicarlbl)
        win3btn.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    def win2cerrar():
        win2.destroy()
    pumpbtn = Button(win2, text="Nombre de sustancia", command=cambiarnp, font=("Cambria", 13))
    pumpbtn.grid(row=0, column=7, columnspan=1, padx=10)
    pumpbtn = Button(win2, text="Cancelar", command=win2cerrar, font=("Cambria", 13))
    pumpbtn.grid(row=1, column=6, columnspan=1, padx=10, pady=5)
    pumpbtn = Button(win2, text="Siguiente", command=win2aceptar, font=("Cambria", 13))
    pumpbtn.grid(row=0, column=6, columnspan=1, padx=10)
    print(listind)


def win2aceptar():
    values = []
    win4 = Tk()
    win4.title("Selección de volúmenes")
    kmax = k-2
    for kmax in entrylist:
        val = kmax.get()
        values.append(val)
    kmaxc = 0
    global loop2list
    loop2list = []
    for kmax in values:
        valind = values[kmaxc]
        if valind.isdigit():
            loop2 = sum(int(digit) * 10 ** i for i, digit in enumerate(valind[::-1]))
            loop2list.append(loop2)
        else:
            messagebox.showerror(message="Favor de llenar los campos correctamente.")
            win4.destroy()
        kmaxc += 1
    print(loop2list)
    global lenlist2
    lenlist2 = len(loop2list)
    kmaxi = 0
    global entrywin4
    entrywin4 = []
    global vezlist
    vezlist = []
    for kl in range(lenlist2):
        entrywin4row = []
        kmaxj = 0
        vwin4lbl = Label(win4, text="Orden")
        twin4lbl = Label(win4, text="Volumen [mL]")
        bwin4lbl = Label(win4, text="Bomba " + str(kmaxi + 1))
        bwin4lbl.grid(row=2*kmaxi, column=kmaxj, columnspan=1, sticky=W, padx=5)
        vwin4lbl.grid(row=2*kmaxi, column=kmaxj+1, columnspan=1, sticky=W, padx=5)
        twin4lbl.grid(row=2*kmaxi+1, column=kmaxj+1, columnspan=1, sticky=W, padx=5)
        vez = loop2list[kl]
        vezlist.append(vez)
        for kll in range(vez):
            entrywin4col = []
            for kli in range(2):
                win4entry = Entry(win4, width=10)
                win4entry.grid(row=2*kmaxi+kli, column=kmaxj+2, columnspan=1, padx=5, pady=5)
                entrywin4col.append(win4entry)
            entrywin4row.append(entrywin4col)
            kmaxj += 1
        entrywin4.append(entrywin4row)
        kmaxi += 1

    def win4destroy():
        win4.destroy()

    win5btn = Button(win4, text="Siguiente", command=win5)
    win4desbtn = Button(win4, text="Cancelar", command=win4destroy)
    win5btn.grid(row=2*kmaxi, column=0, columnspan=1, pady=5, padx=5)
    win4desbtn.grid(row=2*kmaxi, column=1, columnspan=1, pady=5, padx=5)


def win5():
    win5 = Tk()
    win5.title("Prevista")
    gridentrystr = []
    for gc in range(lenlist2):
        gridcolentstr = []
        vl = vezlist[gc]
        for gr in range(vl):
            gridrowentstr = []
            for two in range(2):
                enter = entrywin4[gc][gr][two]
                enr = enter.get()
                gridrowentstr.append(enr)
            gridcolentstr.append(gridrowentstr)
        gridentrystr.append(gridcolentstr)
    gridentry = []
    for sc in range(lenlist2):
        gridcolent = []
        sl = vezlist[sc]
        for sr in range(sl):
            gridrowent = []
            for dos in range(2):
                enterint = gridentrystr[sc][sr][dos]
                if enterint.isdigit():
                    loop3 = sum(int(digit) * 10 ** i for i, digit in enumerate(enterint[::-1]))
                    gridrowent.append(loop3)
                else:
                    messagebox.showerror(message="Favor de sólo escribir números.")
                    gridentry = []
                    win5.destroy()
                    return
            gridcolent.append(gridrowent)
        gridentry.append(gridcolent)
    global listabomba
    listabomba = []
    for lp in range(len(cb2f)):
        cb2fi = cb2f[lp]
        cb2fi = (sum(int(digit) * 10 ** i for i, digit in enumerate(cb2fi[::-1])))
        listabomba.append(cb2fi)
    global listadopin
    global listatiempoescogido
    global listaconvescogida
    listadopin = []
    listadebombas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    listatiempocarga = [1, 17, 18, 18, 55, 45, 70, 25, 15]
    listaconv = [28, 0.25, 0.22, 0.28, 57, 58, 59, 45, 56]
    listatiempoescogido = []
    listaconvescogida = []
    for lbi in range(len(listabomba)):
        for bli in range(len(listadebombas)):
            if listabomba[lbi] == listadebombas[bli]:
                listadopin.append(listpin[bli])
                listatiempoescogido.append(listatiempocarga[bli])
                listaconvescogida.append(listaconv[bli])
    maximum = []
    maximumsin = []
    for r in range(len(gridentry)):
        maximumcol = []
        for s in range(len(gridentry[r])):
            maximumcol.append(gridentry[r][s][0])
            maximumsin.append(gridentry[r][s][0])
        maximum.append(maximumcol)
    mm = max(maximumsin)
    for ege in range(len(gridentry)):
        for egej in range(len(gridentry[ege]) - 1):
            if gridentry[ege][egej][0] >= gridentry[ege][egej + 1][0]:
                messagebox.showerror("Orden", "Favor de ingresar los tiempos en orden")
                win5.destroy()
                return
    global rango
    rango = []
    for r in range(mm):
        rango.append(r + 1)
    for r in range(len(gridentry)):
        if len(rango) != len(gridentry[r]):
            for ij in range(len(rango) - len(gridentry[r])):
                gridentry[r].append([0, 0])
        for s in range(len(rango)):
            if rango[s] == gridentry[r][s][0]:
                gridentry[r][s] = gridentry[r][s]
            else:
                if s < len(gridentry[r]):
                    for t in range((len(rango) - 1) - s):
                        gridentry[r][len(rango) - 1 - t] = gridentry[r][len(rango) - t - 2]
                    gridentry[r][s] = [rango[s], 0]
    global listaentrywin6
    listaentrywin6 = []
    for lk in range(len(listabomba)):
        labell = Label(win5, text="Bomba " + str(listabomba[lk]))
        labelp = Label(win5, text="Pin " + str(listadopin[lk]))
        labell.grid(row=lk + 1, column=0, padx=5)
        labelp.grid(row=lk+1, column=1, padx=5)
    msgwin5 = messagebox.askquestion("Tiempos de carga", "¿Desea ocupar los valores por defecto?")
    if msgwin5 == "yes":
        labeltt = Label(win5, text="Tiempo de carga [s]")
        labeltt.grid(row=0, column=3)
        for td in range(len(listatiempoescogido)):
            label = Label(win5, text=str(listatiempoescogido[td]))
            label.grid(row=td+1, column=3)
            listaentrywin6.append(listatiempoescogido[td])
    else:
        win6 = Tk()
        win6.title("Escoger valores default")
        win6entrylist = []
        win6label = Label(win6, text="Bomba")
        win6label2 = Label(win6, text="Tiempo de carga [s]")
        win6label.grid(row=0, column=0, pady=5)
        win6label2.grid(row=1, column=0, pady=5)
        for tdw in range(len(listatiempoescogido)):
            labelwin6 = Label(win6, text="Bomba " + str(listabomba[tdw]))
            entrywin6 = Entry(win6, width=5)
            win6entrylist.append(entrywin6)
            labelwin6.grid(row=0, column=tdw+1, pady=5)
            entrywin6.grid(row=1, column=tdw+1, pady=5)

        def cmdwin6():
            for wse in range(len(win6entrylist)):
                entrywin6valstr = win6entrylist[wse].get()
                entrywin6val = sum(int(digit) * 10 ** i for i, digit in enumerate(entrywin6valstr[::-1]))
                listaentrywin6.append(entrywin6val)
                labeltt = Label(win5, text="Tiempo de carga [s]")
                labeltt.grid(row=0, column=3)
            for td in range(len(listaentrywin6)):
                label = Label(win5, text=str(listaentrywin6[td]))
                label.grid(row=td + 1, column=3)
            win6.destroy()

        def cmdwin6lg():
            win6lg = Tk()
            win6lg.title("Tiempos de carga varios")
            listacarga = [["EtOH", 45], ["NaOH", 55], ["Benzaldehído", 50]]
            for lgd in range(len(listacarga)):
                labellg1 = Label(win6lg, text=listacarga[lgd][0])
                labellg2 = Label(win6lg, text=str(listacarga[lgd][1]))
                labellg1.grid(row=lgd, column=0, pady=5, padx=10)
                labellg2.grid(row=lgd, column=1, pady=5, padx=10)
            win6lgdbtn = Button(win6lg, text="Cerrar", command=win6lg.destroy)
            win6lgdbtn.grid(row=len(listacarga)+1, column=0, columnspan=2)

        win6btn = Button(win6, text="Cargar tiempos", command=cmdwin6)
        win6btn.grid(row=2, column=0, columnspan=len(listatiempoescogido)+1)
        win6lgbtn = Button(win6, text="Sustancias", command=cmdwin6lg)
        win6lgbtn.grid(row=3, column=0, columnspan=len(listatiempoescogido)+1)

    for t in range(len(rango)):
        labeln = Label(win5, text="Volumen " + str(t+1))
        labeln.grid(row=0, column=t + 4)
    for r in range(len(gridentry)):
        for s in range(len(rango)):
            label = Label(win5, text=str(gridentry[r][s][1]))
            label.grid(row=r + 1, column=s + 4)
    global valoresbomba
    valoresbomba = []
    for tim in range(len(rango)):
        valoresbombacol = []
        for timb in range(len(listabomba)):
            valoresbombacol.append(gridentry[timb][tim][1])
        valoresbomba.append(valoresbombacol)

    for lew6 in range(len(rango)):
        lewcount = 0
        for lewj in range(len(listabomba)):
            if valoresbomba[lew6][lewj] == 0:
                lewcount += 1
        if lewcount == len(listabomba):
            messagebox.showerror("Datos", "Favor de no colocar un tiempo con sólo ceros")
            win5.destroy()
            return

    def win5close():
        win5.destroy()

    win5delbtn = Button(win5, text="Cancelar", command=win5close)
    win5printbtn = Button(win5, text="Iniciar reacción", command=oopfun)
    win5delbtn.grid(row=len(gridentry)+2, column=0, columnspan=2)
    win5printbtn.grid(row=len(gridentry)+2, column=3, columnspan=2)


def oopfun():
    valoresml = []
    for ir in range(len(rango)):
        valoresmlcol = []
        for jr in range(len(valoresbomba[ir])):
            valoresmlcol.append(round(valoresbomba[ir][jr]/listaconvescogida[jr], 1))
        valoresml.append(valoresmlcol)

    print(listabomba)
    # Bombas escogidas.
    print(listaentrywin6)
    # Tiempos de carga, sean default o dados por el usuario.
    print(listaconvescogida)
    # Conversión de mL a s.
    print(listadopin)
    # Lista de pines.
    print(valoresbomba)
    # mL que da el usuario en la ventana cuatro.
    print(valoresml)
    # Valores convertidos a tiempo.

    def bomba(ir, jr):
        print(f"Bomba {listabomba[jr]} encendida")
        print(listadopin[jr]*valoresml[ir][jr])
        print(type(valoresml[ir][jr]))
        time.sleep(listabomba[jr]*2)
        print(f"Bomba {listabomba[jr]} apagada")

    def bombacarga(jr):
        print(f"Bomba {listabomba[jr]} encendida")
        print(listadopin[jr]*listaentrywin6[jr])
        print(type(valoresml[ir][jr]))
        time.sleep(listabomba[jr]*2)
        print(f"Bomba {listabomba[jr]} apagada")

    threadcarga = []
    for jr in range(len(listabomba)):
        ooptc = threading.Thread(target=bombacarga, args=(jr,))
        threadcarga.append(ooptc)
        ooptc.start()
    for jr in threadcarga:
        jr.join()

    threadlist = []
    for ir in range(len(rango)):
        threadlistcol = []
        for jr in range(len(valoresbomba[ir])):
            oopt = threading.Thread(target=bomba, args=(ir, jr,))
            threadlistcol.append(oopt)
        threadlist.append(threadlistcol)

    for ir in range(len(rango)):
        for thread in threadlist[ir]:
            thread.start()
        for thread in threadlist[ir]:
            thread.join()
        time.sleep(5)

    messagebox.showinfo("Finalización", "Proceso terminado.")


def salir():
    win1.destroy()
    root.destroy()


labelr1 = Label(root, text="Número de bombas deseadas:")
labelr1.grid(row=0, column=0, columnspan=2, ipady=10)
entry1 = Entry(root, width=5)
entry1.grid(row=1, column=0, columnspan=1)
button1 = Button(root, command=createwin1, text="Aceptar")
button1.grid(row=1, column=1, ipadx=15, padx=20)
mainloop()
